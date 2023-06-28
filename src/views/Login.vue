<template>
    <div class = "main-container flex items-center justify-center ">
        <div class = "p-8 w-1/2 border border-black">
            <p class="block text-2xl" >Sign In</p>
            <label class="block text-sm mb-2 mt-4" for="username">
            Email:
            </label>
            <input class="shadow appearance-none border border-black rounded-lg w-full py-2 px-3 mb-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Email">
            <label class="block text-sm mb-2" for="password">
            Password:
            </label>
            <input class="shadow appearance-none border border-black rounded-lg w-full py-2 px-3 mb-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="password" type="text" placeholder="Password">
            <button @click = "" class="select-but" type="button">
            Sign In
            </button>
            <hr class = "border-t border-black my-4">
            <p>Don't have an account? <router-link :to="'/register'" class = "text-black">Register</router-link>.</p>
        </div>
    </div>
</template>

<script>
    
    export default{
        
    }
</script>