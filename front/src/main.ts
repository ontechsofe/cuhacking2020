import Vue from 'vue'
import store from './store'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import vuetify from './plugins/vuetify';
import axios from 'axios';
// @ts-ignore

Vue.config.productionTip = false;

const PROD = false;

axios.defaults.baseURL = (PROD ? '' : 'http://9158a429.ngrok.io/');

Vue.prototype.$appName = 'Thoughtful Therapy';

new Vue({
    router,
    // @ts-ignore
    vuetify,
    store,
    render: h => h(App)
}).$mount('#app');
