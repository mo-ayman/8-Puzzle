from .Heuristic import Heuristic


class ManhattanHeuristic(Heuristic):
    def estimateCost(self, curri,currj,number):
        i,j = self.getGoalPosition(curri,currj,number)
        return abs(curri-i)+abs(currj-j)



