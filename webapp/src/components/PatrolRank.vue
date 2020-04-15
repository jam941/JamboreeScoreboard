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
    import axios from "axios"
    export default {
        name: "PatrolRank",

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
                axios.get("http://127.0.0.1:8000/patrol-score/")
                    .then((response) => {
                        this.scores = response.data;
                    });

            }

        }
    }
</script>

<style scoped>

</style>