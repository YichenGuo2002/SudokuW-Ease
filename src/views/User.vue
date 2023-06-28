<template>
    <div class = "main-container">
        <div class = "h-64 flex items-center p-8 border-b border-black">
            <div id="user-icon" class = "block h-32 w-32 rounded-full overflow-hidden border border-black m-8">
                <img src="../assets/icon_user.png" />
            </div>
            <div class = "h-32 m-8 flex flex-col justify-center">
                <p class="text-base mb-2">Username: </p>
                <p class="text-base mb-2">Email: </p>
            </div>
        </div>
        
        <div class = "p-8">
            <p class="text-base mb-2">{{ 0 ?
             'My Favorite List of Sudokus:':
             "You haven't saved any Sudokus. Start saving Sudoku puzzles!"}}</p>
            
            <button @click = "" class="select-but" type="button">
                Delete Account
            </button>
        </div>

    </div>
</template>

<script>
    
    export default{
        
    }
</script>