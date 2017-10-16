from collections import defaultdict

class Graph:
    def __init__(self):
        """
        Graph variable is a dictionary of lists - graph is implemented as adjacency lists
        We keep track of the nodes withour outgoing edges too
        """
        self.graph = defaultdict(list)

    def _topological_sort(self, root, visited, result):
        visited.add(root)
        print(root)
        for neighbour in self.graph[root]:
            if neighbour not in visited:
                self._topological_sort(neighbour, visited, result)

        result.append(root)

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
                self._topological_sort(n, visited, result)

        return result[::-1]

    def add_to_graph(self, node_from, node_to):
        if node_from:
            self.graph[node_from].append(node_to)

        if node_to:
            self.graph[node_to]
