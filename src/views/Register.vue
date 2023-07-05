<template>
    <div class = "main-container flex items-center justify-center ">
        <div class = "p-8 w-1/2 border border-black">
            <p class="block text-2xl mt-2" >Register</p>
            <p id = "errorMessage" class = "block mt-2 mb-2 text-red-light">{{error}}</p>
            <label class="block text-sm mb-2 mt-2" for="email">
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
    const messages = [
        'Email not valid.',
        'Password length should be between 6 and 24. Must include one uppercase, one lowercase letter, and one numerical number.',
        'Username can only include letters, numbers, and special characters("_.-"). Must be shorter than 24 characters.',
        'Connection error. Please try later!',
        'User creation error. Email already exists or database connection error. Please try again!'
    ]

    /*Email restrictions: 
    Maximum email length <= 60
    Allowed characters:
    latin letters (a-z).
    numbers (0-9).
    special characters: underscores (_), periods (.), and dashes (-).
    Must include an at sign (@).

    ## Password restrictions:
    Minimum password length >= 6
    Maximum password length <= 24
    Require at least one lowercase letter
    Require at least one uppercase letter
    Require at least one number

    ## Name restrictions:
    Allowed characters:
    latin letters (a-z).
    numbers (0-9).
    special characters: underscores (_), periods (.), and dashes (-). 
    Maximum username length <= 24 */
    export default{
        data(){
            return{
                error:""
            }
        }, 
        methods:{
            async localRegister(){
                this.error = ""
                const email = document.getElementById('email');
                const password = document.getElementById('password');
                const username = document.getElementById('username');
                let newEmail = email.value;
                let newPassword = password.value;
                let newUsername = username.value;
                let newUser;

                if (newEmail.length <= 60 && /[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/.test(newEmail)) {
                    // Valid email
                } else {
                    // Invalid email
                    this.error = messages[0]
                    return
                }

                if (
                    newPassword.length >= 6 &&
                    newPassword.length <= 24 &&
                    /[a-z]/.test(newPassword) &&
                    /[A-Z]/.test(newPassword) &&
                    /[0-9]/.test(newPassword)
                ) {
                    // Valid password
                } else {
                    // Invalid password
                    this.error = messages[1]
                    return
                }

                
                if (newUsername.length <= 24 && /^[a-zA-Z0-9_.-]+$/.test(newUsername)) {
                    // Valid username
                } else {
                    // Invalid username
                    this.error = messages[2]
                    return
                }


                try{
                    await register(newEmail, newPassword, newUsername)
                    .then(result =>{
                        console.log("I get the result", result.user)
                        email.value = ""
                        password.value = ""
                        username.value = ""
                        newUser = result.user
                    })
                }catch(err){
                    this.error = messages[3]
                    return
                }

                if(newUser && newUser != null){
                    console.log(newUser)
                    this.$router.push({name:'User', query: {
                        id:newUser.id,
                        name:newUser.name,
                        email:newUser.email
                    }})
                    return
                }else{
                    this.error = messages[4]
                    return
                }
            }
        }
    }
</script>