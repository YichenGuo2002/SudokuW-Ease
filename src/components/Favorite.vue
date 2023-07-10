<template>
    <div class = "flex flex-col items-center justify-center p-2">
      <table class = "flex-1 m-2" id = "sudoku-panel">
            <tbody v-html =  "puzzleTable"></tbody>
      </table>
      <div class = "flex-1" id="button-panel">
        <button @click = "" class = "select-but">Play</button>
        <button @click = "" class = "select-but">Remove</button>
      </div>
      <div class = "flex-1 m-2" id = "message-panel">
        <p>{{message}}</p>
      </div>
    </div>
  </template>
  
  <script>
    const printTable = (sudoku, size) =>{
          let result = "";
          const boxSize = Math.sqrt(size);
          if(sudoku.length != size * size) return "Error in reading Sudoku." + sudoku.length
          for(let i = 1; i <= size * size ; i++){
              if(i % size == 1){
                  result += '<tr>'
              }
  
              result += '<td class= " cell-block '
              if((i-1)/size <1) result +='cell-bt '
              if(i % size == 1) result +='cell-bl '
              if((i-1)/size >= size-1) result +='cell-bb '
              if(((i-1)/size < size-1) && Math.floor((i - 1) / size) % boxSize == boxSize - 1) result +='cell-bb-h '
              if(i % size == 0) result +='cell-br '
              if(i % boxSize == 0 && i % size != 0) result += 'cell-br-h '
              result += ' ">'
  
              if(Number.isInteger(sudoku[i-1]) && Number(sudoku[i-1]) != 0){
                  result += '<div class = "cell flex items-center justify-center bg-grey-light"> ' + Number(sudoku[i-1]).toString() + ' </div>'
              }else{
                  result += `<input oninput = "this.value = this.value.replace(/[^1-9.]/g, '').replace(/(\..*?)\..*/g, '$1');" class = "cell cell-input" type="text" size="1" autocomplete="off" maxlength="1" name="${i}" value="" />`
              }
  
              result += '</td>'
          
              if(i % size == 0){
                  result += '</tr>'
              }
          }
          return result
      }
  
    export default {
      name: 'Sudoku',
      props:{
        puzzle: Object
      },
      data(){
        return{
          localPuzzle: this.puzzle,
          message:''
        }
      }, 
      computed: {
        puzzleTable() {
          let result = printTable(this.localPuzzle.sudoku, this.localPuzzle.size);
          return result
        },
      },
      methods:{
        
      }
    }
  </script>