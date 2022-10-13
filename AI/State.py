from copy import deepcopy


class State(object):
    def __init__(self):
        self.previousState = None
        self.previousCost = 0
        self.grid = [[0]*3 for i in range(3)]

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    return i, j
        raise LookupError

    def get_next_state(self, x1: int, y1: int, x2: int, y2: int):
        new_state = State()
        new_state.previousState = self
        new_state.grid = deepcopy(self.grid)
        new_state.grid[x1][y1] = self.grid[x2][y2]
        new_state.grid[x2][y2] = self.grid[x1][y1]
        new_state.previousCost = self.previousCost + 1

        return new_state

    def get_successor(self) -> list:
        successors = []

        x, y = self.find_empty()
        if x < 2:
            successors.append(self.get_next_state(x, y, x + 1, y))
        if x > 0:
            successors.append(self.get_next_state(x, y, x - 1, y))
        if y < 2:
            successors.append(self.get_next_state(x, y, x, y + 1))
        if y > 0:
            successors.append(self.get_next_state(x, y, x, y - 1))

        return successors

