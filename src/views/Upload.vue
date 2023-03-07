<template>
    <div class = "ml-48 mt-16 px-4 py-2 mb-4 bg-white text-black flex-1">
        <div>
            <p class="m-2">
            Input your own Sudoku Puzzle:
            </p>
            <textarea class="border border-black rounded-lg w-full h-64 p-2 m-2 text-black leading-normal focus:outline-none focus:shadow-outline" id="userPuzzle" type="text"  />
        </div>
        <button @click = "getUpload" class="mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey" type="button">
        Submit
        </button>
        <button @click = "clearUpload" class="mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey" type="button">
        Clear
        </button>
        <Sudoku v-bind:puzzle="puzzle"/>
    </div>
</template>

<script>
    import Sudoku from '../components/Sudoku.vue'
    
    export default{
        components:{
            Sudoku,
        },
        data(){
            return{
                puzzle:{
                    sudoku:Array(16),
                    size:4
                }
            }
        },
        methods:{
            clearUpload(){
                document.getElementById("userPuzzle").value = ""
                this.puzzle.sudoku = Array(16)
                this.puzzle.size = 4
            },
            getUpload(){
                console.log("trying")
                let result = document.getElementById("userPuzzle").value.split(',');
                let localPuzzle = [];
                for(let i = 0; i < result.length; i++){
                    if (!isNaN(result[i]) && parseInt(result[i]) != 0){
                        localPuzzle.push(parseInt(result[i]) )
                    }else{
                        localPuzzle.push(0)
                    }
                }
                this.puzzle.sudoku = localPuzzle
                this.puzzle.size = Math.sqrt(localPuzzle.length);
            },
            
        }
    }
</script>