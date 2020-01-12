<template>
    <v-dialog fullscreen transition="dialog-bottom-transition" v-model="dialog">
        <template v-slot:activator="{ on }">
            <v-card @click="open">
                <v-card-title class="">Session on {{ date }}</v-card-title>
                <v-card-text>
                    <p class="ma-0 pa-0">
                        Exchanged {{session.messageCount}} messages total
                    </p>
                    <p class="ma-0 pa-0">
                        Average happiness of {{ session.average }}
                    </p>
                    <p class="ma-0 pa-0">
                        Started at {{ startTime }}
                    </p>
                    <p class="ma-0 pa-0">
                        Ended at {{ endTime }}
                    </p>
                </v-card-text>
            </v-card>
        </template>
        <v-card>
            <v-app-bar flat>
                <v-btn @click="close" color="primary" icon>
                    <v-icon>mdi-close</v-icon>
                </v-btn>
                <v-toolbar-title>
                    {{ date }}
                </v-toolbar-title>
            </v-app-bar>
            <v-sheet color="transparent">
                <v-card elevation="0" class="pa-4" v-for="(message, index) in session.conversation" v-bind:key="index">
                    <v-divider class="mb-2"/>
                    <span class="mr-4">
                        {{message.message}}
                    </span>
                    <v-btn :color="(message.sentiment === 1 ? '#236932' : '#ff0000')" fab x-small absolute right elevation="0"/>
                </v-card>
            </v-sheet>
        </v-card>
    </v-dialog>
</template>

<script>
    import Vue from 'vue';
    import moment from 'moment';

    export default Vue.extend({
        name: 'sessions',
        props: ['session'],
        data: () => ({
            dialog: false,
            loading: true
        }),
        mounted() {
            console.log('s', this.session)
        },
        computed: {
            date() {
                return moment(this.session.endTime).format("MMMM Do YYYY")
            },
            startTime() {
                return moment(this.session.startTime).format("HH:mm:ss a")
            },
            endTime() {
                return moment(this.session.endTime).format("HH:mm:ss a")
            }
        },
        methods: {
            open() {
                let t = this;
                t.dialog = true;
            },
            close() {
                this.dialog = false;
            },
        }
    });
</script>

<style>

</style>
