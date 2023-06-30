const electron = require('electron')
const { ipcRenderer } = require('electron');
const { app } = require('electron');
//const { w3cwebsocket: WebSocket } = require('websocket');

// Establish WebSocket connection
//const socket = new WebSocket('ws://localhost:5000');

// Event listeners for WebSocket connection
/*
socket.onopen = () => {
    console.log('WebSocket connection established');
};

  // Event listener for WebSocket connection errors
socket.onerror = (error) => {
    console.error('WebSocket error:', error);
    console.error('WebSocket error message:', error.message);
};

socket.onmessage = (event) => {
    // Handle incoming messages
    const message = JSON.parse(event.data);
    console.log('Received function update:', message.text);
    return false;
};
  
socket.onclose = () => {
    console.log('WebSocket connection closed');
};*/

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
const scrape = async (index, difficulty = "") =>{
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

const register = async (email, password, name) =>{
    const query = `mutation Register{
    register(
		email:"${email}",
		password:"${password}",
		name:"${name}"
	)
	{
   user{
		id,
		email,
		name
		}
    }
    }
    `;
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
        return response.data.register
    })
}

const login = async (email, password) =>{
    const query = `mutation Login{
    login(
		email:"${email}",
		password:"${password}"
	)
	{
   user{
		id,
		email,
		name,
		fav{
			sudoku
			}
		}
    }
    }
    `;
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
        return response.data.login
    })
}

const removeUser = async (userId) =>{
    const query = `mutation RemoveUser{
    removeUser(
		userId:${userId},
	)
	{
    success
	}
    }
    `;
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
        return response.data.removeUser
    })
}

const fav = async (sudoku, userId) =>{
    const query = `
        mutation Fav{
        fav(
                sudoku:${JSON.stringify(sudoku)},
                userId:${userId},
            )
            {
        success
            }
        }
    `;
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
        return response.data.fav
    })
}

// Scraping Sudoku puzzles(Find page requests)
const getFav = async (userId) =>{
    const query = `mutation GetFav{
        getFav(
                userId:${userId}
            )
            {
        favSudokus{
                sudoku,
                id,
                userId,
                user{
                    name,
                    email
                }
            }
            }
        }
    `;
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
        return response.data.getFav
    })
}

const removeFav = async (sudokuId, userId) =>{
    const query = `mutation RemoveFav{
        removeFav(
              userId:${userId},
              sudokuId:${sudokuId}
          )
          {
         success
          }
      }
    `;
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
        return response.data.removeFav
    })
}

/*
const socket_on = () => {
    // Subscribe to 'function_update' event
    const message = {
      event: 'function_update',
      action: 'subscribe',
    };
    socket.send(JSON.stringify(message));
  };
  
  const socket_off = () => {
    // Unsubscribe from 'function_update' event
    const message = {
      event: 'function_update',
      action: 'unsubscribe',
    };
    socket.send(JSON.stringify(message));
  };*/

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById("btn-close").addEventListener('click', () => {
        ipcRenderer.invoke('quit-app');
    });

    document.getElementById("btn-minimize").addEventListener('click', () => {
        ipcRenderer.invoke('min-app');
    });
});

electron.contextBridge.exposeInMainWorld('electron', {
    solve, // Expose the solve function
    scrape,// Expose the scrape function
    //socket_on, // Expose the socket_on function
    //socket_off // Expose the socket_off function
    register,
    login,
    removeUser,
    fav,
    getFav,
    removeFav
});


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
