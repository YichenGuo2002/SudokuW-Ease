<img width="50%" alt="Sudoku_w_ease_logo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/sudoku_logo.png?raw=true">

### Master Sudoku effortlessly with Sudoku W/ Ease App - the simplest way to solve Sudoku puzzles on your desktop!

Developed by [Yichen Guo](www.yichenguo.com).

Sudoku made effortless! Solve any puzzle, scrape online games, and create custom grids with Sudoku W/ Ease. Our advanced solver and scraper algorithms, including BeautifulSoup, constraint satisfaction, and depth-first search, make every puzzle a breeze. Built with Electron, VueJS, SQLite, Flask, and Tailwind CSS for a seamless desktop experience.

## Table of Contents
- [Product Background](#project-background)
- [App Usage](#app-usage)
- [Technology](#technology)
- [Product Architecture](#product-architecture)
- [Incoming Features](#incoming-features)
- [Acknowledgement](#acknowledgement)
- [Lab Doc](#lab-doc)

### Project Background
Are you ...

> - A Sudoku enthusiast who enjoys solving puzzles of varying sizes, including custom puzzles you create yourself. You are looking for a desktop app that is easy to use and allows you to scrape online puzzles and create your own grids.<br>

> - A casual Sudoku player who is struggling to solve a particularly challenging puzzle. You are looking for an app that can help you solve the puzzle quickly and easily, and are interested in finding the most advanced Sudoku solver algorithms.

I created the project out of a desire for an all-in-one solution for Sudoku lovers like myself. With this desktop app, you can access puzzles from all your favorite newspapers and websites, all in one place. Plus, the advanced solver algorithm can solve even the most challenging puzzles in seconds. Try the ***Sudoku W/ Ease*** app today!

### App Usage
 - Sudoku Solving

 	This app includes a user-friendly Sudoku board interface to display puzzles of various sizes, including 4×4, 9×9, 16×16, and 25×25. The "Solve" button below initiates backend API calls to Python Flask endpoints, providing fast and accurate solutions in milliseconds. Users can also dynamically modify the puzzle by inputting values into empty boxes and check their solutions for accuracy. 

	<img width="75%" alt="Sudoku_w_ease_home_demo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/home_demo.png?raw=true">

 - Online Puzzles

 	This app uses BeautifulSoup web scrapping tools to extract random/daily Sudokus from many online sources, each with varying difficulty levels. Some are easy, some are so hard that takes 40+ seconds for the most advanced solver algorithm to handle. Users can choose from a wide range of sources and click on a button to pull puzzles from that source, making it easy to find the perfect Sudoku challenge. 

	<img width="75%" alt="Sudoku_w_ease_find_demo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/find_demo.png?raw=true">

 - Upload puzzles

 	This app enables user upload of custome Sudoku puzzles. It analyzes the Sudoku and offers instant solution.

	<img width="75%" alt="Sudoku_w_ease_upload_demo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/upload_demo.png?raw=true">

 - Optimal Algorithm

 	This app introduces a variety of published Sudoku algorithms, each with their own strengths and weaknesses. Here is a brief introduction about what constraint satisfaction and depth-first search are and how they are utilized in this program.

Isn't that cool? Just go out and have fun without worrying about the plans!


### Technology
- JavaScript, Typescript
- Python
- Electron
- VueJS
- PostgreSQL, SQLAlchemy, psycopg2
- Flask
- GraphQL, Graphene, WebSockets
- BeautifulSoup, Selenium
- Fetch APIs
- Tailwind CSS
- HTML & CSS

### Product Architecture

- Project Structures

	The front end of this project is built using the Electron-vue framework. The main process is initiated by the [background.js](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/background.js) file, which loads the [preload.js](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/preload.js) file containing Fetch APIs for exchanging JSON-formatted data with the back end. These API functions are exposed to Vue components through Vue ContextBridge.

	The back end of this project is built on the Python framework, with a [Flask server](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/scripts/app.py) connected to the BeautifulSoup and Selenium [web scraping algorithm](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/scripts/scrape.py) and the [AI Sudoku solver algorithm](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/scripts/sudoku.py). When requests are received, the Flask server sends the result back to the front-end. We are also working on connecting the back-end Flask to SQLite to allow users to save their favorite Sudoku puzzles.

	<img width="100%" alt="Project Structure" src="./doc/system%20design.png">

 - Front-Back Integration

	The two ends are connected via [GraphQL](./scripts/app.py) API endpoints. Based on Graphene and WebSocket, the APIs enable a secured user system, efficient Sudoku solving and scraping, and realtime updates. You can find a list of frontend requests and the corresponding backend functions here.

	<img width="70%" alt="GraphQL Requests" src="./doc/graphql%20requests.png">

 - Database Design

	The back end is connected to PostgreSQL database. It contains two tables, one for saving user accounts and the other for saving users' favorite Sudokus. The database schema is designed for the purpose of a secured user system, so certain restrictions are applied to some fields to ensure valid input.

	<img width="80%" alt="User Database Design" src="./doc/user%20table.png">
	<img width="60%" alt="Sudoku Database Design" src="./doc/sudoku%20table.png">

 - User System Pathways

	The user system is set up with multiple error handling functions to send accurate error description if any step of the pipeline breaks down. The "save" Sudoku feature is connected to Pinia global store to ensure a smooth experience for both logged-in and non-logged-in users.

	<img width="100%" alt="User Database Design" src="./doc/user%20paths.png">
	<img width="80%" alt="Sudoku Database Design" src="./doc/save%20paths.png">

 - Error Handling

	Coming up.

Overall, this project utilizes a client-server architecture with a multi-tier structure. Each tier has separated functionalities, helping to increase the scalability and flexibility of the project.

### Incoming Features
- In Progress: Connect Python Flask server to SQLite to save users' favorite puzzles.
- In Progress: Use Selenium to scrape Javascript-loaded content from sites like LA Times.

### Acknowledgement

Thanks to [The Assembly's](https://www.youtube.com/watch?v=GX4c13SSBrs&list=WL&index=4&ab_channel=TheAssembly) and [Peter Novig](http://norvig.com/sudoku.html)'s Sudoku Algorithms, and [澁谷直樹](https://kikaben.com/)'s tech blog. I was able to learn a lot about traditional Sudoku algorithms.

### Lab Doc

1. [Lab1 - RESTful API vs GraphQL](./doc/SudokuW_Ease%20Lab%201%20RESTful%20API%20vs%20GraphQL.pdf)
2. [Lab2 - Web Socket & Database Design](./doc/SudokuW_Ease%20Lab%202%20Web%20Socket%20%26%20Database%20Design.pdf)

### Cheatsheet:
1. [Emojicode cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet)
2. Git command
```
git pull //sync local repo
```
3. Sample request query: 
```
mutation SolveSudoku{
  solveSudoku(
		sudoku: [0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0],
		size: 9
	) 
	{
   solution,
	 time
  }
}

mutation ScrapeSudoku{
  scrapeSudoku(
		index: 6
	) 
	{
   sudoku,
		size,
		difficulty
  }
}

mutation Register{
  register(
		email:"****@***",
		password:"***",
		name:"***"
	)
	{
   user{
		id,
		email,
		name
		}
  }
}

mutation Login{
  login(
		email:"****@***",
		password:"***"
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

mutation RemoveUser{
  removeUser(
		userId: 1,
	)
	{
   success
	}
}

mutation Fav{
  fav(
		sudoku:[1,2,3],
		userId: 1,
	)
	{
   success
	}
}


mutation GetFav{
  getFav(
		userId:1
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

mutation RemoveFav{
  removeFav(
		userId:2,
		sudokuId:1
	)
	{
   success
	}
}

```
4. Create PostgreSQL models:
Go to python shell by running python and return:
```
from app import app, db
with app.app_context():
    db.create_all()
exit()
# Only need to run this once.
```
