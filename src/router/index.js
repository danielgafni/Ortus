import Vue from 'vue'
// import store from '../store' DRAFT
import VueRouter from 'vue-router'

import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Passwords from '@/views/Passwords.vue'
// import Dashboard from '@/views/Dashboard.vue'
// import Verify from '@/views/Verify.vue'

Vue.use(VueRouter)

// Draft of auth protection in Vue.
// Currently doesn't work because the `user` store does not exist at the moment of execution.
// Lines that belong to this draft are commented with DRAFT
// const ifNotAuthenticated = (to, from, next) => {
//   if (!store.getters.user.token) {
//     next()
//     return
//   }
//   next('/')
// }
//
// const ifAuthenticated = (to, from, next) => {
//   if (store.getters.user.token) {
//     next()
//     return
//   }
//   next('/login')
// }

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    // beforeEnter: ifNotAuthenticated DRAFT
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/passwords',
    name: 'passwords',
    component: Passwords,
    // beforeEnter: ifAuthenticated  DRAFT
  },
  // {
  //   path: '/dashboard',
  //   name: 'dashboard',
  //   component: Dashboard,
  //   // beforeEnter: ifAuthenticated DRAFT
  // },
  // {
  // path: '/account/verify',
  // name: 'verify',
  // component: Verify,
  // // beforeEnter: ifAuthenticated DRAFT
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: env.process.BASE_URL,
  routes
})

export default router
