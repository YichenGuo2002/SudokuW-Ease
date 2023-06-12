<template>
    <div class = "ml-48 mt-16 px-4 py-2 mb-4 text-black flex-1 bg-grey-lightest">
        <p>Pick some Sudoku puzzles! 
        <button  @click = "getScrape(1, 'easy')" class = "select-but">New York Times Daily Easy</button>
        <button  @click = "getScrape(1, 'medium')" class = "select-but">New York Times Daily Medium</button>
        <button  @click = "getScrape(1, 'hard')" class = "select-but">New York Times Daily Hard</button>
        <button  @click = "getScrape(2)" class = "select-but">Menneske.No 6913752 Random Sudokus</button>
        <button  @click = "getScrape(3)" class = "select-but">Sudokuweb.Org Generator</button>
        <button  @click = "getScrape(4)" class = "select-but">UK Sudoku Daily Competition</button>
        <button  @click = "getScrape(5)" class = "select-but">Dr Arto Inkala's world hardest puzzle 2006</button>
        <button  @click = "getScrape(6)" class = "select-but">Dr Arto Inkala's world hardest puzzle 2010</button>
        <button  @click = "getScrape(7, 'medium')" class = "select-but">USA Sudoku Championship 2020</button>
        <button  @click = "getScrape(8, 'slowest')" class = "select-but">Dr Peter's Unsolvable Sudoku</button>
        .</p>
        <Sudoku v-bind:puzzle="puzzle"/>
    </div>
</template>

<script>
    const {scrape} = window.electron
    import Sudoku from '../components/Sudoku.vue'

    export default{
        components:{
            Sudoku,
        },
        data(){
            return{
                puzzle:{
                    sudoku:Array(81),
                    size:9
                }
            }
        },
        methods:{
            async getScrape(index, difficulty = ""){
                return await scrape(index, difficulty)
                .then(result =>{
                    console.log("I get the result", result)
                    this.puzzle.sudoku = result.sudoku
                    this.puzzle.size = result.size
                })
            }
        }
    }
</script>