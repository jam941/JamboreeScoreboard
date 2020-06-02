<template>
  <div id="app">
    <div class="BS" v-if="$store.state.name">
                Logged in as: {{$store.state.name}}
    </div>
    <div id="nav">
      <router-link to="/">Scoreboard</router-link>
      |
      <router-link to="/about">About</router-link>
      
      <template v-if="canAccessRoute('/barcode')">
       |
        <router-link to="/barcode">Submit Scores</router-link>

      </template>
      <template v-if="!$store.getters.isLoggedIn">
        |
        <router-link to="/login">Login</router-link>
      </template>

    </div>
    <router-view/>
  </div>
</template>

<script>
    import {canAccessRoute} from "./router";

    export default {

        methods: {
            canAccessRoute: canAccessRoute
        }


    }


</script>

<style lang="scss">
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #nav {
    padding: 30px;

    a {
      font-weight: bold;
      color: #2c3e50;

      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
  .BS {
    padding-top: .25em;
    padding-right:.5em;
    font-size: .8rem;
    text-align: right;
    font-style: italic;
    color: #2c3e50;
  }
</style>
