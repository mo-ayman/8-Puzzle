from AI import State, GUI

initial_state = State()


def take_input():
    print("Enter the initial state of the grid")
    for i in range(3):
        initial_state.grid[i][0], initial_state.grid[i][1], initial_state.grid[i][2] = map(int, input().split())

    print("Enter the search algorithm")
    search_algo = input()


take_input()
GUI = GUI(initial_state.get_successor()[0].get_successor()[0])
GUI.run()
