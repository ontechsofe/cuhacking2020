<template>
    <v-content>
        <v-img class="blur" height="100vh" src="../assets/desk.jpg"/>
        <v-overlay :absolute="absolute" :value="overlay">
            <v-container class="fill-height" fluid>
                <v-container>
                    <v-row align="center" justify="center">
                        <v-col cols="12" sm="8" md="4">
                            <v-card width="350" class="pa-7" tile elevation="5" light>
                                <div class="logo mb-6">
                                    <v-icon class="my-5" size="100" color="accent">mdi-brain</v-icon>
                                    <div>
                                        <span class="font-weight-bold display-1 primary--text">THING</span>
                                        <span class="display-1 primary--text">THING</span>
                                    </div>
                                </div>
                                <p>
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur ligula
                                    auctor dignissim tristique. Praesent porttitor gravida magna, interdum egestas nisi
                                    posuere vitae. Proin pretium eu lorem at efficitur. Integer iaculis lacus non
                                    rhoncus molestie.
                                </p>
                                <v-btn to="/register" class="my-7" block tile color="primary" x-large>Get Started</v-btn>
                                <v-btn block tile text color="secondary">Login</v-btn>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>
            </v-container>
        </v-overlay>
    </v-content>
</template>
<script lang="ts">
    import Vue from 'vue';

    export default Vue.extend({
        name: 'landing',

        data: () => ({}),
    });
</script>
<style>
    .logo {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .blur {
        filter: blur(4px);
    }
</style>
