import abc


class Searcher(abc.ABC):
    def __init__(self):
        self.visited = set()

    @abc.abstractmethod
    def search(self, state):
        return None

    def goal_test(self, state):
        return state.get_grid() == [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
