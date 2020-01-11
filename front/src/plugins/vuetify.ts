import Vue from 'vue';
// @ts-ignore
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: '#00838F',
                secondary: '#006064',
                accent: '#E65100'
            }
        }
    }
});
