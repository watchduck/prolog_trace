import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

Vue.config.devtools = true;

export const store = new Vuex.Store({
  state: {
    input: '',
    output: {},
    error: null,
    showResults: false,
    focus: {row: null, col: null, knot: null, functor: null},
    showCustomNames: true,
    errorsCustomName: [],
    showTermTables: false
  },
  mutations: {
    mutInput(state, val) {
      state.input = val;
    },
    mutReset(state) {
      state.output = {};
      state.showResults = false;
    },
    mutResponse(state, data) {
      state.output = data;
      state.showResults = true;
    },
    mutError(state, val) {
      state.error = val;
    },
    mutFocus(state, payload) {
      state.focus = payload;
    },
    mutUnfocus(state) {
      state.focus = {knot: null, functor: null}
    },
    mutCustomName(state, pl) {
      Vue.set(state.output.functors[pl.id],  'cname', pl.val);  // actual custom name
      Vue.set(state.output.functors[pl.id], 'tcname', pl.val);  // temporary custom name
      state.errorsCustomName = [];
    },
    mutTempCustomName(state, pl) {
      Vue.set(state.output.functors[pl.id], 'tcname', pl.val);
    },
    mutErrorsCustomName(state, val) {
      state.errorsCustomName = val;
    },
    mutShowCustomNames(state, val) {
      state.showCustomNames = val
    },
    mutErrorsCustomName(state, val) {
      state.errorsCustomName = val
    },
    mutShowTermTables(state, val) {
      state.showTermTables = val
    },
  },
  actions: {
    actPost(context, input) {
      let url = 'http://127.0.0.1:8000/trace/';
      axios.post(url, {'text': input})
        .then(response => {
          if ('error' in response.data) {
            context.commit('mutError', response.data.error);
          } else {
            context.commit('mutError', null);
            context.commit('mutResponse', response.data);
          }
        })
        .catch(e => {
          console.log(e)
        });
    },
    actCustomName(context, pl) {
      let checker = context.getters.checkCustomName;
      let target_id = pl.id, target_val = pl.val.replace(' ', '_'), new_pl = {id: target_id, val: target_val};
      let check = checker(target_id, target_val);
      if (check.legal) {
        context.commit('mutCustomName', new_pl);
      } else {
        context.commit('mutErrorsCustomName', check.affected);
        context.dispatch('actTempCustomName', new_pl);
      }
    },
    actTempCustomName(context, pl) {
      let checker = context.getters.checkCustomName;
      let target_id = pl.id, functors = context.state.output.functors;
      context.commit('mutTempCustomName', pl);  // illegal temp val, supposed to be changed quickly by the user

      function correctIfNotFixed() {
        let current_temp_val = functors[target_id].tcname;
        let check = checker(target_id, current_temp_val);
        if (!check.legal) {
          let current_val = functors[target_id].cname;
          context.commit('mutCustomName', {id: target_id, val: current_val});  // replace temp val by last legal val
        }
      }

      setTimeout(correctIfNotFixed, 1000);
    }
  },
  getters: {
    checkCustomName: state => (target_id, target_val) => {
      if (target_val == '') {
        return {legal: false, affected: [target_id]}
      }
      let functors = state.output.functors;
      let target_ary = functors[target_id].ary;
      for (let [test_id, test_functor] of functors.entries()) {
        let test_val = test_functor.cname, test_ary = test_functor.ary;
        if (target_val == test_val && target_ary == test_ary && target_id != test_id) {
          return {legal: false, affected: [target_id, test_id]}
        }
      }
      return {legal: true, affected: []}
    }
  }
});
