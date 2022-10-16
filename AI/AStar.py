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
        stateExplored=1
        self.__frontier.put((self.__heuristic.heuristic_cost(initialState)+initialState.previous_cost,stateExplored,initialState))
        self.__visited.add(initialState.get_hash());
        while not self.__frontier.empty():
            state = self.__frontier.get()[2]

            if super().goal_test(state):
                return state

            for neighbor in state.get_successor():
                grid_hash = neighbor.get_hash()
                if grid_hash not in self.__visited:
                    self.__visited.add(grid_hash)
                    stateExplored+=1
                    self.__frontier.put((self.__heuristic.heuristic_cost(neighbor)+neighbor.previous_cost,stateExplored,neighbor))
                else:
                    pass
        return None

