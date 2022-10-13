from .Searcher import Searcher
from queue import PriorityQueue
from .Heuristic import Heuristic
class AStar(Searcher):
    def __init__(self,Heuristic):
        super().__init__()
        self.__frontier = PriorityQueue()
        self.__visited = set()
        self.__heuristic = Heuristic

    def search(self, initialState):
        self.__frontier.put((self.__heuristic.heuristicCost+initialState.previous_cost,initialState))

        while not self.__frontier.empty():
            state = self.__frontier.get()

            if super().goal_test(state):
                return state

            for neighbor in state.get_successor():
                grid_hash = neighbor.get_hash()
                if grid_hash not in self.__visited:
                    self.__visited.add(grid_hash)
                    self.__frontier.put((self.__heuristic.heuristicCost+neighbor.previous_cost,neighbor))
                else:
                    pass
        return None

