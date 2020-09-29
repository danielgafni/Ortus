<template>
  <!-- ======= Header ======= -->
  <header
    id="header"
    class="fixed-top"
  >
    <div class="container d-flex align-items-center">
      <h1
        class="logo mr-auto"
        data-cy="logo"
      >
        <a href="/">ORTUS 💫</a>
      </h1>

      <b-navbar class="nav-menu d-none d-lg-block">
        <ul>
          <li v-if="!isLoggedIn">
            <router-link
              to="/login"
              data-cy="nav-login"
            >
              Login
            </router-link>
          </li>
          <li v-if="isLoggedIn">
            <a
              href="#logout"
              @click="onLogout"
            >
              Logout
            </a>
          </li>
          <li v-if="(!isVerified === isLoggedIn)">
            <a
              href="#"
              @click="onVerify"
            >
              Verify Account
            </a>
          </li>
        </ul>
      </b-navbar>
    </div>
  </header>
</template>

<script>
import Api from '@/services/Api'
import axios from "axios";

export default {
  name: 'Header',
  data() {
    return {
    }
  },
  computed: {
    isLoggedIn:  function () {
      return !!this.$store.state.user.token
    },
    isVerified:  function () {
      return this.$store.state.user.isVerified
    }
  },
  methods: {
    // TODO: Make this call the logout helper method.
    onLogout() {
      // Remote the token first
      this.$store.dispatch('user/unload')
      sessionStorage.clear()
      // Then try to log out via the api
      Api().post('/logout')
        .then((resp) => {
          axios.defaults.headers.common['Authorization'] = ""
          this.$router.push({path: '/'})
        })
        .catch((error) => {
          // alert(error.data.message)
          this.$router.push({path: '/'})
        });
    },
    onVerify() {
      Api().post('/send_verification_email')
        .then((resp) => {
          if (resp.status === 200) {
            alert("Please visit the verification link in an email we've sent you!")
          }
          else {
            // console.log(resp)
            alert("Something went wrong!")
          }
        })
        .catch((error) => {
          if (error.message.includes("401")) {
            alert("Please authorize first.")
            this.$store.dispatch('user/load', {token: null, verified: false})
          } else {
            alert(error)
          }
          // this.$router.push({path: '/'})
        });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>