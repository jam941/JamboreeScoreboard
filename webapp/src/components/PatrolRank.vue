<template>

    <div>
        <table class="table">
            <thead>
            <caption>Patrol Rankings</caption>
            <thead class = "thead-dark">
            <tr>
                <th scope="col">Place</th>
                <th scope="col">Patrol Name</th>
                <th scope="col">Score</th>

            </tr>
            </thead>
            <tbody>
            <tr v-for="score in scores">
                <th scope="row">{{score.id}}</th>
                <td>{{score.patrol_name}}</td>
                <td>{{score.total_score}}</td>

            </tr>
            </tbody>
        </table>
    </div>

</template>

<script>
    import axios from "axios"

    export default {
        name: "PatrolRank",

        data() {
            return {
                scores: []
            }
        },
        created() {
            this.updateData()
        },
        methods: {

            updateData() {
                axios.get("http://127.0.0.1:8000/patrol-score/")
                    .then((response) => {
                        this.scores = response.data;
                        this.scores.sort(function (a, b) {
                            return b.total_score - a.total_score;
                        });
                        var count = 1;
                        for (var i in this.scores) {
                            this.scores[i].id = count++;
                        }
                    });


            }

        }
    }
</script>

<style scoped>

</style>