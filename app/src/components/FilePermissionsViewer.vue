<template>
    <div class="file-permissions-backdrop" id="main-file-permissions-viewer">
        <div class="permission-config-contents" onClick="javascript:void(0)">
            <h4>Select a contact to share the file with</h4><br>
            <div class="perm-contents">
                <select v-model="selected" id="soflow">
                    <option v-for="contact in $parent.$parent.contacts" v-bind:value="contact.name" v-on:change="selectUserToShare">
                        {{ contact.name }}
                    </option>
                </select>
                <a @click="grantUserAccess" class="clickables perm-click">🔓</a>
            </div>
            <br>
            <a @click="showAdd">add new contact</a><br>
            <!-- <input type="text" name="" id="userKeysInput"> -->
            <!-- <span>Selected: {{ selected }}</span> -->
        </div>
        <div class="file-permissions-backdrop-dark" @click="toggleFilePermissionsViewer">
        </div>
    </div>
</template>
<script>
/* eslint-disable no-console */

export default {
    name: 'FilePermissionsViewer',
    props: {
        contents: String,
        contacts: Array,
        selected: String,
    },
    methods: {
        selectUserToShare: function(e) {
            console.log(e)
        },
        toggleFilePermissionsViewer: function() {
            if (this.$el.style.display != "block") {
                this.$el.style.display = "block";
            } else {
                this.$el.style.display = "none";
            }

        },
        showAdd(){
            console.log("ALLOW FUTARI KEY ADD")
            this.toggleFilePermissionsViewer()
            document.getElementById("centerContactAdd").style.display = "block"
        },
        grantUserAccess: function() {

            var sel = this.selected

            var user = this.$parent.$parent.contacts.filter(function(el) {
                return el.name == sel
            })[0].pub;

            console.log(user)

            this.$parent.grantAccess(
                sel,
                this.$parent.username,
                this.$parent.password,
                // "12345678901234567890",
                this.contents["cid"],
                this.contents["label"],
                user.root,
                user.signing
            )
        }
    }
}
</script>
<style>

#userKeysInput{
    display: none;
    background-color: blue;
}

.perm-click {
    margin-top: 20px;
}

.perm-contents {
        width: 90%;
    display: inline-flex;
}

.file-permissions-backdrop {
    display: none;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    position: absolute;
    z-index: 999999999;

}

.file-permissions-backdrop-dark {
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

.my-file-permissions-pane {
    max-width: 100%;
}

select#soflow,
select#soflow-color {
    -webkit-appearance: button;
    -webkit-border-radius: 2px;
    -webkit-box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.1);
    -webkit-padding-end: 20px;
    -webkit-padding-start: 2px;
    -webkit-user-select: none;
    background-image: url(http://i62.tinypic.com/15xvbd5.png), -webkit-linear-gradient(#FAFAFA, #F4F4F4 40%, #E5E5E5);
    background-position: 97% center;
    background-repeat: no-repeat;
    border: 1px solid #AAA;
    color: #555;
    font-size: inherit;
    margin: 20px;
    overflow: hidden;
    padding: 5px 10px;
    text-overflow: ellipsis;
    white-space: nowrap;
    width: 100%;
}

.permission-config-contents {
    z-index: 9999999999;
    background: white;
    -webkit-box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
    height: 100%;
    max-width: 80%;
    margin: 0 auto 0;
    margin-top: 50%;
    max-height: 240px;
    overflow-y: scroll;
    position: relative;
    -webkit-transition: all .2s ease-out;
    transition: all .2s ease-out;
}
</style>