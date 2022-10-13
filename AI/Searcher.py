class Searcher(object):
    def __init__(self):
        self.__visited = None
        self.final_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def search(self, state):
        return None

    def goal_test(self, state):
        for i in range(3):
            for j in range(3):
                if self.final_state[i][j] is not state.grid[i][j]:
                    return False
        return True
