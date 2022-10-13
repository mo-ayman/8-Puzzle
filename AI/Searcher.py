import abc


class Searcher(abc.ABC):
    def __init__(self):
        self.visited = []

    @abc.abstractmethod
    def search(self, state):
        return None

    def goalTest(self, state):
        return state.grid == [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
