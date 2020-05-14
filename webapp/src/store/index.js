import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios"

Vue.use(Vuex)
const store = new Vuex.Store({
    state: {
        submissionQueue: [],
    },
    mutations: {
        addScore(state, score) {
            // mutate state
            state.submissionQueue.push(score);
        },
        flushQueue(state) {
            let queue = state.submissionQueue;
            let item = queue.pop();
            while (item !== undefined) {

                axios.post("http://127.0.0.1:8000/scores/", item).catch(error => {
                    console.error(error);
                    //TODO implement resend after 30 seconds
                })
                item = queue.pop();
            }
        }

    },
    actions: {},
    modules: {}
})
store.subscribe((mutation, state) => {

    if (mutation.type === 'addScore') {
        store.commit('flushQueue')
    }
})


export default store;
