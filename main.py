from AI import State, GUI
from AI.SearchFactory import SearchFactory
import time

initial_state = State()


def take_input():
    print("Enter the initial state of the grid")
    grid = [[0] * 3 for _ in range(3)]
    for i in range(3):
        grid[i][0], grid[i][1], grid[i][2] = map(int, input().split())
    initial_state.set_grid(grid)
    print("Enter the number corresponding to search algorithm:\n"
          "1.DFS\n"
          "2.BFS\n"
          "3.AStar Euclidean\n"
          "4.AStar Manhattan\n"
          "5.Naive Heuristic")
    algo = input()
    return algo


search_algo = take_input()
searcher = SearchFactory.get_search_algo(search_algo)
start_time = time.time()
finishing_state, nodes_expanded = searcher.search(initial_state)
end_time = time.time()
time_taken = 1000 * (end_time - start_time)
print(time_taken)

GUI = GUI(finishing_state, nodes_expanded, time_taken)
GUI.run()
