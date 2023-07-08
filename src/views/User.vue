<template>
    <div class = "main-container">
        <div class = "h-64 flex items-center p-8 border-b border-black">
            <div id="user-icon" class = "block h-32 w-32 rounded-full overflow-hidden border border-black m-8">
                <img src="../assets/icon_user.png" />
            </div>
            <div class = "h-32 m-8 flex flex-col justify-center">
                <p class="text-base mb-2">Username: {{user.name}}</p>
                <p class="text-base mb-2">Email: {{user.email}}</p>
            </div>
        </div>
        
        <div class = "p-8">
            <p class="text-base mb-2">{{favSudokus.length != 0 ?
             `My Favorite List of Sudokus: ${favSudokuStrings}`:
             "You haven't saved any Sudokus. Start saving Sudoku puzzles!"}}</p>
            
            <button @click = "test()" class="select-but" type="button">
                Delete Account
            </button>
        </div>

    </div>
</template>

<script>
    const {getFav} = window.electron;
    import {useUserStore} from '@/user'

    export default{
        mounted(){
            const store = useUserStore()
            if (store && store.userObject && store.userObject != null) {
                this.user = store.userObject
                if(this.user.id){
                    getFav(this.user.id)
                    .then((response)=> {
                        console.log("Favorite Sudokus",response.favSudokus)
                        this.favSudokus = response.favSudokus
                        for(let i = 0; i < this.favSudokus.length; i++){
                            this.favSudokuStrings.push(i + this.favSudokus[i].sudoku + "\n")
                        }
                    })
                }
            }else {
                this.$router.push({name:'Home'}) 
            }
        },
        data() {
                return {
                    user:{},
                    favSudokus:[],
                    favSudokuStrings:[]
                };
        },
        methods:{
            test(){
                console.log(this.$route.query)
            }
        }       
    }
</script>