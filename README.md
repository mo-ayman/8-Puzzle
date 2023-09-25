
<h1 align="center">8-Puzzle Solver</h1>


<p align="center">Using Informed and Uninformed Search Algorithms to Solve 8-Puzzle</p>
<br><br>
<p align="center">
    <img src="ai.png" alt="Calculator image">
</p>



Table of Contents
-----------------

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Algorithms](#algorithms)
- [License](#license)

About
-----

The 8-Puzzle is a popular sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one empty space. The goal is to rearrange the tiles to reach a specific configuration, usually the goal state:
<p align="center">
    <img src="https://th.bing.com/th/id/R.4cbd0d8dbc033c062dc4fe901b471839?rik=m37R6ArYQtn4Cg&riu=http%3a%2f%2f2.bp.blogspot.com%2f-gN0ZIkpNM08%2fTtPfeC1XgLI%2fAAAAAAAAABM%2fE8afLYPb1Vg%2fs1600%2feightpuzzle.png&ehk=h9G51VdUAZwEZM7DednHj1%2b01BBkmGkUbX9aW8bFYl8%3d&risl=&pid=ImgRaw&r=0" alt="Calculator image">
</p>


This repository provides a Python program that solves the 8-Puzzle using various search algorithms, allowing you to find the optimal solution or explore different strategies.

Getting Started
---------------

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mo-ayman/8-Puzzle.git
   ```
   
2. Navigate to the project directory:

   ```bash
   cd 8-Puzzle
   ```

3. Install the required packages (if not already installed):

   ```bash
   pip install -r requirements.txt
   ```

### Usage

To solve the 8-Puzzle, run the main script:

   ```bash
   python main.py
   ```


This will prompt you to select the search algorithm and provide the initial puzzle state. The program will then output the solution steps and the number of moves required to reach the goal state.

### Algorithms

This repository includes the following search algorithms for solving the 8-Puzzle:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search

Feel free to explore and compare these algorithms for solving the puzzle.


### License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/mo-ayman/8-Puzzle/blob/main/LICENSE) file for details.

