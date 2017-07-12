import random


class Graph:
    def __init__(self):
        """
        graph variable is a dictionary of lists - graph is implemented as adjacency lists
        """
        self.graph = dict()
        self.nodes = set()

    def _topological_sort(self, root, visited, result):
        visited.add(root)

        for neighbour in self.graph[root]:
            if neighbour not in visited:
                result, visited = self._topological_sort(neighbour, visited, result)

        result.append(root)

        return result, visited

    def _get_random_node(self, nodes):
        return random.choice(nodes)

    def start_topological_sort(self, root=None):
        visited = set()
        result = list()
        nodes = list(self.graph.keys())
        print(nodes)

        if not nodes:
            return []

        if root is None:
            root = self._get_random_node(nodes)

        result, visited = self._topological_sort(root, visited, result)

        # For not connected graphs
        # nodes = nodes - visited
        # while nodes:
        #     new_root = self._get_random_node(nodes)
        #     new_result, new_visited = self._topological_sort(new_root, visited, result)
        #     nodes = nodes - new_visited
        #     result.extend(new_result)

        return result

    def add(self, node_from, node_to):
        if node_from not in self.graph.keys():
            self.graph.update({node_from: [node_to]})
        else:
            self.graph[node_from].append(node_to)

        if node_to not in self.nodes:
            self.graph.update({node_from: []})
