from AI import DFS,BFS,AStar,EuclideanHeuristic , ManhattanHeuristic


class SearchFactory:
    @staticmethod
    def get_search_algo(search_algo):
        print(search_algo)
        if search_algo == 'DFS':
            search = DFS()
        elif search_algo == 'BFS':
            search = BFS()
        elif search_algo == 'A* Euclidean':
            search = AStar(EuclideanHeuristic())
        elif search_algo == 'A* Manhattan':
            search = AStar(ManhattanHeuristic())
        return search

