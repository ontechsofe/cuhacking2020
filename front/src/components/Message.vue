<template>
    <v-dialog v-model="dialog" width="500">
        <template v-slot:activator="{ on }">
            <v-sheet class="mb-5" width="100vw" tile color="transparent">
                <div v-on="on" v-if="message.type === 0" class="message-left">
                    <v-sheet dark color="accent" class="mx-4 pa-2" width="50vw" elevation="2">{{ message.txt }}</v-sheet>
                </div>
                <div v-on="on" v-else-if="message.type === 1" class="message-right">
                    <v-sheet dark color="primary" class="mx-4 pa-2" width="50vw" elevation="2">{{ message.txt }}</v-sheet>
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
<script lang="ts">
    import Vue from 'vue';

    export default Vue.extend({
        props: ['message'],
        name: 'home',
        data: () => ({
            dialog: false
        }),
        mounted() {
            console.log(this.message)
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
