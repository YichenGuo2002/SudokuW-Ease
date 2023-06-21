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
- PostgreSQL
- Flask
- GraphQL, Graphene
- BeautifulSoup
- Fetch API
- Tailwind CSS
- HTML & CSS

### Product Architecture

- Project Structures

The front-end of this project is built using the Electron-vue framework. The main process is initiated by the [background.js](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/background.js) file, which loads the [preload.js](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/preload.js) file containing Fetch APIs for exchanging JSON-formatted data with the back-end. These API functions are exposed to Vue components through IPC.

The back-end of this project is built on the Python framework, with a [Flask server](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/scripts/app.py) connected to the BeautifulSoup [web scraping algorithm](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/scripts/scrape.py) and the [AI Sudoku solver algorithm](https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/scripts/sudoku.py). When requests are received, the Flask server sends the result back to the front-end. We are also working on connecting the back-end Flask to SQLite to allow users to save their favorite Sudoku puzzles.

<img width="100%" alt="Project Structure" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/architecture_demo.jpg?raw=truehttps://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/architecture_demo.jpg?raw=true">

Overall, this project utilizes a client-server architecture with a multi-tier structure. Each tier has separated functionalities, helping to increase the scalability and flexibility of the project.

### Incoming Features
- In Progress: Connect Python Flask server to SQLite to save users' favorite puzzles.
- In Progress: Use Selenium to scrape Javascript-loaded content from sites like LA Times.

#### Development Progress:
**2023 Summer**: 
- [ ] Finish current features; 
- [x] Refactor RESTful APIs to GraphQL APIs; 
- [ ] Connect to PostgreSQL; 
- [ ] Set up CI/CD pipeline;
- [ ] Improve performance: Vue takes a lot of load time;
- [ ] Optimize system error handling;
- [ ] Convert Javascript to Typescript.

- (06/07/23): Made plans for the project and decided tech stack to use. :notebook_with_decorative_cover:
- (06/08/23): Restructured and revisited existing code. Changed the font to Roboto. :facepalm:
- (06/09/23): Changed background color. Removed border line to improve aesthetics.

*Summer Week 4/10 Plan: Finish the About page. Adapt application to GraphQL:heavy_check_mark:. Implement GraphQL realtime updates.*
- (06/12/23): Changed button color. Added border line to each box. Optimized button styling by clustering inline CSS rules to external style sheets. Set up styling for About page. :pleading_face:
- (06/13/23): Learned about GraphQL. Decided to refactor existing Flask RESTful API to GraphQL + Graphene and connect to PostgreSQL database.     Finished reconstructing a GraphQL+Graphene+Flask backend API system, and examined through Insomia. Set up frontend fetch API GraphQL request query. Found problem in system error handling. :cowboy_hat_face:
- (06/14/23): Tested speed of RESTful API and GraphQL. Wrote [lab doc for examining the pros and cons of using GraphQL](./doc/SudokuW_Ease%20Lab%201%20RESTful%20API%20vs%20GraphQL.pdf). Planned to implement GraphQL realtime updates.

*Summer Week 5/10 Plan: Implement GraphQL realtime updates. Set up user system. Connect Application to PostgreSQL. Part I.*
- (06/20/23): Set up web socket environment for realtime backend update. Still learning the concepts of web sockets. It is hard so took some time. Hope I can get through it!

*Summer Week 6/10 Plan: Set up user system. Connect Application to PostgreSQL. Part II.*

*Summer Week 7/10 Plan: Packaging. Set up CI/CD Pipeline.*

*Summer Week 8/10 Plan: Improve performance: Reduce latency.*

*Summer Week 9/10 Plan: (tbd) Secure application delivery using AWS AppStream 2.0. Part I*

*Summer Week 10/10 Plan: (tbd) Secure application delivery using AWS AppStream 2.0. Prepare for final showcase. Part II*

*Summer after 10-Week Plan: App announced in my personal portfolio and showcased via Youtube.*

*Summer if possible: Convert Javascript to Typescript*

### Acknowledgement

Thanks to [The Assembly's](https://www.youtube.com/watch?v=GX4c13SSBrs&list=WL&index=4&ab_channel=TheAssembly) and [Peter Novig](http://norvig.com/sudoku.html)'s Sudoku Algorithms, and [澁谷直樹](https://kikaben.com/)'s tech blog. I was able to learn a lot about traditional Sudoku algorithms.

### Lab Doc

1. [Lab1 - RESTful API vs GraphQL](./doc/SudokuW_Ease%20Lab%201%20RESTful%20API%20vs%20GraphQL.pdf)

### Git Cheatsheet:
[Emojicode](https://github.com/ikatyang/emoji-cheat-sheet) //cheatsheet
```

git pull //sync local repo
```