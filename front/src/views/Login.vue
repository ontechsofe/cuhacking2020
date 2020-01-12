<template>
    <v-content>
        <v-img class="blur" height="100vh" src="../assets/desk.jpg"/>
        <v-overlay absolute :value="true">
            <v-container class="fill-height" fluid>
                <v-container>
                    <v-row align="center" justify="center">
                        <v-col cols="12" sm="8" md="4">
                            <v-card width="350" class="" tile elevation="5" light>
                                <div class="logo pa-6">
                                    <v-icon class="my-5" size="100" color="accent">mdi-brain</v-icon>
                                </div>
                                <v-toolbar flat color="primary" dark>
                                    <v-toolbar-title>Login</v-toolbar-title>
                                </v-toolbar>
                                <v-sheet flat color="transparent" width="100%" class="pa-4">
                                    <v-form>
                                        <v-text-field v-model="username" outlined placeholder="" label="Username"/>
                                        <v-text-field v-model="password" outlined placeholder="" label="Password"
                                                      type="password"/>
                                        <v-btn @click="login" block tile x-large color="primary">Login</v-btn>
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
<script>
    import Vue from 'vue';
    import axios from 'axios';
    import storage from 'localStorage';

    export default Vue.extend({
        name: 'login',
        data: () => ({
            username: '',
            password: ''
        }),
        methods: {
            login() {
                axios.post('/auth', {
                    username: this.username,
                    password: this.password
                }).then(res => {
                    console.log(res);
                    storage.clear();
                    storage.setItem('token', 'tokencodehere');
                    // response might also include the type of user to indicate where to redirect
                    /**
                     * this.$router.push('/home/patient')
                     * this.$router.push('/home/therapist')
                     */
                }).catch(e => console.log(e));
                this.$router.push('/home/patient')
            }
        }
    })
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
