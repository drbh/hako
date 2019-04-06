<template>
    <div class="large-screen">
        <!-- <h4>My Files</h4> -->
        <div class="wrap">
            <div class="table-wrapper">
                <table class="table-responsive card-list-table">
                    <thead>
                        <tr>
                            <th>Label</th>
                            <th>CID</th>
                            <th>Size</th>
                            <th>Open</th>
                            <th>Permission</th>
                            <th>Policies</th>
                        </tr>
                        <tr class="mini">
                            <th>the NuCyhpher network label</th>
                            <th>the identifier on IPFS</th>
                            <th>the files size</th>
                            <th>click to open file</th>
                            <th>allow others to access</th>
                            <th>who has access</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr :key="index" v-for="(item, index) in files" :data="index">
                            <td data-title="Column #1" :title="item.label">{{ item.label.substring(0,8)+"..." }}</td>
                            <td data-title="Column #2" :title="item.cid">{{ item.cid.substring(0,8)+"..." }}</td>
                            <td data-title="Column #3">{{ humanFileSize(item.size, true) }}</td>
                            <td data-title="Column #4" @click="openFile">📖</td>
                            <td data-title="Column #5" @click="openFilePermissionViewer">🔓</td>
                            <!-- <td data-title="Column #6">👪</td> -->
                            <td data-title="Column #6" style="display: grid;min-height: 26px;">
                                <span class="allowed" :data="d.nucid" @click="copyToClipboard" v-for="d in item.granted_access">{{ d.user }}</span>
                                <!-- {{ item.granted_access }}  -->
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Files',
    props: {
        files: Array
    },
    methods: {
        humanFileSize(size) {
            var i = Math.floor(Math.log(size) / Math.log(1024));
            return (size / Math.pow(1024, i)).toFixed(2) * 1 + ' ' + ['B', 'kB', 'MB', 'GB', 'TB'][i];
        },
        // humanFileSize(bytes, si) {
        //     var thresh = si ? 1000 : 1024;
        //     if (Math.abs(bytes) < thresh) {
        //         return bytes + ' B';
        //     }
        //     var units = si ? ['kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'] : ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'];
        //     var u = -1;
        //     do {
        //         bytes /= thresh;
        //         ++u;
        //     } while (Math.abs(bytes) >= thresh && u < units.length - 1);
        //     return bytes.toFixed(1) + ' ' + units[u];
        // },
        openFile: function(e) {
            // get file index
            var filesindex = e.target.parentElement.getAttribute("data")
            // make visable
            document.getElementById("main-file-viewer").style.display = "block"
            // fetch file
            var dat = this.$parent.$parent.files[filesindex]
            // var fv = this.$parent.$children[1]
            // console.log("YYYYYYYY")
            var fv = this.$parent.$children.filter(function(elem) {
                return elem.$vnode.componentOptions.tag == "FileViewer"
            })[0]


            // update data
            fv.contents = dat
            fv.ext = ((dat != undefined) ? dat.label.split(".")[1] : '');

            console.log(dat)
        },
        openFilePermissionViewer: function(e) {
            // get file index
            var filesindex = e.target.parentElement.getAttribute("data")
            // make visable
            document.getElementById("main-file-permissions-viewer").style.display = "block"
            // fetch file
            var dat = this.$parent.$parent.files[filesindex]

            console.log(this.$parent.$children)
            // var fv = this.$parent.$children[2]
            var fpv = this.$parent.$children.filter(function(elem) {
                return elem.$vnode.componentOptions.tag == "FilePermissionsViewer"
            })[0]



            fpv.contents = dat

            console.log(fpv)
        },
        copyToClipboard(e) {



            console.log("NEW")
            console.log(e.target)

            // e.target.style.border = "solid 1px #000"
            e.target.style.background = "#085fcc"
            

            setInterval(function(event){
                // e.target.style.border = "none"
                e.target.style.background = "#4bcbf0"
            }, 600)

            // value = e.target.textContent
            var value = e.target.getAttribute("data")

            let textarea;
            let result;

            try {
                textarea = document.createElement('textarea');
                textarea.setAttribute('readonly', true);
                textarea.setAttribute('contenteditable', true);
                textarea.style.position = 'fixed'; // prevent scroll from jumping to the bottom when focus is set.
                textarea.value = value //string;

                document.body.appendChild(textarea);

                textarea.focus();
                textarea.select();

                const range = document.createRange();
                range.selectNodeContents(textarea);

                const sel = window.getSelection();
                sel.removeAllRanges();
                sel.addRange(range);

                textarea.setSelectionRange(0, textarea.value.length);
                result = document.execCommand('copy');
            } catch (err) {
                console.error(err);
                result = null;
            } finally {
                document.body.removeChild(textarea);
            }

            // manual copy fallback using prompt
            if (!result) {
                const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
                const copyHotkey = isMac ? '⌘C' : 'CTRL+C';
                result = prompt(`Press ${copyHotkey}`, string); // eslint-disable-line no-alert
                if (!result) {
                    return false;
                }
            }
            return true;
        },
        copyTestingCode(e) {

            console.log("yerp")
            console.log(e.target)

            // value = e.target.textContent
            var value = e.target.getAttribute("data")

            e.target.style.border = "solid 1px #000"

            console.log(value)

            var tempInput = document.createElement("input");
            // var tempInput = document.createElement("div");
            // el.contentEditable = true;



            tempInput.style = "font-size:16pt;position: absolute; left: -1000px; top: -1000px";
            tempInput.value = value;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand("copy");
            document.body.removeChild(tempInput);
        },
    }
}
</script>
<style>
.allowed {
    background-color: #4bcbf0;
    padding: 5px;
    border-radius: 13px;
    margin: 5px;
    font-size: 10pt;
    line-height: 10pt;
    text-align: center;

}

