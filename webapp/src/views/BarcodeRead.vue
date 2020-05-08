<template>
    <div>
        <div class="row">
            <video id="preview"></video>


        </div>
        <div class="row">

            <div class="col">
                {{this.scannedInfo.scout}}
            </div>

            <div class="col">
                {{this.scannedInfo.patrol}}
            </div>

        </div>

        <button type="button" v-on:click="startScanning"> Start scanning</button>


    </div>
</template>

<script>
    import Instascan from 'instascan'

    export default {
        name: "BarcodeRead",

        data() {
            return {
                scanner: null,
                scannedInfo: {scout: null, patrol: null},
                goodBeep: null,
            }
        },
        mounted() {
            this.scanner = new Instascan.Scanner({video: document.getElementById('preview'), backgroundScan: false,});
            this.goodBeep = new Audio('http://soundbible.com/mp3/Checkout Scanner Beep-SoundBible.com-593325210.mp3');

        },
        methods: {
            startScanning() {
                this.scanner.addListener('scan', this.finishedScanning);
                Instascan.Camera.getCameras().then((cameras) => {
                    if (cameras.length > 0) {
                        this.scanner.start(cameras[0]);
                    } else {
                        console.error('No cameras found.');
                    }
                }).catch(function (e) {
                    console.error(e);
                });
            },
            finishedScanning(content) {
                this.scanner.removeListener('scan', this.finishedScanning);
                this.playerSound(this.goodBeep);
                this.scanner.stop();
                this.scannedInfo = JSON.parse(content);
                

            },
            playerSound(sound) {
                sound.play();
            }
        }
    }


</script>

<style scoped>

</style>