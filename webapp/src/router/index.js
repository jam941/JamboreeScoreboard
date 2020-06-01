import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ScoreList from "../views/ScoreList";
import ScoreSubmit from "../views/ScoreSubmit";
import BarcodeRead from "../views/BarcodeRead";
import Login from "../views/Login"
import store from "../store"

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Scores',
        component: ScoreList
    },

    {
        path: '/barcode',
        name: 'Score Submit With barcode',
        component: BarcodeRead,
        meta:{
            requireAuth: true
        }
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})
// region Vue Navigation Guards
// https://router.vuejs.org/guide/advanced/navigation-guards.html

/**
 * Navigation Guard function to prevent unauthenticated users from
 * accessing pages which require auth.
 *
 * see https://scotch.io/tutorials/vue-authentication-and-route-handling-using-vue-router
 */
function checkAuthenticated(to, from, next) {
    // to.matched returns an array of the route and any child routes
    // Array.some(element => true) returns true if any element in the array resolves to true
    if (to.matched.some(route => route.meta.requireAuth)) {
        // This page requires authentication
        if (store.getters.isLoggedIn) {
            // User is logged in
            return next();
        } else {
            // User is not logged in, redirect to the home page
            return next('/');
        }
    } else {
        return next();
    }
}

router.beforeEach(checkAuthenticated)
export default router
