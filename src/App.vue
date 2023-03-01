<template>
    <div id="app" class="font-sans flex min-h-screen">
        <div id="nav">
            <router-link to="/">Home</router-link>
            <router-link to="/about">About</router-link>
        </div>
    <router-view/>
    </div>
</template>

<style src="./assets/tailwind.css"/>