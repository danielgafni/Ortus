
const state = {
  email: null
};

const getters = {
  email() {
    return state.email;
  }
};

const actions = {
  load(context, payload) {
    context.commit('load', payload);
    return payload;
  },
  unload(context, payload) {
    context.commit('unload', payload);
    return payload;
  }
};

const mutations = {
  load(state, email) {
    state.email = email;
  },
  unload(state) {
    state.email = null;
    state.errors = {};
  }
};

export default {
  namespaced: true,
  state: state,
  actions: actions,
  mutations: mutations,
  getters: getters
};