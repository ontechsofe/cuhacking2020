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
                                    <v-icon class="my-5" size="100" color="accent">mdi-leaf</v-icon>
                                </div>
                                <p class="display-2 text-center primary--text">Register</p>
                                <v-sheet flat color="transparent" width="100%" class="pa-4">
                                    <v-form>
                                        <v-text-field v-model="name" autofocus outlined placeholder="" label="Name"/>
                                        <v-text-field v-model="username" outlined placeholder="" label="Username"/>
                                        <v-text-field v-model="password" outlined placeholder="" label="Password" type="password"/>
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
<script>
    import Vue from 'vue';
    import axios from 'axios';
    import sha256 from 'sha256';

    export default Vue.extend({
        name: 'register',
        data: () => ({
            name: '',
            username: '',
            password: ''
        }),
        methods: {
            hash(data) {
                return sha256(data);
            },
            join() {
                let t = this;
                console.log(this.username, this.password);
                axios.post('/register', {
                    name: this.name,
                    username: this.username,
                    password: this.hash(this.password)
                }).then(res => {
                    console.log(res);
                    if (res.data.success) {
                        t.$router.push('/login');
                    } else {
                        // show some error message
                    }
                }).catch(e => console.log(e));
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
