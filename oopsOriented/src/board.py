from copy import deepcopy
from math import sqrt


class Board:
    def __init__(self, tiles: str, hole: str = '0', sz: int = None):
        board_ = tiles.split(',')
        print("Board Values :")
        print("Board is ",board_)
        #Board is  ['1', '2', '5', '3', '4', '0', '6', '7', '8']
        self._sz = sz or int(sqrt(len(board_)))
        print("_sz is ",self._sz)
        self._sorted_tokens = [str(x) for x in range(self._sz ** 2)]
        print("_sorted tokens are",self._sorted_tokens)
        #_sorted tokens are ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self._goal = [[str(i + j * self._sz) for i in range(self._sz)] for j in range(self._sz)]
        print("Goal is ",self._goal)
        #Goal is  [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
        self._state = [[board_[i + j * self._sz] for i in range(self._sz)] for j in range(self._sz)]
        print("_state is ",self._state)
        #_state is  [['1', '2', '5'], ['3', '4', '0'], ['6', '7', '8']]
        self._hole = hole
        print("Hole is ",self._hole)
        self._valid_moves = self.valid_moves()
        print("Valid moves are",self._valid_moves)
        self._neighbors = self.neighbors()
        print("Neighbours are",self._neighbors)
        print("\n")

    def __repr__(self):
        return str(self._state)

    @property
    def actions(self):
        return self._valid_moves

    @property
    def size(self):
        return self._sz

    @property
    def goal(self):
        print("Entered into Board.goal()")
        return ','.join(self._sorted_tokens)

    @property
    def sorted_tokens(self):
        print("Entered into Board.sorted_tokens()")
        return self._sorted_tokens

    @property
    def string(self):
        return self.stringify(self._state)

    @property
    def state(self):
        return self._state

    @staticmethod
    def stringify(state: [list]):
        stringified = ','.join([item for sublist in state for item in sublist])
        return stringified

    def hole_pos(self):
        ix = [self._state[r][c] == self._hole for r in range(self._sz)
              for c in range(self._sz)].index(True)
        print("IX is ",ix)
        hole_pos_ = divmod(ix, self._sz)
        return hole_pos_

    def tile(self, pos: tuple):
        return self._state[pos[0]][pos[1]]

    def neighbors(self):
        r, c = self.hole_pos()
        neighbors = {
            'Up': (r - 1, c),
            'Down': (r + 1, c),
            'Left': (r, c - 1),
            'Right': (r, c + 1)
        }
        return neighbors

    def act(self, action: str):
        pos = self._neighbors[action]
        board_ = self.swap(pos)
        return board_

    def valid_moves(self):
        """
        find neighboring tiles to hole position
        """
        hole = self.hole_pos()
        actions_ = []
        if hole[0] > 0:
            actions_.append('Up')
        if hole[0] < self._sz - 1:
            actions_.append('Down')
        if hole[1] > 0:
            actions_.append('Left')
        if hole[1] < self._sz - 1:
            actions_.append('Right')
        return actions_

    def swap(self, pos: tuple):
        """
        position is tuple (R,C) of neighboring tile to hole
        """
        hole = self.hole_pos()
        tile = self.tile(pos)
        temp_state = deepcopy(self._state)
        temp_state[pos[0]][pos[1]] = self._hole
        temp_state[hole[0]][hole[1]] = tile
        new_board = Board(self.stringify(temp_state),
                          hole=self._hole,
                          sz=self._sz)
        return new_board

#What is the meaning of __repr__
