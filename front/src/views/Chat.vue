<template>
    <v-content>
        <v-app-bar fixed color="primary" dark>
            <v-icon left>mdi-brain</v-icon>
            <v-toolbar-title>{{ $appName }}</v-toolbar-title>
            <v-spacer/>
            <v-toolbar-items>
                <v-btn to="/logout" text>
                    <v-icon left>mdi-logout</v-icon>
                    Logout
                </v-btn>
            </v-toolbar-items>
        </v-app-bar>
        <v-divider class="my-10" />
        <div class="message-container pt-10" v-chat-scroll>
            <message v-for="(message, index) in messageData" v-bind:key="index" v-bind:message="message"/>
        </div>
        <v-divider class="my-10" />
        <v-footer fixed>
            <v-text-field placeholder="Type a message here..."/>
            <v-btn icon color="accent">
                <v-icon>mdi-send</v-icon>
            </v-btn>
        </v-footer>
    </v-content>
</template>
<script>
    import Vue from 'vue';
    import storage from 'localStorage';

    export default Vue.extend({
        name: 'home',
        components: {
            message: () => import('../components/Message.vue')
        },
        computed: {
            messageData() {
                return [
                    {
                        type: 0,
                        txt: "HEY FRIEND",
                        from: {},
                        to: {},
                        time: 0,
                    },
                    {
                        type: 1,
                        txt: "HEY FRIEND",
                        from: {},
                        to: {},
                        time: new Date().valueOf(),
                    }
                ]
            }
        },
        data: () => ({
        }),
    });
</script>
<style>
    .message-container {
        width: 100vw;
        height: 90%;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
    }
</style>
