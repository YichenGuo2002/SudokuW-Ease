const URL = "http://127.0.0.1:5000/graphql";
const electron = require('electron')
const { ipcRenderer } = require('electron');

// Solving Sudoku puzzles (Sudoku component requests)
const solve = async (sudoku, size) =>{
    const query = `mutation SolveSudoku {
        solveSudoku(
          sudoku: ${JSON.stringify(sudoku)},
          size: ${size}
        ){
          solution
          time
        }
      }`;
    
    return await fetch(URL, {
        // Adding method type
        method: "POST",
        // Adding body or contents to send
        body: JSON.stringify({
            query: query
          }),
        // Adding headers to the request
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        })
        // Converting to JSON
        .then((response) => {
            return response.json()
        }).then((response) =>{
            console.log(response)
            return response.data.solveSudoku
        })
}

// Scraping Sudoku puzzles(Find page requests)
const scrape = async (index, difficulty) =>{
    const query = `mutation ScrapeSudoku{
        scrapeSudoku(
              index:${index},
              difficulty:${JSON.stringify(difficulty)}
          ) 
          {
         sudoku,
              size,
              difficulty
        }
      }
    `;
    console.log(query)
    return await fetch(URL, {
    // Adding method type
    method: "POST",
    // Adding body or contents to send
    body: JSON.stringify({
        query: query
    }),
    // Adding headers to the request
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    })
    // Converting to JSON
    .then((response) => {
        return response.json()
    }).then((response) =>{
        console.log(response)
        return response.data.scrapeSudoku
    })
}

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById("btn-close").addEventListener('click', () => {
        ipcRenderer.invoke('quit-app');
    });

    document.getElementById("btn-minimize").addEventListener('click', () => {
        ipcRenderer.invoke('min-app');
    });
});

electron.contextBridge.exposeInMainWorld('electron', {
    solve,
    scrape
  });
