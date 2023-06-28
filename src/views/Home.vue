<template>
    <div class = "main-container">
        <p>Select your Sudoku of size:
        <button @click = "puzzle.size = 4; puzzle.sudoku = Array(16)" class = "select-but">4×4</button>
        <button @click = "puzzle.size = 9; puzzle.sudoku = Array(81)" class = "select-but">9×9</button>
        <button @click = "puzzle.size = 16; puzzle.sudoku = Array(256)" class = "select-but">16×16</button>
        <button @click = "puzzle.size = 25; puzzle.sudoku = Array(625)" class = "select-but">25×25</button>
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
                    sudoku:Array(16),
                    size:4
                }
            }
        }
    }
</script>