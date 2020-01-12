import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

/**
 * 1. Landing Page
 * 2. Login / Register
 * 3. logged in user home -> chat interface
 *
 */

const routes = [
  {
    path: '/',
    name: 'landing',
    component: () => import('../views/Landing.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/logout',
    name: 'logout',
    component: () => import('../views/Logout.vue')
  },
  {
    path: '/new-session',
    name: 'new-session',
    component: () => import('../views/NewSession.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/home/patient',
    name: 'chat',
    component: () => import('../views/Chat.vue')
  },
  {
    path: '/home/therapist',
    name: 'home',
    component: () => import('../views/Home.vue')
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
