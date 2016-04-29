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
             :options="mapOptions"
             @g-idle="refreshMap">
            <marker
                v-for="m in markers"
                :position.sync="m.position"
                :icon.sync="m.icon"
                :clickable.sync="markersOptions.clickable"
                :draggable.sync="markersOptions.draggable"
                :title.sync="m.title">
            </marker>
        </map>
    </div>
</template>

<script>

    import { Promise } from 'es6-promise';
    import { API_ROOT } from '../config.js';
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
             * Then, refresh map
             */
            search: function() {
                let vm = this;
                this.geocode(this.query).then(function() {
                    vm.refreshMap();
                }, function(error) {          
                    console.warn(error);
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
            }, 

            /**
             * Refresh map : call API for actual bounds
             */
            refreshMap: function() {
                var vm = this;
                
                // Search params : map bounds
                var params = {
                    lat_min: vm.mapBounds.getSouthWest().lat(), 
                    lat_max: vm.mapBounds.getNorthEast().lat(),
                    lg_min: vm.mapBounds.getSouthWest().lng(), 
                    lg_max: vm.mapBounds.getNorthEast().lng(), 
                };
                
                vm.$http.get(API_ROOT + 'stations/', params).then(function(stations) {
                    vm.markers = [];
                    for(var d of stations.data) {
                        vm.markers.push({
                            title: d.name, 
                            position: {lat: d.latitude, lng: d.longitude}, 
                            // icon: {url: 'http://www.hotel-albert1.com/medias/2013/07/picto-gare.png'}
                        });
                    };

                }, function(error) {
                    console.warn(error);
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