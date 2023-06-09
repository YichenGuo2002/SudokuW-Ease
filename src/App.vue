<template>
    <div id="app" class="flex min-h-screen block text-red-dark bg-grey-lightest">
        <sidebar></sidebar>
    <router-view/>
    </div>
</template>

<script>
    import Sidebar from "./components/Sidebar.vue"

    export default{
        components:{
            Sidebar,
        },
    }
</script>

<style src="./assets/tailwind.css"/>