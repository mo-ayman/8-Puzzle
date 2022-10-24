from .Heuristic import Heuristic


class ManhattanHeuristic(Heuristic):
    """Heuristic for A* Searcher implementing the Heuristic interface using manhattan distance formula"""

    def heuristicCostCell(self, curri, currj, number):
        i, j = self.getGoalPosition(number)
        return abs(curri - i) + abs(currj - j)

