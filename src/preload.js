const electron = require('electron')
const { ipcRenderer } = require('electron');
const { app, BrowserWindow, contextBridge } = require('electron');
import io from 'socket.io-client';

// Establish WebSocket connection
const socket = io('http://localhost:5000');

/*
// Fetching RESTful APIs
const URL = "http://127.0.0.1:5000/";

const solve = async (sudoku, size) =>{
    return await fetch(URL + 'solve', {
        // Adding method type
        method: "POST",
        // Adding body or contents to send
        body: JSON.stringify({
            sudoku: sudoku,
            size: size
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
            return response.body
        })
}

// Scraping Sudoku puzzles(Find page requests)
const scrape = async (index, difficulty) =>{
    return await fetch(URL + 'scrape', {
    // Adding method type
    method: "POST",
    // Adding body or contents to send
    body: JSON.stringify({
        index: index,
        difficulty: difficulty
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
        return response.body
    })
}
*/


// Fetching GraphQL APIs
const URL = "http://127.0.0.1:5000/graphql";
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

const socket_on = () => {
    // Subscribe to 'new_message' event
    socket.emit('subscribe', { event: 'function_update' });

    // Handle 'function_update' event
    socket.on('function_update', (message) => {
        // Update your UI or perform actions based on the received message
        console.log('Received function update:', message.text);
    });
}

const socket_off = () => {
    socket.emit('unsubscribe', { event: 'function_update' });
    socket.off('function_update')
}

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById("btn-close").addEventListener('click', () => {
        ipcRenderer.invoke('quit-app');
    });

    document.getElementById("btn-minimize").addEventListener('click', () => {
        ipcRenderer.invoke('min-app');
    });
});

contextBridge.exposeInMainWorld('electron', {
    solve: solve, // Expose the solve function
    scrape: scrape, // Expose the scrape function
    socket_on: socket_on, // Expose the socket_on function
    socket_off: socket_off // Expose the socket_off function
});
