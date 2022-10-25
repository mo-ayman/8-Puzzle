from .Searcher import Searcher
from queue import PriorityQueue


class AStar(Searcher):
    """A* Class implementing the Searcher interface"""

    def __init__(self, Heuristic):
        super().__init__()
        self.__frontier = PriorityQueue()
        self.__visited = set()
        self.__heuristic = Heuristic  # inject heuristic class

    def search(self, initialState):
        """Implementation of the search algorithm according to pseudocode"""

        max_depth = 0  # max depth of the tree
        explored_states = 0
        uniqueIdentifier = 0  # unique ID to tie break priority queue
        self.__frontier.put(
            (
                self.__heuristic.heuristic_cost(initialState)
                + initialState.previous_cost,
                uniqueIdentifier,
                initialState,
            )
        )
        while not self.__frontier.empty():
            state = self.__frontier.get()[2]

            # Check that current state is not already visited
            current_grid_hash = state.get_hash()
            if current_grid_hash in self.__visited:
                continue

            self.print_state(state)
            explored_states += 1
            max_depth = max(max_depth, state.depth)

            self.__visited.add(state.get_hash())
            if super().goal_test(state):
                return state, explored_states, max_depth

            for neighbor in state.get_successor():
                grid_hash = neighbor.get_hash()
                if grid_hash not in self.__visited:
                    uniqueIdentifier += 1
                    self.__frontier.put(
                        (
                            self.__heuristic.heuristic_cost(neighbor)
                            + neighbor.previous_cost,
                            uniqueIdentifier,
                            neighbor,
                        )
                    )

        return None, None, None  # Return None in case of failure to find a solution