import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import vuetify from './plugins/vuetify';
import axios from 'axios';

Vue.config.productionTip = false;

const PROD = false;

axios.defaults.baseURL = (PROD ? '' : 'http://localhost:5555/');

new Vue({
    router,
    // @ts-ignore
    vuetify,
    render: h => h(App)
}).$mount('#app');
