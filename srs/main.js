import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import LoadScript from 'vue-plugin-load-script'
import store from '@/store'


Vue.config.productionTip = false


Vue.use(LoadScript);
new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
