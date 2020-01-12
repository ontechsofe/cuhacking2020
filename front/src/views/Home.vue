<template>
    <v-content>
        <v-system-bar color="secondary"/>
        <v-app-bar fixed color="primary" dark>
            <v-icon left>mdi-brain</v-icon>
            <v-toolbar-title>{{ $appName }}</v-toolbar-title>
            <v-spacer/>
            <v-toolbar-items>
                <v-btn to="/logout" text><v-icon left>mdi-logout</v-icon>Logout</v-btn>
            </v-toolbar-items>
        </v-app-bar>
    </v-content>
</template>

<script>
    import Vue from 'vue';

    export default Vue.extend({
        name: 'home',
        data: () => ({

        }),
    });
</script>

<style>

</style>
