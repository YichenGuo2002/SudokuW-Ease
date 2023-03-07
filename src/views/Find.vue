<template>
    <div class = "ml-48 mt-16 px-4 py-2 mb-4 bg-white text-black flex-1">
        <p>Pick some Sudoku puzzles! 
        <button  @click = "getScrape(1, 'easy')" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">New York Times</button>
        <button  @click = "getScrape(2)" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Menneske.No 6913752 Random Sudokus</button>
        <button  @click = "getScrape(3)" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Sudokuweb.Org Generator</button>
        <button  @click = "getScrape(4)" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">UK Sudoku Daily Competition</button>
        <button  @click = "getScrape(5)" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Dr Arto Inkala's world hardest puzzle 2006</button>
        <button  @click = "getScrape(6)" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Dr Arto Inkala's world hardest puzzle 2010</button>
        <button  @click = "getScrape(7, 'medium')" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">USA Sudoku Championship 2020</button>
        <button  @click = "getScrape(8, 'slowest')" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Dr Peter's Unsolvable Sudoku</button>
        .</p>
        <p>{{ show }}</p>
    </div>
</template>

<script>
    const {solve, clear, scrape} = window.electron

    export default{
        data(){
            return{
                show: "Initial State"
            }
        },
        methods:{
            async getScrape(index, difficulty = ""){
                return await scrape(index, difficulty)
                .then(result =>{
                    console.log("I get the result", result)
                    this.show = result.sudoku
                })
            }
        }
    }
</script>