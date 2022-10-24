from .Searcher import Searcher
from queue import PriorityQueue


class AStar(Searcher):
    def __init__(self, Heuristic):
        super().__init__()
        self.__frontier = PriorityQueue()
        self.__visited = set()
        self.__heuristic = Heuristic

    def search(self, initialState):
        max_depth = 0
        explored_states = 0
        self.__frontier.put(
            (
                self.__heuristic.heuristic_cost(initialState)
                + initialState.previous_cost,
                explored_states,
                initialState,
            )
        )
        while not self.__frontier.empty():
            state = self.__frontier.get()[2]
            self.print_state(state)
            explored_states += 1
            max_depth = max(max_depth, state.depth)

            self.__visited.add(state.get_hash())
            if super().goal_test(state):
                return state, explored_states, max_depth

            for neighbor in state.get_successor():
                grid_hash = neighbor.get_hash()
                if grid_hash not in self.__visited:
                    self.__frontier.put(
                        (
                            self.__heuristic.heuristic_cost(neighbor)
                            + neighbor.previous_cost,
                            explored_states,
                            neighbor,
                        )
                    )
                else:
                    pass
        return None, None, None
