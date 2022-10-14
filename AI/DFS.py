from .Searcher import Searcher
from queue import LifoQueue


class DFS(Searcher):
    def __init__(self):
        super().__init__()
        self.__frontier = LifoQueue()
        self.__frontier_set = set()

    def search(self, initial_state):
        self.__frontier.put(initial_state)
        self.__frontier_set.add(initial_state.get_hash())

        while not self.__frontier.empty():
            state = self.__frontier.get()
            self.__frontier_set.remove(state.get_hash())
            self.visited.add(state.get_hash())

            if super().goal_test(state):
                return state

            for neighbor in state.get_successor():
                grid_hash = neighbor.get_hash()
                if grid_hash not in self.visited and grid_hash not in self.__frontier_set:
                    self.__frontier.put(neighbor)
                    self.__frontier_set.add(grid_hash)
        return None
"""
6 7 8
3 2 1
0 5 4

"""