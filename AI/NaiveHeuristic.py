from .Heuristic import Heuristic


class NaiveHeuristic(Heuristic):
    def heuristicCostCell(self, curri, currj, number):
        i, j = self.getGoalPosition(number)
        return 1 if i != curri or j != currj else 0
