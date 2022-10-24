import math
from copy import deepcopy


class State(object):
    def __init__(self):
        self.previous_state = None
        self.previous_cost = 0
        self.grid_int= 0
        self.depth = 0

    def find_empty(self):
        grid=self.get_grid()
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    return i, j
        raise LookupError

    def get_grid(self):
        grid = [[0] * 3 for _ in range(3)]
        grid_string=str(self.grid_int)
        if len(grid_string)==8:
            grid_string='0'+grid_string

        for i in range(3):
            for j in range(3):
                grid[i][j]=int(grid_string[i*3+j])
        return grid

    def set_grid(self,grid):
        self.grid_int=0
        for i in range(len(grid[0])):
            for j in range(len(grid[i])):
                self.grid_int=self.grid_int+grid[i][j]*(10**(8-(i*3+j)))



    def get_next_state(self, x1: int, y1: int, x2: int, y2: int):
        new_state = State()
        new_state.previous_state = self
        grid=deepcopy(self.get_grid())
        temp=grid[x1][y1]
        grid[x1][y1]=grid[x2][y2]
        grid[x2][y2]=temp
        new_state.set_grid(grid)
        new_state.previous_cost = self.previous_cost + 1
        new_state.depth = self.depth + 1

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

    def get_hash(self):
        grid=self.get_grid()
        return hash(tuple(grid[0] + grid[1] + grid[2]))


