<template>
    <ul id="example-2">
        <li :key="index" v-for="(item, index) in people">
            {{ item.name.substring(0,8) }}
        </li>
    </ul>
</template>
<script>
export default {
    name: 'Contacts',
    props: {
        people: Array
    }
}
</script>
<style>
ul {
    list-style: none;
    padding-inline-start: 0;
}

li {
    font-size: 7pt;
    margin: 15px;
    padding: 10px;
    height: 40px;
    width: 40px;
    border-radius: 40px;
    line-height: 40px;
    border: solid 1px #085fcc;
}

li:hover {
    border: solid 1.5px #51cbaa;
}
</style>