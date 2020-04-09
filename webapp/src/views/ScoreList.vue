<template>
    <div>
        <div v-for= "score in scores" >
            {{score}}
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    export default {
        name: "ScoutList",
        data(){
            return {
                rawScores: [],
                scores: {}
            }
        },
        created() {
            this.updateScores();

        },
        updated(){

        },
        methods: {
            updateScores(){
                axios.get("http://127.0.0.1:8000/scores/")
                    .then((response) => {
                         this.rawScores = response.data;
                        console.log(this.rawScores);
                        for ( let idx in this.rawScores){
                            var score =this.rawScores[idx];

                            if(score.patrol == null){


                            }


                        }
                    });


            }
        }
    }
</script>

<style scoped>

</style>