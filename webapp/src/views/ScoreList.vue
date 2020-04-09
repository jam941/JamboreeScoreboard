<template>
    <div>
        <div v-for= "score in rawScores" >
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

                    });


            }
        }
    }
</script>

<style scoped>

</style>