
const state = {
  token: null,
  isVerified: false
};

const getters = {
  token() {
    return state.token;
  },
  isVerified() {
    return state.isVerified;
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
  load(state, data) {
    state.token = data.token;
    state.isVerified = data.verified;
  },
  unload(state) {
    state.token = null;
    state.isVerified = false;
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