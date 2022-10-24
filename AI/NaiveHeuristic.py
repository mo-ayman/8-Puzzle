from .Heuristic import Heuristic


class NaiveHeuristic(Heuristic):
    """Heuristic for A* Searcher implementing the Heuristic interface using a naive method
     by counting the number of cells in a wrong place"""

    def heuristicCostCell(self, curri, currj, number):
        i, j = self.getGoalPosition(number)
        return 1 if i != curri or j != currj else 0
