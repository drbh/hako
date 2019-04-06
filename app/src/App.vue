<!-- /* eslint-disable */  -->
<template>
    <!-- <h1> HAKO </h1> -->
    <div id="app">
        <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
        <!-- <div id="login-pane" style="display:none"> -->
        <div id="login-pane">
            <!-- <h2>Please Select a user</h2> -->
            <div class="middle-pane" id="signin">
                <img src="/hako_logo_white.png" style="height: 100px; padding: 5px; margin-bottom: 10px;">
                <br><small style="color:white;padding-top:40px">Log into your</small><br>
                <h2 style="color:white;line-height: 0px;">Futari</h2><br>
                <input type="text" class="new-futari-input" name="" style="text-transform: lowercase;" v-model="username"><br>
                <input type="password" class="new-futari-input" name="" v-model="password"><br>
                <button class="btn" @click="loginToFutari">Login</button><br>
                <a class="btn" @click="openCreatePane"><small>Create</small></a>
            </div>
            <div class="middle-pane" id="makenew" style="display:none">
                <br><small style="color:white;padding-top:40px">Make a new</small><br>
                <h2 style="color:white;line-height: 0px;">Futari</h2><br>
                <input type="text" class="new-futari-input" name="" style="text-transform: lowercase;" v-model="username"><br>
                <input type="password" class="new-futari-input" name="" v-model="password"><br>
                <button class="btn" @click="createNewFutari">Register</button><br>
            </div>
            <div id="futariCreateMessage" style="display:none;">
                <h1>Please wait while the Futari is being created</h1><br>
                <small>Could take up to 30 seconds</small>
            </div>
        </div>
        <Config :keys="userconfig" />
        <FileViewer :contents="currentFile" />
        <FilePermissionsViewer :contents="currentFile" />
        <div id="spinner-pane">
            <h1 id="spinner-counter">0</h1>
            <h1 id="spinner-text"></h1>
            <div class="lds-circle" id="spinner">
                <div></div>
            </div>
        </div>
        <div class="top-bar">
            <img src="/hako_logo_white.png" style="height: 30px; padding: 5px;">
            <p @click="copyMyKeys">MY KEYZ</p>
            <!-- <h4  contenteditable="true" class="username" v-model="username">{{ username }}</h4> -->
            <!-- <input type="text" class="pword-input" name="" v-model="username"> -->
            <!-- <input type="text" class="pword-input" name="" v-model="password"> -->
            <!-- <div class="leftside"> -->
            <a class="clickables" id="add-file-top" @click="toggleDropzone">💾</a>
            <a class="leftside" @click="toggleDropzone">{{ username }} </a>
            <!-- </div> -->
        </div>
        <div class="main">
            <div class="cent">
                <NucidBar query="" />
            </div>
            <div class="contain">
                <div class="left-pane">
                    <h4>My Friends</h4><br>
                    <a class="clickables" @click="addContact">➕</a>
                    <!-- <button @click="addContact">➕</button> -->
                    <Contacts :people="mycontacts" />
                </div>
                <!-- <button @click="addContact">Add</button> -->
                <div class="center-console">
                    <vue-dropzone ref="myVueDropzone" id="dropzone" v-on:vdropzone-sending="sendingEvent" v-on:vdropzone-success="uploadComplete" v-on:vdropzone-error="uploadError" :options="dropzoneOptions" style="display:none;"></vue-dropzone>
                    <Files :files="myfiles" />
                </div>
                <!-- <button @click="addContact">Grant</button> -->
                <div class="right-pane">
                    <h4>Add A File</h4><br>
                    <a class="clickables" id="add-file-right" @click="toggleDropzone">💾</a>
                    <!-- <br /> -->
                    <!-- <br /> -->
                    <!-- <h4>My Keys</h4><br> -->
                    <!-- <a class="clickables" @click="openConfig">🔐</a> -->
                </div>
            </div>
        </div>
    </div>
</template>
<script>
// import HelloWorld from './components/HelloWorld.vue'

import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'

import $ from 'jquery';

import NucidBar from './components/NucidBar.vue'
import Files from './components/Files.vue'
import Contacts from './components/Contacts.vue'
import Config from './components/Config.vue'
import FileViewer from './components/FileViewer.vue'
import FilePermissionsViewer from './components/FilePermissionsViewer.vue'


var refreshIntervalId = setInterval(function() {}, 100000000000000000000)
var host = "192.168.0.4"

