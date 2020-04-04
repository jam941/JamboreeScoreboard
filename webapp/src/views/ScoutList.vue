<template>
    <div>
        <div v-for= "scout in scouts" >
            {{scout.name}}
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    export default {
        name: "ScoutList",
        data(){
            return {
                scouts: []
            }
        },
        created() {
            this.updateScouts()
        },
        methods: {
            updateScouts(){
                axios.get("http://127.0.0.1:8000/scouts/")
                    .then((response) => {
                        this.scouts = response.data
                    })
            }
        }
    }
</script>

<style scoped>

</style>