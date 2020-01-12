<template>
    <v-content>
        <v-img class="blur" height="100vh" src="../assets/desk.jpg"/>
        <v-overlay absolute :value="true">
            <v-container class="fill-height" fluid>
                <v-container>
                    <v-row align="center" justify="center">
                        <v-col cols="12" sm="8" md="4">
                            <v-progress-circular :size="90" :width="8" color="accent" indeterminate/>
                        </v-col>
                    </v-row>
                </v-container>
            </v-container>
        </v-overlay>
    </v-content>
</template>
<script>
    import Vue from 'vue';
    import storage from 'localStorage';
    import axios from 'axios';

    export default Vue.extend({
        name: 'new-session',
        data: () => ({
        }),
        mounted() {
            let t = this;
            axios.post('/start', {
                clientID: storage.getItem('token')
            }).then(res => {
                if (res.data.success && res.data.sessionID) {
                    storage.setItem('session', res.data.sessionID);
                    t.$router.push('/home/patient');
                } else {
                    t.$router.push('/login');
                }
            }).catch(e => {
                console.log(e);
                t.$router.push('/login');
            })
        }
    });
</script>
<style>
    .blur {
        filter: blur(4px);
    }
</style>