export default {
    name: 'app',
    data: function() {
        return {
            // myname: ,
            mycontacts: [],
            currentFile: "",
            userconfig: [],
            myfiles: [],
            username: "drbh",
            // username: "",
            password: "thisismysupersecurepassword",
            // password: "",
            dropzoneOptions: {
                url: 'http://' + host + ':5000/data',
                thumbnailWidth: 150,
                maxFilesize: 100.0,
                // headers: ,
            },
        }
    },
    components: {
        // HelloWorld
        vueDropzone: vue2Dropzone,
        NucidBar,
        Files,
        FileViewer,
        FilePermissionsViewer,
        Contacts,
        Config
    },
    methods: {
        // updateCurrentFile: function() {
        //     this.currentFile = "davud";
        // },
        sendingEvent(file, xhr, formData) {

            console.log("START SPINNER")


            // if (document.getElementById("spinner").style.display != "block") {
            document.getElementById("spinner-pane").style.display = "block"

            document.getElementById("spinner-pane").style.backgroundColor = "#085fcccc"

            document.getElementById("spinner-text").innerHTML = "Adding File to IPFS"

            document.getElementById("spinner-counter").innerHTML = "0"


            refreshIntervalId = setInterval(function() {
                document.getElementById("spinner-counter").innerHTML = parseInt(document.getElementById("spinner-counter").innerHTML) + 1
            }, 1000);



            // } else {
            // document.getElementById("dropzone").style.display = "none"
            // }


            console.log(this.username, this.password)

            // console.log(file)
            formData.append("username", this.username)
            formData.append("password", this.password)
            formData.append("filename", file.name)

            // formData.append("contents", "hello world! this is a rest request 2")

            // formData.append('paramName', 'some value or other');
        },
        copyMyKeys() {
            var settings = {
                "async": true,
                "crossDomain": true,
                "url": "http://" + host + ":5000/my_public_keys",
                "method": "POST",
                "headers": {
                    "content-type": "application/json"
                },
                "processData": false,
                "data": JSON.stringify({
                    "username": this.username
                })
            }

            $.ajax(settings).done(function(response) {
                console.log(response);
            });
        },
        openCreatePane() {
            document.getElementById("signin").style.display = "none"
            document.getElementById("makenew").style.display = "block"
        },

        createNewFutari() {


            document.getElementById("makenew").style.display = "none"
            document.getElementById("futariCreateMessage").style.display = "block"


            console.log(this.username, this.password)

            var settings = {
                "async": true,
                "crossDomain": true,
                "url": "http://" + host + ":5000/create_user",
                "method": "POST",
                "headers": {
                    "content-type": "application/json"
                },
                "processData": false,
                "data": JSON.stringify({
                    "name": this.username,
                    "password": this.password
                })
            }

            $.ajax(settings).done(function(response) {
                console.log(response);



                location.reload()

            });

        },
        loginToFutari() {
            document.getElementById("login-pane").style.display = "none"
        },
        grantAccess(recipient_name, user, pass, cid, fname, enc, sig) {

            // console.log({
            //     "username": user,
            //     "password": pass,
            //     "cid": cid,
            //     "filename": fname,
            //     "enc": enc,
            //     "sig": sig,
            // })

            var data = JSON.stringify({
                "username": user,
                "password": pass,
                "cid": cid,
                "filename": fname,
                "enc": enc,
                "sig": sig,
            })

            console.log(data)

            var settings = {
                "async": true,
                "crossDomain": true,
                "url": "http://" + host + ":5000/allow_access",
                "method": "POST",
                "headers": {
                    "content-type": "application/json"
                },
                "processData": false,
                "data": data
            }

            $.ajax(settings).done(function(response) {
                console.log(response);

                var files = this.$parent.files

                var file = files.filter(function(el) {
                    return el.cid == cid
                })[0];

                file.granted_access.push({ "user": recipient_name, "allower": user, "nucid": response["nucid"] })


                console.log(file)

            }.bind(this));



        },
        uploadError(file, response) {
            console.log(response)
            document.getElementById("spinner-pane").style.display = "none"
            clearInterval(refreshIntervalId);
            console.log(refreshIntervalId)
        },
        uploadComplete(file, response) {

            console.log(response)


            var nucid = response["nucid"]
            var settings = {
                "async": true,
                "crossDomain": true,
                "url": "http://" + host + ":5000/decrypt_message",
                "method": "POST",
                "headers": {
                    "content-type": "application/json"
                },
                "processData": false,
                "data": JSON.stringify({
                    "username": this.username,
                    "nucid": nucid
                })
            }

            var info = nucid.split("//")[1].split("_");
            console.log(info)

            document.getElementById("spinner-pane").style.backgroundColor = "#08cc4dcc"
            document.getElementById("spinner-text").innerHTML = "Success, Now Fetching and Decrypting the File"

            $.ajax(settings).done(function(response) {

                // console.log("compeltedUpload",response);

                this.$parent.files.push({

                    "label": info[3],
                    "cid": info[0],
                    "contents": response["contents"],
                    "size": response["contents"].length,
                    "granted_access": [
                        { "user": this.username, "allower": this.username, "nucid": nucid }
                    ]

                })


                document.getElementById("spinner-pane").style.display = "none"
                document.getElementById("dropzone").style.display = "none"

                clearInterval(refreshIntervalId);
                console.log(refreshIntervalId)

                // {
                //     "label": "art.png",
                //     "cid": "QmWadaT...",
                //     "contents": null,
                //     "size": 18
                // }
            }.bind(this));

            // e.preventDefault();



            // formData.append('paramName', 'some value or other');
        },
        toggleDropzone: function() {
            if (document.getElementById("dropzone").style.display != "block") {
                document.getElementById("dropzone").style.display = "block"
            } else {
                document.getElementById("dropzone").style.display = "none"
            }

        },
        updateContacts: function() {
            this.mycontacts = this.$parent.contacts
        },
        updateFiles: function() {
            this.myfiles = this.$parent.files
        },
        updateConfig: function() {
            this.userconfig = this.$parent.user //[this.$parent.user.roles.alice.pub.root]
        },
        addContact: function() {
            this.$parent.contacts.push({
                "name": "richard",
                "pub": {
                    "root": "",
                    "signing": ""
                }
            })
        },
        // openConfig: function() {
        //     // need better way to call Config method


        //     var config = this.$parent.$children.filter(function(elem) { 
        //         return elem.$vnode.componentOptions.tag == "Config" 
        //     })[0]

        //     // this.$children[0]
        //     config.toggleConfig()
        //     // console.log()
        // }
    },
    created: function() {
        /* eslint-disable no-console */

        // this.checkForLocalStore()

        // // drop the box
        // setInterval(function(){
        //      document.getElementById("signin").style.marginTop = "20%"
        //  }, 750)


        this.updateContacts()
        this.updateConfig()
        this.updateFiles()
    }
}
</script>
<style>
select,
textarea,
input[type="text"],
input[type="password"],
input[type="datetime"],
input[type="datetime-local"],
input[type="date"],
input[type="month"],
input[type="time"],
input[type="week"],
input[type="number"],
input[type="email"],
input[type="url"],
input[type="search"],
input[type="tel"],
input[type="color"] {
    font-size: 16px;
}

