from .Searcher import Searcher
from queue import Queue


class BFS(Searcher):
    def __init__(self):
        super().__init__()
        self.__frontier = Queue()
        self.__visited = set()

    def search(self, initialState):
        self.__frontier.put(initialState)

        while not self.__frontier.empty():
            state = self.__frontier.get()

            if super().goal_test(state):
                return state

            for neighbor in state.get_successor():
                grid_hash = neighbor.get_hash()
                if grid_hash not in self.__visited:
                    self.__visited.add(grid_hash)
                    self.__frontier.put(neighbor)
        return None
