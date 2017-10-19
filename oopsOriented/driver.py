from argparse import ArgumentParser
from resource import getrusage, RUSAGE_SELF

from src.puzzle import Puzzle

if __name__ == "__main__":
    try:
        parser = ArgumentParser()
        parser.add_argument("solver", help="algorithm (bfs | dfs)")
        parser.add_argument("board", help="board string (0,1,2,3...)")
        args = parser.parse_args()
        print("Args are",args)
        #Args are Namespace(board='1,2,5,3,4,0,6,7,8', solver='bfs')

        puzzle = Puzzle(tiles=args.board, algorithm=args.solver)
        results = puzzle.solve()
        print ("results are",results)
        # with open('output.txt', 'w+') as f:
        #     f.write(f"path_to_goal: {puzzle.actions}\n")
        #     f.write("cost_of_path: {puzzle.path_cost}\n")
        #     f.write("nodes_expanded: {puzzle.nodes_expanded}\n")
        #     f.write("fringe_size: {puzzle.fringe_size}\n")
        #     f.write("max_fringe_size: {puzzle.max_fringe_size}\n")
        #     f.write("search_depth: {puzzle.search_depth}\n")
        #     f.write("max_search_depth: {puzzle.max_search_depth}\n")
        #     f.write("running_time: {puzzle.running_time}\n")
        #     f.write("max_ram_usage: {getrusage(RUSAGE_SELF)[2]/(1024**2)}\n")
    except TypeError as e:
        print(e)
        exit(1)
    except RuntimeError as e:
        print(e)
        exit(1)
