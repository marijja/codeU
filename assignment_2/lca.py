from math import sqrt

class Lca_finder:
    # we divide levels of tree into zones (groups of levels with that have hegiht of sqrt(height)
    # zones denote last ancestor in the previous zone

    def __init__(self):
        self._levels = {}
        self._parents = {}
        self._zones = {}
        self._height = 0
        self._zone_size = 1
        self._root = None

    def set_data(self, node, parent_data, current_level):
        if node == None:
            return

        if current_level == 0:
            self._root = node

        self._parents.update({ node._data : parent_data })
        self._levels.update({ node._data : current_level })

        if node._left == None and node._right == None:
            if self._height < current_level:
                self._height = current_level
                self._zone_size = 1 if sqrt(self._height) < 1 else sqrt(self._height)
        else:
            self.set_data(node._left, node._data, current_level+1)
            self.set_data(node._right, node._data, current_level + 1)


    def set_zones(self, node):
        if self._levels[node._data] < self._zone_size:
            self._zones.update( { node._data : 1 })
        else:
            if self._levels[node._data] % self._zone_size == 0:
                self._zones.update({ node._data : self._parents[node._data] })
            else:
                self._zones.update({ node._data : self._zones[self._parents[node._data]] })

        if node._left != None:
            self.set_zones(node._left)

        if node._right != None:
            self.set_zones(node._right)

    def run_lca(self, node1_data, node2_data, root):
        self.set_data(root, -1, 0)
        self.set_zones(root)
        x = node1_data
        y = node2_data

        if node1_data not in self._levels or node2_data not in self._levels:
            return -1

        while self._zones[x] != self._zones[y]:
            if self._levels[x] > self._levels[y]:
                x = self._zones[x]
            else:
                y = self._zones[y]

        while x != y and self._parents[x] != -1:
            if self._levels[x] > self._levels[y]:
                x = self._parents[x]
            else:
                y = self._parents[y]

        return x