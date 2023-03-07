<img width="50%" alt="Sudoku_w_ease_logo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/sudoku_logo.png?raw=true">

### Master Sudoku effortlessly with Sudoku W/ Ease CLI - the simplest way to solve Sudoku puzzles on your desktop!

Sudoku made effortless! Solve any puzzle, scrape online games, and create custom grids with Sudoku W/ Ease CLI. Our advanced solver and scraper algorithms, including BeautifulSoup, constraint satisfaction, and depth-first search, make every puzzle a breeze. Built with Electron, VueJS, SQLite, Flask, and Tailwind CSS for a seamless desktop experience.

<img width="75%" alt="Sudoku_w_ease_demo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/demo.png?raw=true">

## Table of Contents
- [Product Background](#project-background)
- [App Usage](#app-usage)
- [Technology](#technology)
- [Product Modules](#product-modules)
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

<img width="75%" alt="Sudoku_w_ease_home_demo" src="image.png">

 - Online Puzzles
 This CLI uses BeautifulSoup web scrapping tools to extract random/daily Sudokus from many online sources, each with varying difficulty levels. Some are easy, some are so hard that takes 40+ seconds for the most advanced solver algorithm to handle. Users can choose from a wide range of sources and click on a button to pull puzzles from that source, making it easy to find the perfect Sudoku challenge. 

<img width="75%" alt="Sudoku_w_ease_find_demo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/find_demo.png?raw=true">

 - Upload puzzles
 This CLI enables user upload of custome Sudoku puzzles. It analyzes the Sudoku and offers instant solution.

<img width="75%" alt="Sudoku_w_ease_upload_demo" src="https://github.com/YichenGuo2002/SudokuW-Ease/blob/main/src/assets/upload_demo.png?raw=true">

 - Optimal Algorithm
 This CLI introduces a variety of published Sudoku algorithms, each with their own strengths and weaknesses. Here is a brief introduction about what constraint satisfaction and depth-first search are and how they are utilized in this program.

<br>Isn't that cool? Just go out and have fun without worrying about the plans!


### Technology
- JavaScript
- Node.js (16.15.0)
- ReactJS
- Azure Serverless Functions
- Azure Cosmos DB
- Azure Blob Storage
- HTML & CSS
- Bootstrap 4

### Product Modules

- Project Structures
<img width="75%" alt="Project Structure" src="https://user-images.githubusercontent.com/60641853/192036975-25612012-1948-400f-9cfa-87672155e0ff.png">

- [Google Places API](/api/googleplaces)
<br>The Google Places API is built on the basis of Google Map's FindPlace and NearbySearch APIs. It serves the app by generating random tourist attractions based upon user inputs and output to the JS functions.
<img width="75%" alt="Google_Places API" src="https://user-images.githubusercontent.com/60641853/192037555-4697a83c-f6ec-4ba9-8922-c243b24c373a.png">


- [Route Calculations API](/api/route_calculation)
<br>The Route Calculations API is established upon a solution for the famous Travelling Salesman Problem. It serves the app by creating graph of multiple destinations and calculating the shortest route to travel through all of them, which is the final trip plan shown to the users.
<img width="75%" alt="Route_Calculation API" src="https://user-images.githubusercontent.com/60641853/192040987-344f312f-6acc-4dd6-bc31-c9da02951bb9.png">


### Incoming Features
- User Login functions for users to save their favorite trip or attraction
- Pictures & Introductions for each output attraction
- Update Google Places API algorithm to expand attraction dataset
- Connect input textfield with Google Map to improve location accuracy


### Acknowledgement
Thanks to Bit Project's Serverless Camp and Mentorship Program, I was able to successfully build the first version of this product. Especially, I would like to thank my mentor @Anthony Chu for offering me so much guidance and experience. 

For the Google Places API, I would like to thank Google for providing open-source Map API. For the Route Calculations API, I would love to thank Steven & Felix Halim, William Fiset, and Micah Stairs for their [Java solution](https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/graphtheory/TspDynamicProgrammingRecursive.java#L2) of Travelling Salesman Problem.

