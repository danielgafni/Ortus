
<template>
  <div id="app">
    <Header />
    <div id="page-content">
      <router-view />
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
};
</script>
