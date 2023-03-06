<template>
    Hi, size {{ puzzle.size }} {{ puzzle.sudoku }}.
    <div id="button-panel">
      <button class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Solve</button>
      <button class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Check</button>
      <button class = "inline-block mx-1 my-1 px-2 py-2 rounded-lg bg-grey-lighter text-black no-underline hover:bg-grey">Clear</button>
    </div>
</template>

<script>
export default {
  name: 'Sudoku',
  props:{
   puzzle:Object
  }
}
</script>