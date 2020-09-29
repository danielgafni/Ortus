<template>
  <section>
    <div class="containter">
      <b-row
        class="justify-content-md-center"
      >
        <b-col
          lg="4"
        >
          <h3>
            Setup Your Account:
          </h3>
          <b-form
            ref="regForm"
            class="needs-validation"
            :class="{'was-validated': invalid}"
            data-cy="reg-form"
            novalidate
            @submit.prevent="registerUser"
          >
            <b-form-group
              id="input-group-email"
              label="Email address:"
              label-for="input-email"
            >
              <b-form-input
                id="input-email"
                ref="email"
                v-model="form.email"
                type="email"
                required
                minlength="8"
                placeholder="Email address"
                data-cy="reg-email"
              />
            </b-form-group>

            <b-form-group
              id="input-group-password"
              label="Please enter a password:"
              label-for="input-password"
              required
              description="Use a strong unique password, 8 characheters long. Preferably created by a password manager."
            >
              <b-form-input
                id="input-password"
                ref="password"
                v-model="form.password"
                type="password"
                required
                data-cy="reg-password"
              />
            </b-form-group>

            <b-form-group
              id="input-group-name"
              label="Your Name:"
              label-for="input-name"
            >
              <b-row>
                <b-col md="6">
                  <b-form-input
                    id="input-first-name"
                    v-model="form.firstName"
                    required
                    placeholder="First name"
                    data-cy="reg-first-name"
                  />
                </b-col>
                <b-col md="6">
                  <b-form-input
                    id="input-last-name"
                    v-model="form.lastName"
                    required
                    placeholder="Last name"
                    data-cy="reg-last-name"
                  />
                </b-col>
              </b-row>
            </b-form-group>

            <b-form-group id="input-group-checkboxes">
              <b-form-checkbox-group
                id="checked-tos"
                v-model="form.checkedTOS"
                required
                data-cy="reg-tos-checkbox-group"
              >
                <b-form-checkbox
                  name="terms-of-service"
                  value="checked"
                >
                  I agree to the terms of service
                </b-form-checkbox>
                <b-form-invalid-feedback>
                  Please select review and agree to the terms of service.
                </b-form-invalid-feedback>
              </b-form-checkbox-group>
              <b-form-checkbox-group
                id="checked-newsletter"
                v-model="form.checkedNewsletter"
                data-cy="reg-newsletter-checkbox"
              >
                <b-form-checkbox
                  value="checked"
                >
                  Sign me up for your newsletter (optional)
                </b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>
            <b-button
              type="submit"
              variant="primary"
              data-cy="reg-submit"
            >
              Submit
            </b-button>
          </b-form>
        </b-col>
      </b-row>
    </div>
  </section>
</template>

<script>
  import Api from "@/services/Api"
  import axios from "axios"

  export default {
    data() {
      return {
        form: {
          email: this.$store.state.signup.email,
          firstName: '',
          lastName: '',
          password: null,
          checkedTOS: [],
          checkedNewsletter: []
        },
        invalid: null
      }
    },
    mounted: function() {
      if (this.$store.state.signup.email) {
        this.$refs.password.focus();
      } else {
        this.$refs.email.focus();
      }
    },
    methods: {
      registerUser() {
        if (!this.$refs.regForm.checkValidity()) {
          this.invalid = true
        } else {
          Api().post('/users', {
            email: this.form.email,
            password: this.form.password,
            first_name: this.form.firstName,
            last_name: this.form.lastName,
            wants_news: this.form.checkedNewsletter.includes('checked')
          }).then((resp) => {
            this.loginUser(this.form.email, this.form.password)
            this.$router.push('/passwords')
          })
            .catch((error) => {
              console.log(error)
              alert(error.response.data.message)
              this.invalid = true
            });
        }
      },
      loginUser(email, password) {
        Api().post('/login', { email: email, password: password, remember_me: false })
          .then((resp) => {
            if (resp.status === 201){
              let token = resp.data["token"];
              let isVerified = resp.data["is_verified"];
              axios.defaults.headers.common['Authorization'] = token
              this.$store.dispatch('user/load', {token: token, verified: isVerified})
              // this.$router.push('/onboarding')
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
</script>