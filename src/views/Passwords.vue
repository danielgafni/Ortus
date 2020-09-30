<template>
  <section>
    <div class="containter">
      <b-row
        class="justify-content-md-center"
      >
        <b-col
          lg="4"
        >
          <h3>Your passwords</h3>
          <hr>
            <div
              v-for="item in passwords"
              :key="item.name"
            >
              <b-form-group
                :label="item.name"
                description=""
              >
                {{ item.password }}
              </b-form-group>
              <hr>
            </div>
        </b-col>
      </b-row>
      <h2>This page is under construction...</h2>
    </div>
  </section>
</template>

<script>
  import Api from "@/services/Api";
  export default {
    data() {
      return {
        show: true,
        passwords: [{
          name: "reddit",
          password: 'password-for-reddit',
        },{
          name: "vk",
          password: 'password-for-vk',
        },{
          name: "google",
          password: 'password-for-google',
        }],
      }
    },
    methods: {
    }
  }
</script>