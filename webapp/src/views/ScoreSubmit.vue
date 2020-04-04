<template>
    <div>
        <label>
            submit user
            <input type="text" v-model="form.submit_user"/>
            {{form.submit_user}}

        </label>
        <label>
            comment
            <input type="text" v-model="form.comment"/>
        </label>
        <label>
            score
            <input type="text" v-model="form.score"/>
        </label>
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
                    "scout": "http://127.0.0.1:8000/scouts/1/",
                    "patrol": null
                },

            }
        },
        created() {

        },
        methods: {
            updateScouts() {
                axios.get("http://127.0.0.1:8000/scouts/")
                    .then((response) => {
                        this.scouts = response.data
                    })
            },
            submit() {
                axios.post("http://127.0.0.1:8000/scores/",this.form)
            }
        }

    }

</script>

<style scoped>

</style>