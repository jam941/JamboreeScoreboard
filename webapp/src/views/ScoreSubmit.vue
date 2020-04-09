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

            <select type="text" v-model="form.scout" >
                <option v-for ="scout in scouts" v-bind:value="scout.url"> {{scout.name}} </option>
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
                    "patrol": null
                },
                scouts: [],

            }
        },
        created() {
            this.updateScouts();
        },
        methods: {
            updateScouts() {
                axios.get("http://127.0.0.1:8000/scouts/")
                    .then((response) => {
                        this.scouts = response.data
                    })
            },
            submit() {
                //this.form.scout = this.form.scout.url;
                axios.post("http://127.0.0.1:8000/scores/",this.form)
            }
        }

    }

</script>

<style scoped>

</style>