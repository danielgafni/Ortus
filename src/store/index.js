import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

// import signup from "./signup.module";
// import user from "./user.module"

Vue.use(Vuex);

export default new Vuex.Store({
    plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
    modules: {
        signup, user
    }
});