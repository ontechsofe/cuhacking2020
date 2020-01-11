<template>
    <v-content>
        <v-system-bar color="secondary">

        </v-system-bar>
        <v-app-bar fixed color="primary" dark>
            <v-icon left>mdi-brain</v-icon>
            <v-toolbar-title>APP NAME</v-toolbar-title>
            <v-spacer/>
            <v-toolbar-items>
                <v-btn to="/chat" text>ACTION</v-btn>
            </v-toolbar-items>
        </v-app-bar>
    </v-content>
</template>

<script lang="ts">
    import Vue from 'vue';

    export default Vue.extend({
        name: 'home',
        data: () => ({
        }),
    });
</script>

<style>

</style>
