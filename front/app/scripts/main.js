var Vue = require('vue');
Vue.use(require('vue-resource'));

// Import Vue components
import MapComponent from './components/map.vue';

// Instanciate vue app
new Vue({
	el: '#app',
	components: {
        'station-map': MapComponent
    }
});