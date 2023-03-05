<template>
    <div id="app" class="font-sans flex min-h-screen block text-red-dark">
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