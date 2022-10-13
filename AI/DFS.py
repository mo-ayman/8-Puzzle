from Searcher import Searcher


class DFS(Searcher):
    def __init__(self):
        super().__init__()
        self.frontier = []

    def search(self, state):
        self.frontier.append(state)
        while len(self.frontier) > 0:
            state = self.frontier.pop()
            if state not in self.visited:
                self.visited.append(state)

            if self.goalTest(state):
                return state
            for neighbour in state.get_successor():
                if neighbour not in self.frontier and neighbour not in self.visited:
                    self.frontier.append(neighbour)
        return False
