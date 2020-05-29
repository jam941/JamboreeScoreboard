<template>
  <div>
    <div class="col">
      <div>
        <label class="row d-none">
          Submitting User
          <!--TODO set to logged in user-->
          <input type="text" v-model="form.submit_user">
        </label>

        <div class="row">
          <div class="col">
            <div class="col-xs-12">
              <br> Comment:
              <br>
              <div class="btn-group btn-group-vertical" data-toggle="buttons">
                <label class="btn active">
                  <input type="radio" name='comment1' v-model="form.comment"
                         value="completed activity">
                  <i class="fa fa-circle-o fa-2x"/><i class="fa fa-dot-circle-o fa-2x"/>
                  <span> Completed Activity</span>
                </label>
                <label class="btn active">
                  <input type="radio" name='comment2' v-model="form.comment" value="good turn">
                  <i class="fa fa-circle-o fa-2x"/><i class="fa fa-dot-circle-o fa-2x"/>
                  <span> Good Turn Daily</span>
                </label>

              </div>

            </div>
          </div>

          <div class="col">
            <div class="col-xs-12">
              <br> Score:
              <br>
              <div class="btn-group btn-group-vertical" data-toggle="buttons">
                <label class="btn active">
                  <input type="radio" name='score1' v-model="form.score" value="1" checked>
                  <i class="fa fa-circle-o fa-2x"/>
                  <i class="fa fa-dot-circle-o fa-2x"/>
                  <span>  1</span>
                </label>
                <label class="btn active">
                  <input type="radio" name='score2' v-model="form.score" value="2">
                  <i class="fa fa-circle-o fa-2x"/>
                  <i class="fa fa-dot-circle-o fa-2x"/>
                  <span> 2</span>
                </label>
                <label class="btn active">
                  <input type="radio" name='score3' v-model="form.score" value="3">
                  <i class="fa fa-circle-o fa-2x"/>
                  <i class="fa fa-dot-circle-o fa-2x"/>
                  <span> 3</span>
                </label>
              </div>

            </div>
          </div>
        </div>
      </div>
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
    import Instascan from 'instascan'
    import axios from "axios"

    export default {
        name: "BarcodeRead",

        data() {
            return {
                scanner: null,
                scannedInfo: {scout: null, patrol: null},
                goodBeep: null,
                "form": {
                    "score": 1,
                    "submit_user": "Jarred",
                    "comment": "completed activity",
                    "scout": "",
                    "patrol": ""
                },
                scanning:false,
                justScanned:false,
            }
        },
        mounted() {
            this.scanner = new Instascan.Scanner({video: document.getElementById('preview'), backgroundScan: false,});
            this.goodBeep = new Audio('http://soundbible.com/mp3/Checkout Scanner Beep-SoundBible.com-593325210.mp3');

        },
        methods: {
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
                if (this.scannedInfo.patrol == null) {
                    this.form.scout = this.scannedInfo.scout;
                } else {
                    this.form.patrol = this.scannedInfo.patrol
                }

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
  label.btn span {
    font-size: 1.5em;
  }

  label input[type="radio"] ~ i.fa.fa-circle-o {
    color: #c8c8c8;
    display: inline;
  }

  label input[type="radio"] ~ i.fa.fa-dot-circle-o {
    display: none;
  }

  label input[type="radio"]:checked ~ i.fa.fa-circle-o {
    display: none;
  }

  label input[type="radio"]:checked ~ i.fa.fa-dot-circle-o {
    color: #42424a;
    display: inline;
  }

  label:hover input[type="radio"] ~ i.fa {
    color: #42424a;
  }

  label input[type="checkbox"] ~ i.fa.fa-square-o {
    color: #c8c8c8;
    display: inline;
  }

  label input[type="checkbox"] ~ i.fa.fa-check-square-o {
    display: none;
  }

  label input[type="checkbox"]:checked ~ i.fa.fa-square-o {
    display: none;
  }

  label input[type="checkbox"]:checked ~ i.fa.fa-check-square-o {
    color: #42424a;
    display: inline;
  }

  label:hover input[type="checkbox"] ~ i.fa {
    color: #42424a;
  }

  div[data-toggle="buttons"] label.active {
    color: #42424a;
  }

  div[data-toggle="buttons"] label {
    display: inline-block;
    padding: 6px 12px;
    margin-bottom: 0;
    font-size: 14px;
    font-weight: normal;
    line-height: 2em;
    text-align: left;
    white-space: nowrap;
    vertical-align: top;
    cursor: pointer;
    background-color: none;
    border: 0px solid #c8c8c8;
    border-radius: 3px;
    color: #c8c8c8;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    -o-user-select: none;
    user-select: none;
  }

  div[data-toggle="buttons"] label:hover {
    color: #7AA3CC;
  }

  div[data-toggle="buttons"] label:active, div[data-toggle="buttons"] label.active {
    -webkit-box-shadow: none;
    box-shadow: none;
  }

  #preview{
    width: 100%;
    object-fit: scale-down;
    z-index: 1;
  }

  .success-popup{
    position: absolute;
    left:50%;
    top:50%;
    transform: translate(-50%,-50%);
    z-index: 10;
    color: greenyellow;
    font-size: 3em;
  }

</style>