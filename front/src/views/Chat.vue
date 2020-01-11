<template>
    <v-content>
        <v-system-bar color="secondary">

        </v-system-bar>
        <v-app-bar fixed color="primary" dark>
            <v-icon left>mdi-brain</v-icon>
            <v-toolbar-title>APP NAME</v-toolbar-title>
            <v-spacer/>
            <v-toolbar-items>
                <v-btn text>ACTION</v-btn>
            </v-toolbar-items>
        </v-app-bar>
        <div class="message-container">
            <message v-for="(message, index) in messageData" v-bind:key="index" v-bind:message="message"/>
        </div>
        <v-footer fixed>
            <v-text-field placeholder="Type a message here..."/>
            <v-btn icon color="accent">
                <v-icon>mdi-send</v-icon>
            </v-btn>
        </v-footer>
    </v-content>
</template>
<script lang="ts">
    import Vue from 'vue';

    export default Vue.extend({
        name: 'home',
        components: {
            message: () => import('../components/Message.vue')
        },
        data: () => ({
            messageData: [
                {
                    type: 0,
                    txt: "HEY FRIEND",
                    from: {},
                    to: {},
                    time: 0,
                },
                {
                    type: 1,
                    txt: "hey twitter world",
                    from: {},
                    to: {},
                    time: 0,
                },
                {
                    type: 0,
                    txt: "how are you",
                    from: {},
                    to: {},
                    time: 0,
                },
                {
                    type: 1,
                    txt: "good n' u?",
                    from: {},
                    to: {},
                    time: 0,
                },
                {
                    type: 0,
                    txt: "good n' u?",
                    from: {},
                    to: {},
                    time: 0,
                },
                {
                    type: 0,
                    txt: "i am very good, this is a very long message to see how it handles word wrap",
                    from: {},
                    to: {},
                    time: 0,
                },
                {
                    type: 1,
                    txt: "wow, that is very cool! it looks like it can handle a very long message and not overflow the container",
                    from: {},
                    to: {},
                    time: 0,
                },
            ]
        }),
    });
</script>
<style>
    .message-container {
        width: 100vw;
        height: 85%;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
    }
</style>
