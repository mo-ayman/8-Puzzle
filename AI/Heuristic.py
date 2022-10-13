import abc
class Heuristic(object):

    def heuristic_cost(self,state):
        cost = 0
        for curri in range(3):
            for currj in range(3):
                cost += self.heuristicCostCell(curri,currj,state.grid[curri][currj])
        return cost

    @abc.abstractmethod
    def heuristicCostCell(self, curri,currj,number):
        pass
    def getGoalPosition(self,number):
        i=number % 3
        j=number-3*i
        return i,j
