import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'

import store from './store'
import axios from "axios"
Vue.config.productionTip = false;
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
