import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ScoreList from "../views/ScoreList";
import ScoreSubmit from "../views/ScoreSubmit";
import BarcodeRead from "../views/BarcodeRead";
import Login from "../views/Login"

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
        component: BarcodeRead
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

export default router
