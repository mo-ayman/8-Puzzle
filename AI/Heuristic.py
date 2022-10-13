import abc
class Heuristic(object):

    @abc.abstractmethod
    def heuristicCost(self, curri,currj,number):
        return 0


    def getGoalPosition(state,number):
        i=number % 3
        j=number-3*i
        return i,j
