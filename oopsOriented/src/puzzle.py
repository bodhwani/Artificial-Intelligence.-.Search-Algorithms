from src.board import Board
from src.solver import BFS, DFS, AST, IDA


class Puzzle:
    def __init__(self, tiles: str, algorithm: str):
        # tiles = 0,1,2,3.... ,algorithm = bfs
        self._tiles = tiles
        print("Tiles are ",tiles)
        self._algorithm = algorithm
        self._board = Board(tiles=tiles)
        print("Self._board is ",self._board)
        self._algorithms = {
            'bfs': BFS(self._board),
            'dfs': DFS(self._board),
            'ast': AST(self._board),
            # 'ida': IDA(self._board)
        }
        self._solver = self._algorithms[self._algorithm]
        print("self._solver is",self._solver)

        self._results = None

    def solve(self):
        print("---1Solve----")
        self._results = self._solver.solve()
        print("---2Result----")
        print(self._results)
        return self._results

    @property
    def actions(self):
        print("Actions----")
        return self._results.actions

    @property
    def path_cost(self):
        return self._results.path_cost

    @property
    def nodes_expanded(self):
        return self._solver.nodes_expanded

    @property
    def fringe_size(self):
        return self._solver.fringe_size

    @property
    def max_fringe_size(self):
        return self._solver.max_fringe_size

    @property
    def search_depth(self):
        return self._solver.search_depth

    @property
    def max_search_depth(self):
        return self._solver.max_search_depth

    @property
    def running_time(self):
        return self._solver.running_time
