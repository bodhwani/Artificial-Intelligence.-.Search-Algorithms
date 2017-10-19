import abc
import heapq
from collections import deque
from random import random
from time import time

from src.board import Board
from src.node import Node


class Solver(metaclass=abc.ABCMeta):
    def __init__(self, start_board: Board, depth: int = None):
        print("Entered itno class solver")
        self._goal = start_board.goal
        print("start_board is ",start_board)
        print("start_board.goal is ",start_board.goal)
        self._start_board = start_board
        self._frontier = deque()
        self._explored = set()
        self._path_cost = 0
        self._nodes_expanded = 0
        self._fringe_sz = 0
        self._max_fringe_sz = 0
        self._search_depth = 0
        self._max_search_depth = 0
        self._running_time = 0
        self._depth_limit = depth

    @property
    def nodes_expanded(self):
        return self._nodes_expanded

    @property
    def fringe_size(self):
        return self._fringe_sz

    @property
    def max_fringe_size(self):
        return self._max_fringe_sz

    @property
    def search_depth(self):
        return self._search_depth

    @property
    def max_search_depth(self):
        return self._max_search_depth

    @property
    def running_time(self):
        return self._running_time

    def update_fringe_size(self):
        self._fringe_sz = len(self._frontier)
        if self._fringe_sz > self._max_fringe_sz:
            self._max_fringe_sz = self._fringe_sz

    @abc.abstractmethod
    def solve(self):
        """
        To be implemented by detailed search strategies
        """
        raise NotImplementedError("Need to implement a concrete class with solve method.")


class IDA(Solver):
    pass


class AST(Solver):
    def __init__(self, start_board: Board, depth: int = None):
        super().__init__(start_board, depth)
        self._frontier = []
        self.action_priority = {
            'Up': 0,
            'Down': 1,
            'Left': 2,
            'Right': 3
        }

    @staticmethod
    def h(state: Board):
        cost = 0
        for r in range(state.size):
            for c in range(state.size):
                tok = int(state.tile((r, c)))
                r_goal, c_goal = divmod(tok, state.size)
                cost += abs(r_goal - r) + abs(c_goal - c)
        return cost

    def solve(self):
        start_time = time()
        root = Node(state=self._start_board)
        self._frontier.append((root.path_cost, None, 0, root))
        heapq.heapify(self._frontier)
        if root.state.string == self._goal:
            self._search_depth = root.depth
            self._running_time = time() - start_time
            return root
        while True:
            if len(self._frontier) == 0:
                self._running_time = time() - start_time
                raise ValueError('Goal not found.')
            cost, action, r, node = heapq.heappop(self._frontier)
            if node.state.string == self._goal:
                self.update_fringe_size()
                self._search_depth = node.depth
                self._running_time = time() - start_time
                return node
            self._nodes_expanded += 1
            self._explored.add(node.state.string)
            actions = node.state.actions
            for index, action in enumerate(actions):
                state = node.state.act(action)
                child = Node(state=state,
                             action=action,
                             path_cost=1,
                             parent=node)
                if child.depth > self._max_search_depth:
                    self._max_search_depth = child.depth
                if child.state.string not in self._explored:
                    heapq.heappush(self._frontier,
                                   (child.path_cost + self.h(state),
                                    self.action_priority[action],
                                    random(),
                                    child))
                    self._explored.add(child.state.string)
                    self.update_fringe_size()


class BFS(Solver):
    print("HEre is bfs")
   
    def solve(self):
        print("entered into solve function")
        start_time = time()
        root = Node(state=self._start_board)
        self._frontier.append(root)
        if root.state.string == self._goal:
            self._search_depth = root.depth
            self._running_time = time() - start_time
            return root
        while True:
            if len(self._frontier) == 0:
                self._running_time = time() - start_time
                raise ValueError('Goal not found.')
            node = self._frontier.popleft()
            if node.state.string == self._goal:
                self.update_fringe_size()
                self._search_depth = node.depth
                self._running_time = time() - start_time
                return node
            self._nodes_expanded += 1
            self._explored.add(node.state.string)
            actions = node.state.actions
            for action in actions:
                state = node.state.act(action)
                child = Node(state=state,
                             action=action,
                             path_cost=1,
                             parent=node)
                if child.depth > self._max_search_depth:
                    self._max_search_depth = child.depth
                if child.state.string not in self._explored:
                    self._frontier.append(child)
                    self._explored.add(child.state.string)
                    self.update_fringe_size()


class DFS(Solver):
    print("here is dfs")
    def solve(self):
        start_time = time()
        root = Node(state=self._start_board)
        self._frontier.append(root)
        if root.state.string == self._goal:
            self._search_depth = root.depth
            self._running_time = time() - start_time
            return root
        while True:
            if len(self._frontier) == 0:
                self._running_time = time() - start_time
                raise ValueError('Goal not found.')
            node = self._frontier.pop()
            self._explored.add(node.state.string)
            if node.state.string == self._goal:
                self.update_fringe_size()
                self._search_depth = node.depth
                self._running_time = time() - start_time
                return node
            self._nodes_expanded += 1
            actions = node.state.actions
            for action in list(reversed(actions)):
                state = node.state.act(action)
                child = Node(state=state,
                             action=action,
                             path_cost=1,
                             parent=node)
                if child.depth > self._max_search_depth:
                    self._max_search_depth = child.depth
                if child.state.string not in self._explored:
                    self._frontier.append(child)
                    self._explored.add(child.state.string)
                    self.update_fringe_size()
