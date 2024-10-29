from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.transposed_graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack=None):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        if stack is not None:
            stack.append(v)

    def _transpose(self):
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                self.transposed_graph[neighbor].append(vertex)

    def _dfs_transposed(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.transposed_graph[v]:
            if not visited[neighbor]:
                self._dfs_transposed(neighbor, visited, component)

    def find_sccs(self):
        stack = []
        visited = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                self._dfs(i, visited, stack)

        self._transpose()

        visited = [False] * self.vertices
        sccs = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                self._dfs_transposed(v, visited, component)
                sccs.append(component)

        return sccs


g = Graph(5)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(1, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

sccs = g.find_sccs()
print("Strongly Connected Components:", sccs)
