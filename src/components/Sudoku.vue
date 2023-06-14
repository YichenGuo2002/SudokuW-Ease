<template>
  <div class = "flex flex-col items-center justify-center p-2">
    <table class = "flex-1 m-2" id = "sudoku-panel">
          <tbody v-html =  "puzzleTable"></tbody>
    </table>
    <div class = "flex-1" id="button-panel">
      <button @click = "localSolve" class = "select-but">Solve</button>
      <button @click = "localCheck" class = "select-but">Check</button>
      <button @click = "localClear" class = "select-but">Clear</button>
      <button @click = "" class = "select-but">Save</button>
    </div>
    <div class = "flex-1 m-2" id = "message-panel">
      <p>{{message}}</p>
    </div>
  </div>
</template>

<script>
  const {solve, scrape} = window.electron

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

  function collect(){
    let values = [];
    const cells = document.getElementsByClassName('cell');
    for (let i = 0; i < cells.length; i++) {
      if(cells[i].tagName == "DIV"){
        values.push(Number(cells[i].textContent.trim()));
      }else if(cells[i].tagName == "INPUT"){
        if(cells[i].value.trim()){
          values.push(Number(cells[i].value.trim()))
        }
        else{
          values.push(0)
        }
      }
    }
    return values
  }

  const check = () =>{
    let sudoku = collect()
    const size = Math.sqrt(sudoku.length);

    // Check each row
    for (let i = 0; i < size; i++) {
      const row = new Set();
      for (let j = 0; j < size; j++) {
        const num = sudoku[i * size + j];
        if (num < 1 || num > size || row.has(num)) {
          return false;
        }
        row.add(num);
      }
    }

    // Check each column
    for (let j = 0; j < size; j++) {
      const col = new Set();
      for (let i = 0; i < size; i++) {
        const num = sudoku[i * size + j];
        if (num < 1 || num > size || col.has(num)) {
          return false;
        }
        col.add(num);
      }
    }

    // Check each box
    const boxSize = Math.sqrt(size);
    for (let r = 0; r < size; r += boxSize) {
      for (let c = 0; c < size; c += boxSize) {
        const box = new Set();
        for (let i = r; i < r + boxSize; i++) {
          for (let j = c; j < c + boxSize; j++) {
            const num = sudoku[i * size + j];
            if (num < 1 || num > size || box.has(num)) {
              return false;
            }
            box.add(num);
          }
        }
      }
    }

    // All checks passed, Sudoku is valid
    return true;
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
      collect,
      localClear(){
        this.localPuzzle.sudoku = new Array(this.localPuzzle.size ** 2).fill(0);
        const inputs = document.getElementsByClassName('cell-input');
        for (let i = 0; i < inputs.length; i++) {
          inputs[i].value = '';
        }
        this.message = ""
      },
      async localSolve(){
        console.time('Execution Time');
        let solution =  await solve(collect(), this.localPuzzle.size)
                .then(result =>{
                    console.log("I get the result", result)
                    this.localPuzzle.sudoku = result.solution
                    this.message = `Solved in ${(result.time * 1000).toFixed(5)} ms.`
                })
        console.timeEnd('Execution Time');
        return solution
      },
      localCheck(){
        if(check()){
          this.message = "Check passed."
        }else{
          this.message = "Check failed."
        }
      }
    }
  }
</script>