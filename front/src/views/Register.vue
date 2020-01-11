<template>
    <v-content>
        <v-img class="blur" height="100vh" src="../assets/desk.jpg"/>
        <v-overlay :absolute="absolute" :value="overlay">
            <v-container class="fill-height" fluid>
                <v-container>
                    <v-row align="center" justify="center">
                        <v-col cols="12" sm="8" md="4">
                            <v-card width="350" class="" tile elevation="5" light>
                                <div class="logo pa-6">
                                    <v-icon class="my-5" size="100" color="accent">mdi-brain</v-icon>
                                </div>
                                <v-toolbar flat color="secondary" dark>
                                    <v-toolbar-title>Register</v-toolbar-title>
                                </v-toolbar>
                                <v-sheet flat color="transparent" width="100%" class="pa-4">
                                    <v-form>
                                        <v-text-field autofocus outlined prepend-inner-icon="mdi-account"
                                                      placeholder="" label="Username" />
                                        <v-btn @click="join" block tile x-large color="primary">Join</v-btn>
                                    </v-form>
                                </v-sheet>
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
        name: 'register',
        data: () => ({}),
        methods: {
            join() {
                this.$router.push('/home')
            }
        }
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
