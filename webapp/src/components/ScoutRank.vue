<template>
    <div>
        <table class="table">
            <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Scout Name</th>
                <th scope="col">Troop Number</th>
                <th scope="col">Patrol Name</th>
                <th scope="col">Score</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="score in scores">
                <th scope="row">1</th>
                <td>{{score.scout_name}}</td>
                <td>{{score.troop_number}}</td>
                <td>{{score.patrol_name}}</td>
                <td>{{score.score}}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    /**
     * Data: Troop, Patrol, sum of their specific Score, Scout name
     * API: Troop, patrol, scout, score
     * Score: get scores, iterate over( select all scores with them as scout, grab numeric score and add in )
     */

    import axios from "axios"
    export default {

        name: "ScoutRank",

        data(){
            return{
                scores:[]
            }
        },
        created(){
            this.updateData()
        },
        methods:{

            updateData(){
                axios.get("http://127.0.0.1:8000/scout-score/")
                    .then((response) => {
                        this.scores = response.data;
                        this.scores.sort(function(a,b){
                            return b.score-a.score;
                        })
                    });

            }

        }


    }



</script>

<style scoped>

</style>