const URL = "http://127.0.0.1:5000";
const electron = require('electron')
const { ipcRenderer } = require('electron');

// Solving Sudoku puzzles (Sudoku component requests)
const solve = async (sudoku, size) =>{
    return await fetch(URL+"/solve", {
        // Adding method type
        method: "POST",
        // Adding body or contents to send
        body: JSON.stringify({
            sudoku: sudoku,
            size: size
        }),
        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
        })
        // Converting to JSON
        .then((response) => {
            return response.json()
        }).then((data) =>{
            console.log(data)
            return data.body
        })
}

// Scraping Sudoku puzzles(Find page requests)
const scrape = async (index, difficulty) =>{
    return await fetch(URL+"/scrape", {
    // Adding method type
    method: "POST",
    // Adding body or contents to send
    body: JSON.stringify({
        index: index,
        difficulty: difficulty
    }),
    // Adding headers to the request
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
    })
    // Converting to JSON
    .then((response) => {
        return response.json()
    }).then((data) =>{
        console.log(data)
        return data.body
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
