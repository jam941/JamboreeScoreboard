<template>
    <div>
        <div>
        <label>
            Submitting User
            <input type = "text" v-model = "form.submit_user">
        </label>
        </div>

        <div>
            <label>
                Scout

                <select name = "scout" type="text" v-model="form.scout" @change="enforcePatrol()" >
                    <option v-for ="scout in scouts" v-bind:value="scout"> {{scout.name}} </option>
                </select>

            </label>
        </div>

        <div>
            <label>
                Patrol
                <select name="patrol" type="text" v-model="form.patrol" id = "patrol" @change="enforceScout()" >
                    <option v-for ="patrol in patrols" v-bind:value="patrol"> {{patrol.name}} </option>
                </select>
            </label>
        </div>


        <div>
        comment
        <label>
            Good turn
            <input type="radio" name="comment" value="good turn" v-model="form.comment"/>
        </label>
        <label>
            Completed activity
            <input type="radio" name="comment" value="completed activity" v-model="form.comment"/>
        </label>
            </div>

        <div>
        score

        <label>
            1
            <input type="radio" name="score" value="1" v-model="form.score"/>
        </label>
        <label>
            2
            <input type="radio" name="score" value="2" v-model="form.score"/>
        </label>
        <label>
            3
            <input type="radio" name="score" value="3" v-model="form.score"/>
        </label>
        </div>
        <button type="button" v-on:click="submit">
            submit
        </button>

    </div>
</template>

<script>
    import axios from "axios"

    export default {

        name: "ScoreSubmit",
        data() {
            return {
                "form": {
                    "score": null,
                    "submit_user": "",
                    "comment": "",
                    "scout": "",
                    "patrol": ""
                },
                scouts: [],
                patrols: []

            }
        },
        created() {
            this.updateScouts();
        },
        methods: {
            updateScouts() {
                axios.get("http://127.0.0.1:8000/scouts/")
                    .then((response) => {
                        this.scouts = response.data;
                        this.scouts.push({ name:null, url:null});
                    })
                axios.get("http://127.0.0.1:8000/patrols/")
                    .then((response) => {
                        this.patrols = response.data;
                        this.patrols.push({ name:null, url:null});
                    })
            },

            submit() {
                this.form.scout = this.form.scout.url;
                this.form.patrol = this.form.patrol.url;
                this.$store.commit("addScore",this.form);

            },

            enforcePatrol(){

               this.form.patrol = { name:null, url:null}

            },

            enforceScout(){

            }

        },
        watch:{
            form(){

            }
        }


    }

</script>

<style scoped>

</style>