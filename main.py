from AI import State
from AI.SearchFactory import SearchFactory
import time
import easygui
import sys


def take_input(initial_state):
    """Takes the input state from the user in a dialog box and save it to initial_state,
    returns the selected search algorithm to be used in the next step of the program"""

    inp = easygui.enterbox(
        "Enter the initial state of the grid",
        "Initial State",
        "[0, 1, 2, 3, 4, 5, 6, 7, 8]",
    )

    grid_1d = eval(inp)  # eval usage is discouraged, a validation layer may be easily added
    grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    for i in range(9):
        grid[i // 3][i % 3] = grid_1d[i]

    initial_state.set_grid(grid)

    algorithm = easygui.buttonbox(
        "Select the search algorithm",
        "Searcher Selector",
        ["DFS", "BFS", "A* Euclidean", "A* Manhattan", "A* Naive"],
    )

    return algorithm


def main():
    from AI import GUI

    initial_state = State()

    search_algo = take_input(initial_state)
    searcher = SearchFactory.get_search_algo(search_algo)

    # Recording time
    start_time = time.time()
    finishing_state, nodes_expanded, max_depth = searcher.search(initial_state)
    end_time = time.time()

    time_taken = 1000 * (end_time - start_time)  # Converting from seconds to milliseconds

    if finishing_state is None:  # The searcher didn't find a solution
        easygui.msgbox(
            "This case is unsolvable!\nTime taken: " + str(time_taken) + " milliseconds",
            "Alert",
        )
        sys.exit(0)

    GUI = GUI(finishing_state, nodes_expanded, time_taken, max_depth)
    GUI.run()


if __name__ == "__main__":
    main()
