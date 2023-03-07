<template>
  <div class = "flex flex-col items-center justify-center p-2">
    <table class = "flex-1 m-2" id = "sudoku-panel">
          <tbody v-html =  "puzzleTable"></tbody>
    </table>
    <div class = "flex-1" id="button-panel">
      <button class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Solve</button>
      <button class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Check</button>
      <button @click = "localClear" class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Clear</button>
    </div>
    <div class = "flex-1 m-2" id = "message-panel">
      <p>Not able to fetch.</p>
    </div>
  </div>
</template>

<script>
  const {solve, check, clear, scrape} = window.electron

  const printTable = (sudoku, size) =>{
        let result = "";
        if(sudoku.length != size * size) return "Error in reading Sudoku." + sudoku.length
        for(let i = 1; i <= size * size ; i++){
            if(i % size == 1){
                result += '<tr>'
            }

            result += '<td class= " cell-block '
            if((i-1)/size <1) result +='cell-bt '
            if(i % size == 1) result +='cell-bl '
            if((i-1)/size >= size-1) result +='cell-bb '
            if(i % size == 0) result +='cell-br '
            result += ' ">'
            if(Number.isInteger(sudoku[i-1]) && Number(sudoku[i-1]) != 0){
                result += Number(sudoku[i-1]).toString()
            }else{
                result += `<input oninput = "this.value = this.value.replace(/[^1-9.]/g, '').replace(/(\..*?)\..*/g, '$1');" class = "cell" type="text" size="1" autocomplete="off" maxlength="1" name="${i}" value="" />`
            }

            result += '</td>'
        
            if(i % size == 0){
                result += '</tr>'
            }
        }
        return result
    }

  const localSolve = () =>{

  }

  const localCheck = () =>{

  }

  export default {
    name: 'Sudoku',
    props:{
      puzzle: Object
    },
    data(){
      return{
        localPuzzle: this.puzzle,
      }
    }, 
    computed: {
      puzzleTable() {
        let result = printTable(this.localPuzzle.sudoku, this.localPuzzle.size);
        return result
      },
    },
    methods:{
        localClear(){
          this.localPuzzle.sudoku = new Array(this.localPuzzle.size ** 2).fill(0);
          const inputs = document.getElementsByClassName('cell');
          for (let i = 0; i < inputs.length; i++) {
            inputs[i].value = '';
        }
      }
    }
  }
</script>