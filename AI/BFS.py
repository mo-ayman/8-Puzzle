from .Searcher import Searcher
from queue import Queue


class BFS(Searcher):
    def __init__(self):
        super().__init__()
        self.__frontier = Queue()

    def search(self, initialState):
        self.__frontier.put(initialState)
        self.visited.add(initialState.get_hash())

        explored_states = 0
        while not self.__frontier.empty():
            state = self.__frontier.get()
            explored_states += 1

            if super().goal_test(state):
                return state, explored_states

            for neighbor in state.get_successor():
                grid_hash = neighbor.get_hash()
                if grid_hash not in self.visited:
                    self.visited.add(grid_hash)
                    self.__frontier.put(neighbor)
        return None
