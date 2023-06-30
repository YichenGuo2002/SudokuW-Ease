<template>
    <div class = "main-container flex items-center justify-center ">
        <div class = "p-8 w-1/2 border border-black">
            <p class="block text-2xl" >Register</p>
            <label class="block text-sm mb-2 mt-4" for="email">
            Email:
            </label>
            <input class="shadow appearance-none border border-black rounded-lg w-full py-2 px-3 mb-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
            id="email" type="text" placeholder="Email">
            <label class="block text-sm mb-2" for="password">
            Password:
            </label>
            <input class="shadow appearance-none border border-black rounded-lg w-full py-2 px-3 mb-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
             id="password" type="text" placeholder="Password">
            <label class="block text-sm mb-2" for="password">
            Username:
            </label>
            <input class="shadow appearance-none border border-black rounded-lg w-full py-2 px-3 mb-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
             id="username" type="text" placeholder="Username">
            <button @click = "localRegister()" class="select-but" type="button">
            Register
            </button>
            <hr class = "border-t border-black my-4">
            <p>Already have an account? <router-link :to="'/login'" class = "text-black">Login</router-link>.</p>
        </div>
    </div>
</template>

<script>
    const {register} = window.electron;
    
    export default{
        methods:{
            async localRegister(){
                const email = document.getElementById('email');
                const password = document.getElementById('password');
                const name = document.getElementById('username');
                let newEmail = email.value;
                let newPassword = password.value;
                let newName = name.value;
                return await register(newEmail, newPassword, newName)
                .then(result =>{
                    console.log("I get the result", result)
                    email.value = ""
                    password.value = ""
                    name.value = ""
                })
            }
        }
    }
</script>