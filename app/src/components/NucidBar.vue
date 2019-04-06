<template>
    <form @submit="checkForm">
        <p style="color:#AAA">nucid://</p>
        <input class="nucidbar" type="text" name="" placeholder="QmWzx5JKSjnBdnR8EhRPNyXQka2KZJiiXKu2jPqT7xHjQT_uxLpz8qvdVSB4yjpL6gX4LgYHzWhWxrYnmKQ3cyHHSic_xc8UZXUtf5APKX4ZsjXJnFJVJaL4XKXNMvuagVKCtWBt_image.png" />
        <button class="action-btn">GET</button>
    </form>
</template>
<script>
import $ from 'jquery';

export default {
    name: 'NucidBar',
    props: {
        query: String
    },
    methods: {
        checkForm: function(e) {


            var nucid = e.target.querySelector('input').value
            // cid = e.target
            var settings = {
                "async": true,
                "crossDomain": true,
                "url": "http://127.0.0.1:5000/decrypt_message",
                "method": "POST",
                "headers": {
                    "content-type": "application/json"
                },
                "processData": false,
                "data": JSON.stringify({
                    "username": this.$parent.username,
                    "nucid": nucid
                })
            }

            var info = nucid.split("//")[1].split("_");
            console.log(info)
            $.ajax(settings).done(function(response) {
                console.log(response);
                this.$parent.$parent.files.push({

                    "label": info[3],
                    "cid": info[0],
                    "contents": response["contents"],
                    "size": response["contents"].length

                })

                // {
                //     "label": "art.png",
                //     "cid": "QmWadaT...",
                //     "contents": null,
                //     "size": 18
                // }
            }.bind(this));

            e.preventDefault();

            // console.log(cid)


        }
    }
}
</script>
<style>
.nucidbar {
    outline-style: none;

    padding: 5px;
    font-weight: 200;
    font-size: 12pt;


    margin: 6px;
}


form:hover {
    /*border: 1px solid rgba(81, 203, 238, 1);*/
    border: 1px solid #085fcc;
}


form {

    margin-right: 8%;
    margin-left: 8%;
    margin-top: 2%;
    margin-bottom: 2%;

    display: flex;
    flex-direction: row;


    outline-style: none;


    border: solid 1px #efefef;
    border-radius: 40pt;

    padding: 2px;
}

input {
    flex-grow: 2;

    border: none;
}

input:focus {
    outline: none;
}

.action-btn {
    font-size: 12pt;
    font-weight: 500;

    outline-style: none;

    padding-left: 20px;
    padding-right: 20px;
    margin-right: 0px;
    border-top-right-radius: 40pt;

    border-bottom-right-radius: 40pt;
    /*background: rgba(81, 203, 238, 1);*/
    background: #085fcc;
    color: white;
}
</style>