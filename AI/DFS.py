from .Searcher import Searcher
from queue import LifoQueue


class DFS(Searcher):
    def __init__(self):
        super().__init__()
        self.__frontier = LifoQueue()

    def search(self, initialState):
        self.__frontier.put(initialState)
        self.visited.add(initialState.get_hash())

        while not self.__frontier.empty():
            state = self.__frontier.get()

            if super().goal_test(state):
                return state

            for neighbor in state.get_successor():
                grid_hash = neighbor.get_hash()
                if grid_hash not in self.visited:
                    self.visited.add(grid_hash)
                    self.__frontier.put(neighbor)
        return None
"""
6 7 8
3 2 1
0 5 4

"""