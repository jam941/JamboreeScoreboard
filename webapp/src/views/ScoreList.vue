<template>
    <div>
        <div>
            <scout-rank v-if="false"/>
        </div>

        <div class="lower">
            <PatrolRank/>
        </div>

    </div>
</template>

<script>
    import axios from "axios"
    import ScoutRank from "../components/ScoutRank";
    import PatrolRank from "../components/PatrolRank";

    export default {
        name: "ScoutList",
        components: {
            PatrolRank,
            ScoutRank
        },
        data() {
            return {
                rawScores: [],
                scores: {}
            }
        },
        created() {
            this.updateScores();

        },
        updated() {

        },
        methods: {
            updateScores() {
                axios.get("http://127.0.0.1:8000/scores/")
                    .then((response) => {
                        this.rawScores = response.data;
                    });
            }
        }
    }
</script>

<style scoped>


</style>