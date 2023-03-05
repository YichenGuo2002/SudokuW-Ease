const URL = "http://127.0.0.1:5000";
const electron = require('electron')

// Solve page (Sudoku component) requests
const solve = async (sudoku, size) =>{
    let body = JSON.stringify({
        sudoku: sudoku,
        size: size
    });
    return await fetch(URL+"/solve", {
    // Adding method type
    method: "POST",
    // Adding body or contents to send
    body: body,
    // Adding headers to the request
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
    })
    // Converting to JSON
    .then(response => response.json())
}

// Find page requests
const scrape = async (index) =>{
    console.log("trying")
    return await fetch(URL+"/scrape", {
    // Adding method type
    method: "POST",
    // Adding body or contents to send
    body: JSON.stringify({
        index: index
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
        return data
    })
}


const check = () =>{

}

const clear = () =>{

}



electron.contextBridge.exposeInMainWorld('electron', {
    solve,
    check,
    clear,
    scrape
  });
