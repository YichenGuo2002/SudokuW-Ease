<template>
    <div class = "ml-48 mt-16 px-4 py-2 mb-4 text-black flex-1 bg-grey-lightest">
        <p>Click to learn about major Sudoku Solving Algorithms:
        <button  @click = "" class = "select-but">Backtracking</button>
        <button  @click = "" class = "select-but">Constraint Satisfaction</button>
        <button  @click = "" class = "select-but">Stochastic search/optimization methods</button>
        <button  @click = "" class = "select-but">Exact cover</button>
        <button  @click = "" class = "select-but">Relations and residuals</button>
        .</p>
        <p class = "p-2 m-2">
        After reducing the solution table according to IG the solution table also have only 1 number in other cells.<br/><br/>
        These cells have been reduced in the process and can now be entered into the sudoku.<br/><br/>
        When you enter the numbers into the sudoku you must remember to remove them from row, column and box in the the solution table too.<br/><br/>
        After removing these 3 new numbers from the solution table we got even more new numbers as solutions.<br/><br/> 
        Actually, this sudoku is SiSo-solvable. Meaning, we can solve the whole sudoku using only the SiSo-method. <br/><br/>
        If you continue inserting the solutions into the sudoku and removing them from the solution table you will eventually solve the sudoku without even doing anything else than crossing out numbers from the rows, columns or boxes.<br/><br/>
        It is easy to overlook a solution which has appeared in the solution table when you have removed numbers, so it is smart to compare the solution table with the sudoku once in a while. The SiSo is the simplest and most important method to solve a sudoku.<br/><br/>
        </p>
   </div>
</template>

<script>
    
</script>