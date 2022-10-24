from .Heuristic import Heuristic


class EuclideanHeuristic(Heuristic):
    def heuristicCostCell(self, curri, currj, number):
        i, j = self.getGoalPosition(number)
        return ((curri - i) ** 2 + (currj - j) ** 2) ** 0.5
