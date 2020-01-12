<template>
    <v-dialog v-model="dialog" width="500">
        <template v-slot:activator="{ on }">
            <v-sheet class="mb-5 text-center" width="100vw" tile color="transparent">
                <p>{{ time }}</p>
                <div v-if="message.type === 0" class="message-left text-left">
                    <v-sheet v-on="on" dark color="accent" class="mx-4 pa-2" max-width="50vw" elevation="2">{{ message.txt }}</v-sheet>
                </div>
                <div v-else-if="message.type === 1" class="message-right text-right">
                    <v-sheet v-on="on" dark color="primary" class="mx-4 pa-2" max-width="50vw" elevation="2">{{ message.txt }}</v-sheet>
                </div>
            </v-sheet>
        </template>
        <v-card>
            <v-card-title class="headline grey lighten-2" primary-title>Message Actions</v-card-title>
            <v-card-text>
                This can be full of things that will allow modifying the message
                <p class="px-5">
                    {{ message.to }}
                </p>
                <p class="px-5">
                    {{ message.from }}
                </p>
                <p class="px-5">
                    {{ message.txt }}
                </p>
            </v-card-text>
            <v-divider/>
            <v-card-actions>
                <v-spacer/>
                <v-btn color="primary" text @click="dialog = false">
                    okay
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

</template>
<script>
    import Vue from 'vue';
    import moment from 'moment';

    export default Vue.extend({
        props: ['message'],
        name: 'home',
        data: () => ({
            dialog: false
        }),
        computed: {
            time() {
                return moment(this.message.time).format("h:mm:ss a")
            }
        },
        mounted() {
            let x = setInterval(() => {
                document.body.scrollTop = document.body.offsetHeight;
            }, 100);
        }
    });
</script>
<style>
    .message-left {

    }

    .message-right {
        margin-left: 42vw;
    }
</style>
