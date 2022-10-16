from AI import DFS,BFS,AStar,EuclideanHeuristic , ManhattanHeuristic


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
        return search

