from AI import State, GUI
from AI.SearchFactory import SearchFactory
import time
import easygui

initial_state = State()


def take_input():
    inp = easygui.enterbox("Enter the initial state of the grid", "Initial State", "[0, 1, 2, 3, 4, 5, 6, 7, 8]")

    grid_1d = eval(inp)
    grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    for i in range(9):
        grid[i // 3][i % 3] = grid_1d[i]

    initial_state.set_grid(grid)

    algorithm = easygui.buttonbox("Select the search algorithm", "Searcher Selector",
                      ["DFS", "BFS", "A* Euclidean", "A* Manhattan", "A* Naive"])

    return algorithm


search_algo = take_input()
searcher = SearchFactory.get_search_algo(search_algo)
start_time = time.time()
finishing_state, nodes_expanded = searcher.search(initial_state)
end_time = time.time()
time_taken = 1000 * (end_time - start_time)
print(time_taken)

GUI = GUI(finishing_state, nodes_expanded, time_taken)
GUI.run()
