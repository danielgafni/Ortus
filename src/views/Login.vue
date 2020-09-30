<template>
  <section>
    <div class="containter">
      <b-row
        class="justify-content-md-center"
      >
        <b-col
          lg="3"
        >
          <h3>
            Login:
          </h3>
          <b-form
            ref="loginForm"
            class="needs-validation"
            :class="{'was-validated': invalid}"
            data-cy="login-form"
            novalidate
            @submit.prevent="loginUser"
          >
            <b-form-group
              id="input-group-email"
              label="Email address:"
              label-for="input-email"
            >
              <b-form-input
                id="input-email"
                v-model="form.email"
                type="email"
                required
                placeholder="you@work.com"
                data-cy="login-email"
              />
            </b-form-group>

            <b-form-group
              id="input-group-password"
              label="Password:"
              label-for="input-password"
              required
            >
              <b-form-input
                id="input-password"
                v-model="form.password"
                type="password"
                required
                data-cy="login-password"
              />
              <!--              <b-form-checkbox-group-->
              <!--                data-cy="login-remember-me-checkbox-group"-->
              <!--              >-->
              <!--                <b-form-checkbox -->
              <!--                  v-model="form.remember_me"-->
              <!--                  value="checked"-->
              <!--                >-->
              <!--                  Remember Me-->
              <!--                </b-form-checkbox>-->
              <!--              </b-form-checkbox-group>-->
            </b-form-group>

            <b-button
              type="submit"
              variant="primary"
              data-cy="login-submit"
            >
              Login
            </b-button>
          </b-form>

          <hr>

          <a href="/">I forgot my password.</a>
        </b-col>
      </b-row>
    </div>
  </section>
</template>

<script>
  import Api from "@/services/Api";
  import axios from "axios";

  export default {
    data() {
      return {
        form: {
          email: "",
          password: "",
          remember_me: []
        },
        invalid: null,
        localIsLoggedIn: localStorage.getItem('user-token')
      }
    },
    methods: {
      loginUser() {
        if (!this.$refs.loginForm.checkValidity()) {
          this.invalid = true
        } else {
          Api().post('/login', {
              email: this.form.email,
              password: this.form.password,
              remember_me: this.form.remember_me.includes("checked")
            })
            .then((resp) => {
              if (resp.status === 201){
                let token = resp.data["token"]
                axios.defaults.headers.common['Authorization'] = token
                let isVerified = resp.data["is_verified"]
                this.$store.dispatch('user/load', {token: token, verified: isVerified})
                this.$router.push("/passwords")
              }
              else if (resp.status === 401) {
                alert("Wrong email or password")
              }
            })
            .catch((error) => {
                alert(error)
              })
              // alert();
              this.valid = false;
              this.$store.dispatch('user/unload')
              this.form.password = ""
        }
      }
    }
  }
</script>