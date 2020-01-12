<template>
    <v-content>
        <v-img class="blur" height="100vh" src="../assets/desk.jpg"/>
        <v-overlay absolute :value="true">
            <v-container class="fill-height" fluid>
                <v-container>
                    <v-row align="center" justify="center">
                        <v-col cols="12" sm="8" md="4">
                            <v-progress-circular :size="90" :width="8" color="accent" indeterminate/>
                        </v-col>
                    </v-row>
                </v-container>
            </v-container>
        </v-overlay>
    </v-content>
</template>
<script>
    import Vue from 'vue';
    import storage from 'localStorage';

    export default Vue.extend({
        name: 'login',
        data: () => ({
            username: '',
            password: ''
        }),
        mounted() {
            setTimeout(() => {
                // clear the session token here
                storage.clear();
                this.$router.push('/');
            }, 1000);
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
