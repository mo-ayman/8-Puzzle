import abc


class Searcher(abc.ABC):
    def __init__(self):
        self.visited = set()
        self.__state_counter = 0

    @abc.abstractmethod
    def search(self, state):
        return None

    def print_state(self, state, should_print: bool = False):
        if should_print:
            self.__state_counter += 1
            print("State #" + str(self.__state_counter))
            print(state.get_grid()[0])
            print(state.get_grid()[1])
            print(state.get_grid()[2])
            print()

    def goal_test(self, state):
        return state.get_grid() == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