.mini {
    font-size: 6pt;
}

.mini th {
    color: #333 !important;
}

::-webkit-scrollbar {
    width: 0.15em;
    height: 0.15em;
}

::-webkit-scrollbar-thumb {
    background: slategray;
}

::-webkit-scrollbar-track {
    background: #b8c0c8;
}

/*body {
    scrollbar-face-color: slategray;
    scrollbar-track-color: #b8c0c8;
}*/

/*body,
html {
    height: 100%;
    width: 100%;
}
*/
/*body {
    font-family: "Roboto";
}
*/
.wrap {

    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 100%;
    width: 100%;
}

/*body {
    background: #f8f8f8;
}*/

button.btn {
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
    border: 0;
    border-radius: 0px;
}

button.btn i {
    margin-right: 3px;
}

div.large-screen .table-wrapper {
    margin-top: 40px;
    height: 70vh;
    max-width: 800px;
}

div.large-screen .card-list-table {
    background: white;
}

div.large-screen .card-list-table tbody tr {
    background: transparent;
    box-shadow: none;
    margin: 0;
}

div.large-screen .card-list-table tbody tr:nth-of-type(even) {
    background: #dfdfdf;
}

div.large-screen .card-list-table thead {
    display: table-header-group;
}

div.large-screen .card-list-table thead th:last-child {
    box-shadow: none;
}

div.large-screen .card-list-table thead th {
    border-bottom: 1px solid #dfdfdf;
    padding: 12px 24px;
}

div.large-screen .card-list-table tbody tr {
    display: table-row;
    padding-bottom: 0;
}

div.large-screen .card-list-table tbody tr:nth-of-type(even) {
    background: #fff;
}

div.large-screen .card-list-table tbody td {
    border-bottom: 1px solid #dfdfdf;
    cursor: pointer;
    display: table-cell;
    padding: 20px 24px;
    transition: background .2s ease-out;
    vertical-align: middle;
}

div.large-screen .card-list-table tbody td:after {
    display: none;
}

div.large-screen .card-list-table tbody td:before {
    content: '';
}

div.large-screen .card-list-table tbody tr:hover td {
    background: #fcf3d0;
}

.buttons {
    margin: 10px 0 50px;
}

.table-wrapper {
    height: 100%;
    max-width: 300px;

    margin: 0 auto 0;
    max-height: 500px;
    overflow-y: scroll;
    position: relative;
    transition: all .2s ease-out;
}

@media (min-width: 768px) {
    .table-wrapper {
        background: white;
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
    }
}

.card-list-table {
    table-layout: fixed;
    background: transparent;
    margin-bottom: 0;
    width: 100%;
}

.card-list-table thead {
    display: none;
}

.card-list-table tbody tr {
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
    background: #fff;
    border-bottom: 1px solid #dfdfdf;
    cursor: pointer;
    display: block;
    padding: 15px 10px;
    margin: 0 0 10px 0;
}

.card-list-table tbody td {
    border: 0;
    display: block;
    padding: 10px 10px 20px 40%;
    position: relative;
}

.card-list-table tbody td:first-of-type::after {
    visibility: hidden;
}

.card-list-table tbody td:after {
    content: '';
    width: calc(100% - 30px);
    display: block;
    margin: 0 auto;
    height: 1px;
    background: #dfdfdf;
    position: absolute;
    left: 0;
    right: 0;
    top: -6px;
}

.card-list-table tbody td:before {
    color: rgba(0, 0, 0, 0.35);
    text-transform: uppercase;
    font-size: .85em;
    content: attr(data-title);
    display: table-cell;
    font-weight: 500;
    height: 100%;
    left: 15px;
    margin: auto;
    position: absolute;
    vertical-align: middle;
    white-space: nowrap;
    width: 40%;
}

.card-list-table thead th {
    text-transform: uppercase;
    font-size: .85em;
    color: rgba(0, 0, 0, 0.35);
    letter-spacing: .5pt;
}
</style>