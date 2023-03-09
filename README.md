<img width="50%" alt="Sudoku_w_ease_logo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/sudoku_logo.png?raw=true">

### Master Sudoku effortlessly with Sudoku W/ Ease CLI - the simplest way to solve Sudoku puzzles on your desktop!

Developed by [Yichen Guo](www.yichenguo.com).

Sudoku made effortless! Solve any puzzle, scrape online games, and create custom grids with Sudoku W/ Ease CLI. Our advanced solver and scraper algorithms, including BeautifulSoup, constraint satisfaction, and depth-first search, make every puzzle a breeze. Built with Electron, VueJS, SQLite, Flask, and Tailwind CSS for a seamless desktop experience.

## Table of Contents
- [Product Background](#project-background)
- [App Usage](#app-usage)
- [Technology](#technology)
- [Product Architecture](#product-architecture)
- [Incoming Features](#incoming-features)
- [Acknowledgement](#acknowledgement)

### Project Background
Are you ...

> - A Sudoku enthusiast who enjoys solving puzzles of varying sizes, including custom puzzles you create yourself. You are looking for a desktop app that is easy to use and allows you to scrape online puzzles and create your own grids.<br>

> - A casual Sudoku player who is struggling to solve a particularly challenging puzzle. You are looking for an app that can help you solve the puzzle quickly and easily, and are interested in finding the most advanced Sudoku solver algorithms.

I created the project out of a desire for an all-in-one solution for Sudoku lovers like myself. With this desktop app, you can access puzzles from all your favorite newspapers and websites, all in one place. Plus, the advanced solver algorithm can solve even the most challenging puzzles in seconds. Try the ***Sudoku W/ Ease*** app today!

### App Usage
 - Sudoku Solving

 This CLI includes a user-friendly Sudoku board interface to display puzzles of various sizes, including 4×4, 9×9, 16×16, and 25×25. The "Solve" button below initiates backend API calls to Python Flask endpoints, providing fast and accurate solutions in milliseconds. Users can also dynamically modify the puzzle by inputting values into empty boxes and check their solutions for accuracy. 

<img width="75%" alt="Sudoku_w_ease_home_demo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/home_demo.png?raw=true">

 - Online Puzzles

 This CLI uses BeautifulSoup web scrapping tools to extract random/daily Sudokus from many online sources, each with varying difficulty levels. Some are easy, some are so hard that takes 40+ seconds for the most advanced solver algorithm to handle. Users can choose from a wide range of sources and click on a button to pull puzzles from that source, making it easy to find the perfect Sudoku challenge. 

<img width="75%" alt="Sudoku_w_ease_find_demo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/find_demo.png?raw=true">

 - Upload puzzles

 This CLI enables user upload of custome Sudoku puzzles. It analyzes the Sudoku and offers instant solution.

<img width="75%" alt="Sudoku_w_ease_upload_demo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/upload_demo.png?raw=true">

 - Optimal Algorithm

 This CLI introduces a variety of published Sudoku algorithms, each with their own strengths and weaknesses. Here is a brief introduction about what constraint satisfaction and depth-first search are and how they are utilized in this program.

Isn't that cool? Just go out and have fun without worrying about the plans!


### Technology
- JavaScript
- Python
- Electron
- VueJS
- SQLite
- Flask
- BeautifulSoup
- Fetch API
- Tailwind CSS
- HTML & CSS

### Product Architecture

- Project Structures
<img width="75%" alt="Project Structure" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/architecture_demo.jpg?raw=truehttps://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/architecture_demo.jpg?raw=true">

### Incoming Features
- In Progress: Connect Python Flask server to SQLite to save users' favorite puzzles.
- In Progress: Use Selenium to scrape Javascript-loaded content from sites like LA Times.

### Acknowledgement

Thanks to [The Assembly's](https://www.youtube.com/watch?v=GX4c13SSBrs&list=WL&index=4&ab_channel=TheAssembly) and [Peter Novig](http://norvig.com/sudoku.html)'s Sudoku Algorithms, and [澁谷直樹](https://kikaben.com/)'s tech blog. I was able to learn a lot about traditional Sudoku algorithms.

