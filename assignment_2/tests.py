import unittest

from binary_tree import T_node
from node_ancestors import print_ancestors
from lca import Lca_finder


class Tree_creator:
    def __init__(self, nodes_num, min_value=0):
        self._values = self.generate_values(nodes_num, min_value)

    def generate_values(self, end, start=0):
        return list(range(start, end))

    def build_full_tree(self, height):
        if height == -1:
            return None

        if not self._values:
            return None

        left = self.build_full_tree(height - 1)
        root = T_node(self._values.pop())
        root._right = self.build_full_tree(height - 1)

        root._left = left

        return root

    def build_path(self):
        if not self._values:
            return None

        root = T_node(self._values.pop())
        root._left = self.build_path()

        return root


class TestParentsPrinting(unittest.TestCase):
    def setUp(self, height=5, searched_node=2, nodes_count=20):
        super(TestParentsPrinting, self).__init__()
        self._height = height
        self._searched_node = searched_node
        self._nodes_count = nodes_count

    def test_full_tree(self):
        full_tree_creator = Tree_creator(pow(2, self._height + 1))
        full_tree = full_tree_creator.build_full_tree(self._height)
        res = print_ancestors(full_tree, self._searched_node)
        self.assertTrue(res)

    def test_single_node(self):
        node = T_node(self._searched_node)
        res = print_ancestors(node, self._searched_node)
        self.assertTrue(res)

    def test_path(self):
        path_creator = Tree_creator(self._nodes_count)
        path = path_creator.build_path()
        res = print_ancestors(path, self._searched_node)
        self.assertTrue(res)


class TestLca(unittest.TestCase):
    def setUp(self, height=5, node=2, nodes_count=20):
        super(TestLca, self).__init__()
        self._height = height
        self._node = node
        self._nodes_count = nodes_count

    def test_full_tree(self):
        full_node_count = pow(2, self._height + 1)
        full_tree_creator = Tree_creator(full_node_count)
        full_tree = full_tree_creator.build_full_tree(self._height)

        lca_run = Lca_finder()
        res = lca_run.run_lca(2, 5, full_tree)
        self.assertEqual(res, 4)

    def test_single_node(self):
        node = T_node(self._node)

        lca_run = Lca_finder()
        res = lca_run.run_lca(3, 10, node)
        self.assertEqual(res, -1)

    def test_path(self):
        path_creator = Tree_creator(self._nodes_count)
        path = path_creator.build_path()

        lca_run = Lca_finder()
        res = lca_run.run_lca(3, 10, path)
        self.assertEqual(res, 10)


if __name__ == '__main__':
    unittest.main()
