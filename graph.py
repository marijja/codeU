import random


class Graph:
    def __init__(self):
        """
        Graph variable is a dictionary of lists - graph is implemented as adjacency lists
        """
        self.graph = dict()

    def _topological_sort(self, root, visited, result):
        visited.add(root)
        print(root)
        for neighbour in self.graph[root]:
            if neighbour not in visited:
                result, visited = self._topological_sort(neighbour, visited, result)

        result.append(root)

        return result, visited

    def start_topological_sort(self):
        """
        We perform topological sort for each node, if it was not visited
        :return list: contents of letters stack
        """
        visited = set()
        result = list()
        nodes = list(self.graph.keys())

        if not nodes:
            return []

        for n in nodes:
            if n not in visited:
                result, visited = self._topological_sort(n, visited, result)

        return result[::-1]

    def add_to_graph(self, node_from, node_to):
        if node_from and node_from not in self.graph.keys():
            self.graph.update({node_from: [node_to]})
        elif node_from:
            self.graph[node_from].append(node_to)

        if node_to and node_to not in self.graph.keys():
            self.graph.update({node_to: []})
