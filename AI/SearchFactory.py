from AI import DFS,BFS,AStar,EuclideanHeuristic , ManhattanHeuristic
from AI.NaiveHeuristic import NaiveHeuristic


class SearchFactory:
    @staticmethod
    def get_search_algo(search_algo):
        if search_algo == '1':
            search = DFS()
        elif search_algo == '2':
            search = BFS()
        elif search_algo == '3':
            search = AStar(EuclideanHeuristic())
        elif search_algo == '4':
            search = AStar(ManhattanHeuristic())
        elif search_algo == '5':
            search = AStar(NaiveHeuristic())
        return search

