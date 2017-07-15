# Introduction
This is based on 8-puzzle game.
An instance of the N-puzzle game consists of a board holding N = m^2 − 1 (m = 3, 4, 5, ...) distinct movable tiles, plus an empty space. The tiles are numbers from the set {1, …, m^2 − 1}. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this assignment, we will represent the blank space with the number 0 and focus on the m = 3 case (8-puzzle).
Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order ⟨0, 1, …, m^2 − 1⟩. The search space is the set of all possible states reachable from the initial state.
The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time. The cost of moving from one configuration of the board to another is the same and equal to one. Thus, the total cost of path is equal to the number of moves made from the initial state to the goal state. <br>
Some points to remember :
- First, we remove a node from the frontier set.
- Second, we check the state against the goal state to determine if a solution has been found.
- Finally, if the result of the check is negative, we then expand the node. To expand a given node, we generate successor nodes adjacent to the current node, and add them to the frontier set. Note that if these successor nodes are already in the frontier, or have already been visited, then they should not be added to the frontier again.

### Before start 
Before starting, you should have basic knowledge about some artificial intelligence concepts. You should know what is Breadth-First Search, Depth-First Search and A-Star Search.
For playing 8-puzzle game, here is the link : http://mypuzzle.org/sliding


### Language
This was written in Python. An open source, interpreted language
with a mix of imperative, OO and functional programming and data structures. Syntax is simple
and easy to learn.

### Run it
- python 8puzzle.py bfs 1,2,5,3,4,0,6,7,8
- python 8puzzle.py dfs 1,2,5,3,4,0,6,7,8
- python 8puzzle.py afs 1,2,5,3,4,0,6,7,8