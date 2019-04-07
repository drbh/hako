<template>
    <div class="file-backdrop" id="main-file-viewer" @click="toggleFileViewer">
        <!-- <h2>{{ contents }}</h2> -->
        <div class="config-contents">
            <div>
                <h4>{{ contents.label }}</h4>
                <small>{{ contents.cid }}</small>
            </div>
            <br>
            <div v-if="ext == 'png' || ext == 'jpeg' ">
                <!--   <img v-if="contents['contents'] != undefined":src="'data:image/jpeg;base64, ' + contents['contents']" class="my-file-pane">
 -->
                <img :src="'data:image/jpeg;base64, ' + contents['contents']" class="my-file-pane">
            </div>
            <div v-else>
                <!-- ="ext == 'txt'"> -->
                <pre v-if="contents['contents'] != undefined"> {{ myFunction() }}</pre>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'FileViewer',
    props: {
        contents: String,
        ext: String
    },
    methods: {
        myFunction: function() {
            return atob(this.contents.contents);
        },
        toggleFileViewer: function() {
            if (this.$el.style.display != "block") {
                this.$el.style.display = "block";

            } else {
                this.$el.style.display = "none";
            }
        }
    }
}
</script>
<style>
.file-backdrop {
    display: none;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    position: absolute;
    z-index: 999999999;
    background-color: #085fcccc;

}

.config-contents pre {
    width: 100%;
}

.my-file-pane {
    max-height: 96%;
    max-width: 96%;
}

.config-contents {
    padding: 10px;
    background: white;
    -webkit-box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
    width: 80%;
    height: 90%;

    max-width: 80%;
    margin: 0 auto 0;
    margin-top: 2%;
    max-height: 90%;

    overflow-y: scroll;
    position: relative;
    -webkit-transition: all .2s ease-out;
    transition: all .2s ease-out;
}
</style>