import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
    data: {
        "test": "david",
        "contacts": [
            {
                "name": "No Contacts!",
                "pub": {
                    "root": "25UygJ9kPhGPyfxA86257hpcBSrPxhd6oidMvSe1bb6Ei",
                    "signing": "2BcjLb7rcPa2GrvzTicQ1E6g4TAhHzgM7C6TNT5fGB1d2"
                }
            },
            // {
            //     "name": "example2",
            //     "pub": {
            //         "root": "dW85V8dbmrprrrsum2vAyy1S1L5aq8tk6cAbUV6vM1rp",
            //         "signing": "cMZA1owiVwAYWatWa7EN7dN3DdocYN1Ph3bDfHfSA7AC"
            //     }
            // }
        ],
        "files": [

// {

//     "label": "filename.txt",
//     "cid": "david",
//     "contents": "aaa",
//     "size": 5,
//     "granted_access": [
//         { "user": "me", "allower": "me", "nucid": "davidislistening" }
//     ]

// }
        ],
        "user": {
            "name": "david",
            "roles": {
                "alice": {
                    "pub": {
                        "root": "dsada",
                        "signing": ""
                    },
                    "priv": {
                        "delegating": "",
                        "root": "",
                        "signing": ""
                    }
                },
                "bob": {
                    "pub": {
                        "root": "",
                        "signing": ""
                    },
                    "priv": {
                        "root": "",
                        "signing": ""
                    }
                }
            }
        }
    }
}).$mount('#app')