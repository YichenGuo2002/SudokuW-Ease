<template>
    <div class = "ml-48 mt-16 px-4 py-2 mb-4 bg-white text-black flex-1">
        <table>
            <tbody v-html =  "printTable(puzzle, 4)">
            </tbody>
        </table>
    </div>
</template>

<script>
import { isIntegerKey } from '@vue/shared';

    const printTable = (sudoku, size) =>{
        let result = "";
        if(sudoku.length != size * size) return "Error in reading Sudoku."
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
                result += `<input oninput = "this.value = this.value.replace(/[^1-9.]/g, '').replace(/(\..*?)\..*/g, '$1');" class = "cell" type="text" size="1" maxlength="1" name="${i}" value=""/>`
            }

            result += '</td>'
        
            if(i % size == 0){
                result += '</tr>'
            }
        }
        return result
    }

    export default{
        data(){
            return{
                puzzle: [ 9, 8, 0, 6, 0, 7, 0, 4, 0, 4, 0, 0, 0, 0, 0, 6]
            }
        },
        methods:{
            printTable
        }
    }
</script>