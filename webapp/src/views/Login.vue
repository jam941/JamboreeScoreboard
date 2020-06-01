<template>
  <div>
    <div>
      <label class="login">
        Log in with your account information
      </label>
    </div>

    <div>
      <label >
        Username
        <input type="text" v-model="form.username" class="textField">
      </label>
    </div>

    <div>
      <label>
        Password
        <input type="password" v-model="form.password" class="textField">
      </label>
    </div>
    <div>
      <button type="button" class="btnColor" v-on:click="login()" >Submit</button>
    </div>
    <div>
      {{$store.state.loginToken}}
    </div>
    <button type="button" v-on:click="startScanning" class="btn" v-bind:class="{'btn-success':!scanning}" v-bind:disabled="scanning"> Start Scanning</button>
    <button v-on:click="stopScanning" id="stop" class="btn" v-bind:class="{'btn-danger':scanning}" v-bind:disabled="!scanning">Stop</button>
    <div class="col">
      <div class="row">
        <div class="position-relative  w-100">
          <video id="preview"></video>
          <span class="success-popup" v-if="justScanned">
            <i class="fas fa-check-circle"></i>
          </span>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
    import axios from "axios"
    import Instascan from 'instascan'
    export default {


        name: "Login",
        data() {
            return {
                "form": {
                    "username": null,
                    "password": null,
                },
                scanner: null,
                goodBeep: null,
                scanning: null,
                scannedInfo: null,
                justScanned:false,
            }
        },
        mounted() {
            this.scanner = new Instascan.Scanner({video: document.getElementById('preview'), backgroundScan: false,});
            this.goodBeep = new Audio('http://soundbible.com/mp3/Checkout Scanner Beep-SoundBible.com-593325210.mp3');

        },
        methods: {
            login() {
                axios.post("http://127.0.0.1:8000/api/login/", this.form).catch(error => {
                    console.error(error);
                }).then((response) => {
                    this.$store.commit("setLoginToken", response.data.token);
                })
            },
            startScanning() {
                this.scanning = true;
                this.scanner.addListener('scan', this.scanCode);
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
            scanCode(content) {
                this.justScanned=true;
                setTimeout(()=>{
                    this.justScanned=false;
                },1000);
                this.playerSound(this.goodBeep);
                this.scannedInfo = JSON.parse(content)
                this.$store.commit("setLoginToken", this.scannedInfo.token);

                this.$store.commit("addScore", this.form);
                this.stopScanning();
                setTimeout(()=>{
                    this.startScanning();
                },500)

            },
            stopScanning(content) {
                this.scanner.removeListener('scan', this.scanCode);
                this.scanner.stop();
                this.scanning = false;
            },
            playerSound(sound) {
                sound.play();
            }
        }
    }

</script>

<style scoped>
  .textField {
    color: #1fa67b;
    font-size: 18px;
    text-align: center;
    font-weight: bold;
    padding-bottom: 20px;
  }
  .btnColor {
    color: #fff;
    background-color: #1fa67b;
  }

  #login {
    padding-top: 50px
  }
  #login .form-wrap {
    width: 30%;
    margin: 0 auto;
  }
  #login h1 {
    color: #1fa67b;
    font-size: 18px;
    text-align: center;
    font-weight: bold;
    padding-bottom: 20px;
  }
  #login .form-group {
    margin-bottom: 25px;
  }
</style>