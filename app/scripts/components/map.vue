<template>
    <div class="search">
        <form v-on:submit.prevent="search()">
            <input placeholder="Search..." v-model="query" />
            <input type="submit" />
        </form>
    </div>
    <div class="map">
        <map :center.sync="center"
             :zoom.sync="zoom"
             :bounds.sync="mapBounds"
             :options="mapOptions">
            <marker
                v-for="m in markers"
                :position.sync="m.position"
                :clickable.sync="markersOptions.clickable"
                :draggable.sync="markersOptions.draggable"
                :title.sync="m.title"
            </marker>
        </map>
    </div>
</template>

<script>

    import { Promise } from 'es6-promise';    
    const VueGoogleMap = require('vue-google-maps');

    export default{
        name: 'station-map', 
        data() {
            return {
                center: {lat: 48.856614, lng: 2.3522219},
                address: null,
                zoom: 14,
                markers: [],
                mapOptions: {
                    mapTypeControl: false,
                    scaleControl: false,
                    zoomControl: false,
                },
                mapBounds: {},
                markersOptions: {
                    draggable: false,
                    clickable: true
                },
                query: ""
            }
        },
        created() {
            VueGoogleMap.load(this.key);
        },
        methods: {
            
            /**
             * Search stations from given address
             * First, geocode the address to get coordinates
             * Then, call API 
             */
            search: function() {
                let vm = this;
                this.geocode(this.query).then(function() {
                    
                    // Search
                    vm.$http.get('http://demo2503145.mockable.io/stations').then(function(stations) {
                        for(var d of stations.data.data) {
                            vm.markers.push({
                                title: d.name, 
                                postion: {lat: d.latitude, lg: d.longitude}
                            });
                        };

                    }, function(error) {
                        console.warn(error);
                    });

                }, function(error) {
                    
                    // Error
                    // @todo

                });
            }, 

            /**
             * Find place coordinates from address, using GMaps geocode API
             * @param string address
             * @return Promise
             */
            geocode: function(address) {
                let vm = this;
                return new Promise(function(resolve, reject) {
                    vm.$http.get('https://maps.googleapis.com/maps/api/geocode/json', {
                        address: address,
                        key: vm.key
                    }).then(function (result) {
                        if (result.data.status === 'OK') {
                            vm.zoom = 13;
                            vm.center = result.data.results[0].geometry.location;
                            resolve(result);
                        }
                        reject;
                    }, function (response) {
                        reject;
                    });
                });
            }


        },
        components: {
            'map': VueGoogleMap.Map,
            'marker': VueGoogleMap.Marker
        },
        props: ['key']
    }


</script>