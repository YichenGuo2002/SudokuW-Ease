<template>
    <div class = "main-container flex items-center justify-center ">
        <div class = "p-8 w-1/2 border border-black">
            <p class="block text-2xl" >Sign In</p>
            <p id = "errorMessage" class = "block mt-2 mb-2 text-red-light">{{ error }}</p>
            <label class="block text-sm mb-2 mt-4" for="username">
            Email:
            </label>
            <input class="shadow appearance-none border border-black rounded-lg w-full py-2 px-3 mb-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
            id="email" type="text" placeholder="Email">
            <label class="block text-sm mb-2" for="password">
            Password:
            </label>
            <input class="shadow appearance-none border border-black rounded-lg w-full py-2 px-3 mb-4 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
            id="password" type="text" placeholder="Password">
            <button @click = "localLogin()" class="select-but" type="button">
            Sign In
            </button>
            <hr class = "border-t border-black my-4">
            <p>Don't have an account? <router-link :to="'/register'" class = "text-black">Register</router-link>.</p>
        </div>
    </div>
</template>

<script>
    const {login} = window.electron;
    import {useUserStore} from '@/user'

    const store = useUserStore()
    const messages = [
        'Email not valid.',
        'Password not valid',
        'Connection error. Please try later!',
        'User retrieval error. Profile does not exist or database connection error. Please try again!'
    ]

    export default{
        data() {
                return {
                    error:""
                };
        },
        methods:{
            async localLogin(){
                const password = document.getElementById('password');
                const email = document.getElementById('email');
                let loginPassword = password.value;
                let loginEmail = email.value;
                let loginUser;

                if (loginEmail.length <= 60 && /[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/.test(loginEmail)) {
                    // Valid email
                } else {
                    // Invalid email
                    this.error = messages[0]
                    return
                }

                if (
                    loginPassword.length >= 6 &&
                    loginPassword.length <= 24 &&
                    /[a-z]/.test(loginPassword) &&
                    /[A-Z]/.test(loginPassword) &&
                    /[0-9]/.test(loginPassword)
                ) {
                    // Valid password
                } else {
                    // Invalid password
                    this.error = messages[1]
                    return
                }

                try{
                    await login(loginEmail, loginPassword)
                    .then(result =>{
                        console.log("I get the result", result.user)
                        password.value = ""
                        email.value = ""
                        loginUser = result.user
                    })
                }catch(err){
                    this.error = messages[2]
                    return
                }

                if(loginUser && loginUser != null){
                    console.log(loginUser)
                    store.defineName(loginUser.name);
                    store.defineId(loginUser.id);
                    store.defineEmail(loginUser.email);
                    this.$router.push({name:'User'})
                    return
                }else{
                    this.error = messages[3]
                    return
                }
            }
        }
    }
</script>