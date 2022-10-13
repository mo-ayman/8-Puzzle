from .Heuristic import Heuristic


class ManhattanHeuristic(Heuristic):
    def heuristicCostCell(self, curri,currj,number):
        i,j = self.getGoalPositio(number)
        return abs(curri-i)+ abs(currj-j)

    pass

