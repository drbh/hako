<template>
    <div class="backdrop" @click="toggleConfig">
        <div class="config-contents">
            <pre >{{ keys }}</pre>
<!--             <div :key="index" v-for="(item, index) in keys">
                {{ item }}
            </div> -->
        </div>
    </div>
</template>
<script>
export default {
    name: 'Config',
    props: {
        keys: Object
    },
    methods: {
        toggleConfig: function() {

            // console.log(this.$el)

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
.backdrop {
    display: none;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    position: absolute;
    z-index: 999999999;
    background-color: #085fcccc;

}

.config-contents pre{
    width: 100%;
}

.config-contents {
    background: white;
    -webkit-box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
    height: 100%;
    max-width: 50%;
    margin: 0 auto 0;
    margin-top: 10%;
    max-height: 500px;
    overflow-y: scroll;
    position: relative;
    -webkit-transition: all .2s ease-out;
    transition: all .2s ease-out;
}
</style>