@media only screen and (max-width: 1000px) {
    .left-pane {
        display: none;
    }

    .right-pane {
        display: none;
    }

    .mini {
        display: none;
    }

    #add-file-top {
        display: block;
    }

    .action-btn {
        margin-left: -10px !important;
    }


    .contain {
        font-size: 6pt;
    }

    th {
        padding: 1px !important;
    }

    .middle-pane {
        margin-top: 40% !important;
    }

}

@media only screen and (min-width: 1000px) {

    #add-file-top {
        display: none;
    }

    .middle-pane {
        max-width: 30% !important;
    }

    #login-pane input {
        padding: 6px;
        margin: 2px;
        border-radius: 6px;
    }


}

#login-pane input {
    color: #555;
}

.leftside {
    position: absolute;
    right: 0;
}

.middle-pane {
    z-index: 9999999999;
    background: #085fcc;

    background: white;
    background: #085fcc;

    border-radius: 8px;
    padding-top: 20px;

    height: 100%;
    max-width: 80%;
    margin: 0 auto 0;
    margin-top: 20%;
    max-height: 340px;

    position: relative;
    -webkit-transition: all .2s ease-out;
    transition: all .2s ease-out;
}

#login-pane {

    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    position: absolute;
    z-index: 999999999;
    background-color: #085fcccc;
    background-color: #085fcccc;
    background-color: #ffffffcc;
}



#spinner-pane {
    display: none;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    position: absolute;
    z-index: 999999999;
    background-color: #085fcccc;
}

#spinner {
    top: 40%;
    position: absolute;
}

.lds-circle {
    display: inline-block;
    transform: translateZ(1px);
}

.lds-circle>div {
    display: inline-block;
    width: 51px;
    height: 51px;
    margin: 6px;
    border-radius: 50%;
    background: #cef;
    animation: lds-circle 2.4s cubic-bezier(0, 0.2, 0.8, 1) infinite;
}

@keyframes lds-circle {

    0%,
    100% {
        animation-timing-function: cubic-bezier(0.5, 0, 1, 0.5);
    }

    0% {
        transform: rotateY(0deg);
    }

    50% {
        transform: rotateY(1800deg);
        animation-timing-function: cubic-bezier(0, 0.5, 0.5, 1);
    }

    100% {
        transform: rotateY(3600deg);
    }
}


.pword-input {
    border-radius: 5px;
    padding: 5px;
    margin: 5px;
}

.top-bar {

    display: -webkit-inline-box;
    background: #43cbf2;
    background: #085fcc;
    height: 36px;
    text-align: left;
    top: 0;
    left: 0;
    right: 0;
    position: absolute;
}

.username {
    color: #fff;
    margin: 10px;
}

th {
    color: #085fcc !important;
}

h4 {
    color: #aaa;
}

#app {

    padding-top: 60px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    font-family: 'Montserrat', sans-serif;

}

.left-pane {
    width: 100px;
    left: 18%;
    top: 15%;
    list-style-type: none;
}

.right-pane {
    width: 100px;
    right: 18%;
    top: 15%;
    list-style-type: none;
}

.contain {
    display: -webkit-inline-box;
}

.clickables {
    font-size: 16pt;
}

.clickables:hover {
    font-size: 18pt;
}
</style>