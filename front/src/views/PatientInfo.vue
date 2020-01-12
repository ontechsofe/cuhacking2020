<template>
    <v-dialog fullscreen transition="dialog-bottom-transition" v-model="dialog">
        <template v-slot:activator="{ on }">
            <v-list-item @click="open">
                <v-list-item-avatar tile>
                    <v-icon>mdi-account</v-icon>
                </v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title class="text-uppercase">{{patient.name}}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </template>
        <v-card>
            <v-overlay absolute :opacity="0.5" :value="loading">
                <v-progress-circular :size="90" :width="8" color="primary" indeterminate/>
            </v-overlay>
            <v-app-bar flat>
                <v-btn @click="close" color="primary" icon>
                    <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title class="text-uppercase">{{ patient.name }} - Client Profile</v-toolbar-title>
                <v-spacer/>
            </v-app-bar>
            <v-sheet>
                <session v-for="(session, index) in sessions" v-bind:session="session" v-bind:key="index"/>
            </v-sheet>
        </v-card>
    </v-dialog>
</template>

<script>
    import Vue from 'vue';
    import axios from 'axios'
    import Sessions from "./Sessions";

    export default Vue.extend({
        name: 'patient-info',
        props: ['patient'],
        components: {
            'session': Sessions
        },
        data: () => ({
            dialog: false,
            patientData: null,
            loading: true,
            sessions: []
        }),
        methods: {
            open: function () {
                let t = this;
                t.dialog = true;
                axios.post('/client/messages', {
                    clientID: this.patient.id
                }).then(res => {
                    t.loading = false;
                    let s = res.data.sessionIDs.map(el => {
                        let filterSessions = res.data.messages.filter(m => m.sessionID === el);
                        let avgSent = Math.floor(filterSessions
                            .map(e => e.sentiment)
                            .reduce((a, b) => a + b) / filterSessions.length * 100
                        ) / 100;
                        return {
                            id: el,
                            conversation: filterSessions,
                            startTime: Math.min(...filterSessions.map(e => e.time)),
                            endTime: Math.max(...filterSessions.map(e => e.time)),
                            messageCount: filterSessions.length,
                            average: avgSent
                        }
                    });
                    t.sessions = s;
                }).catch(err => {
                    console.log(err);
                    t.dialog = false;
                });
            },
            close() {
                this.dialog = false;
            },
        }
    });
</script>

<style>

</style>
