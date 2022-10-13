from .Heuristic import Heuristic


class EuclideanHeuristic(Heuristic):
    def estimateCost(self, curri,currj,number):
        i,j = self.getGoalPosition(curri,currj,number)
        return ( (curri-i)**2 +(currj-j)**2 )**0.5



