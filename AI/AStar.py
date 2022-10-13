from .Searcher import Searcher


class AStar(Searcher):
    def __init__(self):
        self.__frontier = None
        self.__heuristic = None

