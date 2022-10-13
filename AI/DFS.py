from .Searcher import Searcher


class DFS(Searcher):
    def __init__(self):
        super().__init__()
        self.frontier = []

    def search(self, state):
        self.frontier.append(state)
        while len(self.frontier) > 0:
            state = self.frontier.pop()
            if state.grid in self.visited:
                continue
            else:
                self.visited.append(state.grid)

            if self.goalTest(state):
                return state
            for neighbour in state.get_successor():
                if neighbour.grid not in self.visited:
                    self.frontier.append(neighbour)
        return False
