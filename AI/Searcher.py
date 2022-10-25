import abc

from AI import State


class Searcher(abc.ABC):
    """Interface for any Search algorithm"""

    def __init__(self):
        self.visited = set()
        self.__state_counter = 0

    @abc.abstractmethod
    def search(self, state):
        return None

    def print_state(self, state: State, should_print: bool = False) -> None:
        """
        Print all expanded states to the console if should_print is True

        :param state: State to be printed
        :param should_print: Indicator whether the grid is supposed to be printed to console
        :return: None
        """

        if should_print:
            self.__state_counter += 1
            print("State #" + str(self.__state_counter))
            print(state.get_grid()[0])
            print(state.get_grid()[1])
            print(state.get_grid()[2])
            print()

    def goal_test(self, state: State) -> bool:
        return state.get_grid() == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
