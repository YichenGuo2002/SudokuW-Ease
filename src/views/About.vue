<template>
    <div class = "ml-48 mt-16 px-4 py-2 mb-4 text-black flex-1 bg-grey-lightest">
        <p class = "m-2">
        After reducing the solution table according to IG the solution table also have only 1 number in other cells.<br>
        These cells have been reduced in the process and can now be entered into the sudoku.
        When you enter the numbers into the sudoku you must remember to remove them from row, column and box in the the solution table too. 
        After removing these 3 new numbers from the solution table we got even more new numbers as solutions. 
        Actually, this sudoku is SiSo-solvable. Meaning, we can solve the whole sudoku using only the SiSo-method. 
        If you continue inserting the solutions into the sudoku and removing them from the solution table you will eventually solve the sudoku without even doing anything else than crossing out numbers from the rows, columns or boxes.
        It is easy to overlook a solution which has appeared in the solution table when you have removed numbers, so it is smart to compare the solution table with the sudoku once in a while. The SiSo is the simplest and most important method to solve a sudoku.
        </p>
   </div>
</template>

<script>
    
</script>