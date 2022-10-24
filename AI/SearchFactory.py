from AI import DFS, BFS, AStar, EuclideanHeuristic, ManhattanHeuristic
from AI.NaiveHeuristic import NaiveHeuristic


class SearchFactory:
    @staticmethod
    def get_search_algo(search_algo):
        if search_algo == "1" or search_algo == "DFS":
            search = DFS()
        elif search_algo == "2" or search_algo == "BFS":
            search = BFS()
        elif search_algo == "3" or search_algo == "A* Euclidean":
            search = AStar(EuclideanHeuristic())
        elif search_algo == "4" or search_algo == "A* Manhattan":
            search = AStar(ManhattanHeuristic())
        elif search_algo == "5" or search_algo == "A* Naive":
            search = AStar(NaiveHeuristic())
        return search
