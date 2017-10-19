class Node:
    def __init__(self, state, action=None, path_cost=None, parent=None):
        if not parent:
            self._state = state
            self._actions = []
            self._path_costs = []
        else:
            self._state = state
            self._actions = parent.actions[:]
            self._actions.append(action)
            self._path_costs = parent.path_costs[:]
            self._path_costs.append(path_cost)

    def __repr__(self):
        return str({'state': self._state.state,
                    'action': self._actions,
                    'path_cost': self.path_cost})

    @property
    def state(self):
        return self._state

    @property
    def actions(self):
        return self._actions

    @property
    def path_costs(self):
        return self._path_costs

    @property
    def path_cost(self):
        return sum(self._path_costs)

    @property
    def depth(self):
        return len(self._actions)  # to account for 0 indexing
