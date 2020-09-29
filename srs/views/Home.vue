<template>
  <span>
    <section
      id="hero"
      class="d-flex align-items-center"
    >
      <div class="container">
        <div class="row">
          <div class="col-lg-6 pt-4 pt-lg-0 order-2 order-lg-1 d-flex flex-column justify-content-center">
            <h1>
              Distribute bulk orders <br>
              to your <u>Remote Team</u> with ease!
            </h1>
            <h2>Let us collect your team's shipping information 📝</h2>
            <h2>Order everything from any retailer 👕 👕 👕</h2>
            <h2>Ship <b>one box</b> directly to us 📦</h2>
            <h2>We ship your team 🚀</h2>
            <h2>Done! ✅</h2>
            <!--             <div><a href="#about" class="btn-get-started scrollto">Get Started</a></div> -->
          </div>
          <div class="col-lg-6 order-1 order-lg-2 hero-img">
            <img
              src="/img/flying-box.png"
              class="img-fluid"
              alt=""
            >
          </div>
        </div>
        <div class="row justify-content-center signup-section">
          <div class="col-lg-6 pt-4 d-flex flex-column justify-content-center">
            <h4>Join our private beta today:</h4>
            <form
              @submit.prevent="submitSignup"
            >
              <input
                v-model="signup.email"
                class="input-email"
                name="email"
                type="email"
                required
                placeholder="you@work.com"
                data-cy="singup-top-email"
              >
              <input
                type="submit"
                value="Sign Up"
                data-cy="singup-top-submit"
              >
            </form>

          </div>
        </div>
      </div>
    </section>

    <section
      id="about"
      class="about"
    >
      <div class="container">

        <div class="row">
          <div class="col-xl-5 col-lg-6 d-flex justify-content-center">
            <img
              class="lg img-fluid d-none d-lg-block"
              src="/img/packing-boxes.png"
            >
            <img
              class="sm img-fluid d-block d-lg-none"
              src="/img/packing-boxes.png"
            >
          </div>

          <div class="col-xl-7 col-lg-6 icon-boxes d-flex flex-column align-items-stretch justify-content-center py-5 px-lg-5">
            <h2>You've got better things to do...</h2>

            <div class="icon-box">
              <div class="icon"><i class="bx bx-customize" /></div>
              <h4 class="title">
                Ship what you want, from any store
              </h4>
              <p class="description">
                You know what your team needs.
                Custom t-shirt, socks, nerf guns, head phones.
                If you can buy it we'll get it to them.
              </p>
            </div>

            <div class="icon-box">
              <div class="icon"><i class="bx bx-smile" /></div>
              <h4 class="title">
                Hassle Free
              </h4>
              <p class="description">
                No serriously.
                With one link,
                we'll handle collecting your teams shipping info,
                t-shirt sizes, color preferences, favorite candy, head circumference.
                You name it, we got it.
              </p>
            </div>

            <div class="icon-box">
              <div class="icon"><i class="bx bx-dollar" /></div>
              <h4 class="title">
                One Packing and Shipping Payment
              </h4>
              <p class="description">
                This is where the real magic happens. Ok, actually it's pretty straight forward.
                We'll pack everything up and find you competive shipping rates.
                Then aggregate all the cost into one payment.
              </p>
            </div>

          </div>
        </div>

      </div>
    </section>

    <section class="d-flex align-items-center">

      <div class="container">
        <div class="row justify-content-center signup-section">
          <div class="col-lg-6 pt-4 d-flex flex-column justify-content-center">
            <h4>Join our private beta today:</h4>
            <form
              id="input-form-2"
              @submit.prevent="submitSignup"
            >
              <input
                v-model="signup.email"
                class="input-email"
                type="email"
                name="email"
                required
                placeholder="you@work.com"
                data-cy="singup-bottom-email"
              >
              <input
                type="submit"
                value="Sign Up"
                data-cy="singup-bottom-submit"
              >
            </form>
          </div>
        </div>
      </div>

    </section>

  </span>
</template>

<script>
import Api from '@/services/Api'

export default {
  name: 'Home',
  components: {
  },
  data() {
    return {
      // This is data storage with the Vue component, BOTH forms are hooked up to it via v-model
      // signup: {
      //   email: null,
      //   valid: null
      // },
    }
  },
  methods: {
    // submitSignup() {
    //   let signupEmail = this.signup.email;
    //   if (!signupEmail) {
    //     this.signup.valid = false
    //   } else {
    //       this.signup.valid = true
    //       Api().post('/signups', {email: signupEmail})
    //         .then((resp) => {
    //           this.$store.dispatch('signup/load', signupEmail)
    //           this.$router.push({path: '/register'})
    //         })
    //         .catch((error) => {
    //           this.signup.valid = false
    //           console.log(error)
    //         });
    //   }
    // }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
