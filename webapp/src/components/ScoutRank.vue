<template>
    <div>
        <div class="list-group" v-for= "score in scores" >
            <div class = "list-group-item">
                {{score}}
            </div>
        </div>
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
                    });

            }

        }


    }



</script>

<style scoped>

</style>