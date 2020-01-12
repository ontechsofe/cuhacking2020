<template>
    <v-content>
        <v-app-bar fixed color="primary" dark>
            <v-icon left>mdi-leaf</v-icon>
            <v-toolbar-title>Melanie</v-toolbar-title>
            <v-spacer/>
            <v-toolbar-items>
                <v-btn to="/phone" text>
                    <v-icon left>mdi-phone</v-icon>
                    Help
                </v-btn>
                <v-btn to="/logout" icon>
                    <v-icon>mdi-logout</v-icon>
                </v-btn>
            </v-toolbar-items>
        </v-app-bar>
        <v-divider class="my-10"/>
        <div class="message-container">
            <message v-for="(message, index) in messageData" v-bind:key="index" v-bind:message="message"/>
        </div>
        <div id="bottom"></div>
        <v-footer fixed elevation="5">
            <v-text-field :disabled="sending" v-model="message" placeholder="Type a message here..."/>
            <v-btn :loading="sending" @click="sendMessage" icon color="accent">
                <v-icon>mdi-send</v-icon>
            </v-btn>
        </v-footer>
    </v-content>
</template>
<script>
    import Vue from 'vue';
    import storage from 'localStorage';
    import axios from "axios";

    export default Vue.extend({
        name: 'home',
        components: {
            message: () => import('../components/Message.vue')
        },
        data: () => ({
            message: '',
            messages: [],
            sending: false,
            bottomed: true,
            chatEl: undefined
        }),
        computed: {
            messageData() {
                return this.messages;
            }
        },
        mounted() {
            let t = this;
            t.getMessages();
        },
        methods: {
            scrollToBottom() {
                document.getElementById('bottom').scrollIntoView();
            },
            getMessages() {
                let t = this;
                axios.post('/messages', {
                    sessionID: storage.getItem('session')
                }).then(res => {
                    console.log('get', res.data);
                    const clientID = storage.getItem('token');
                    t.messages = [...res.data.messages].map(e => {
                        return {
                            message: e.message,
                            type: clientID === e.recipientID ? 0 : 1,
                            time: e.time
                        }
                    });
                    t.scrollToBottom();
                }).catch(e => {
                    console.log(e);
                })
            },
            sendMessage() {
                let t = this;
                if (t.message === '') {
                    return;
                }
                t.sending = true;
                axios.post('/send', {
                    message: t.message,
                    clientID: storage.getItem('token'),
                    sessionID: storage.getItem('session')
                }).then(res => {
                    t.message = '';
                    console.log('send', res.data);
                    t.sending = false;
                    t.getMessages();
                }).catch(e => {
                    console.log(e);
                    t.sending = false;
                });
            }
        }
    });
</script>
<style>
    .message-container {
        width: 100vw;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
        margin-bottom: 60px;
    }
</style>
