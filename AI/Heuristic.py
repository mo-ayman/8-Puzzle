import abc


class Heuristic(object):
    """Interface for any Heuristic algorithm to be used in the A* Search"""

    def heuristic_cost(self, state):
        """Computes the heuristic value for the whole state using the heuristic value for each cell"""

        cost = 0
        grid = state.get_grid()
        for curri in range(3):
            for currj in range(3):
                if grid[curri][currj] != 0:
                    cost += self.heuristicCostCell(curri, currj, grid[curri][currj])
        return cost

    @abc.abstractmethod
    def heuristicCostCell(self, curri, currj, number):
        pass

    def getGoalPosition(self, number):
        i = number // 3
        j = number % 3
        return i, j
