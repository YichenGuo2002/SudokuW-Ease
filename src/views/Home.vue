<template>
    <div class = "ml-48 mt-16 px-4 py-2 mb-4 bg-white text-black flex-1">
        <p>Select your Sudoku of size:
        <button @click = "puzzle.size = 4; puzzle.sudoku=''" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">4×4</button>
        <button @click = "puzzle.size = 9; puzzle.sudoku=''" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">9×9</button>
        <button @click = "puzzle.size = 16; puzzle.sudoku=''" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">16×16</button>
        <button @click = "puzzle.size = 25; puzzle.sudoku=''" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">25×25</button>
        .</p>
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
                    sudoku:"",
                    size:4
                }
            }
        }
    }
</script>