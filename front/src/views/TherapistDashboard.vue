<template>
    <v-content>
        <v-app-bar color="primary" dark>
            <v-icon left>mdi-leaf</v-icon>
            <v-toolbar-title>{{ $appName }}</v-toolbar-title>
            <v-spacer/>
            <v-toolbar-items>
                <v-btn to="/logout" text><v-icon left>mdi-logout</v-icon>Logout</v-btn>
            </v-toolbar-items>
        </v-app-bar>
        <p class="ml-3 my-5 display-1 accent--text">Dashboard</p>
        <v-sheet tile color="white" width="100vw">
            <v-list two-line>
                <patient v-for="(client, index) in clients" v-bind:patient="client" v-bind:key="index" />
            </v-list>
        </v-sheet>
        <v-dialog v-model="dialog" width="500">
            <v-card>
                <v-card-title class="headline grey lighten-2" primary-title>Privacy Policy</v-card-title>
                <v-card-text>

                </v-card-text>
                <v-divider/>

                <v-card-actions>
                    <v-spacer/>
                    <v-btn color="primary" text @click="dialog = false">I accept</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-content>
</template>

<script>
    import Vue from 'vue';
    import axios from 'axios';
    import PatientInfo from "./PatientInfo";

    export default Vue.extend({
        name: 'therapist-dashboard',
        components: {
            'patient': PatientInfo
        },
        data: () => ({
            clients: [],
            dialog: false
        }),
        mounted() {
            let t = this;
            axios.get('/clients').then(res => {
                console.log(res.data);
                t.clients = res.data.clients.map(e => {
                    return {
                        name: e.clientName,
                        id: e.clientID
                    }
                });
            }).catch(e => {
                console.log(e);
            })
        }
    });
</script>

<style>

</style>
