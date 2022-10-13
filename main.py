from AI import State, GUI, DFS

initial_state = State()


def take_input():
    print("Enter the initial state of the grid")
    for i in range(3):
        initial_state.grid[i][0], initial_state.grid[i][1], initial_state.grid[i][2] = map(int, input().split())

    print("Enter the search algorithm")
    search_algo = input()


take_input()

DFS_search = DFS()
finishing_state = DFS_search.search(initial_state)

GUI = GUI(finishing_state)
GUI.run()
