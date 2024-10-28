from collections import deque, defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        distances = [-1] * self.vertices
        queue = deque([start])
        distances[start] = 0

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)

        return distances

    def all_pairs_shortest_path(self):
        dist = []
        for i in range(self.vertices):
            dist.append(self.bfs(i))
        return dist


# Create a graph with 5 vertices
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

distances = g.all_pairs_shortest_path()
print("All-Pairs Shortest Path Matrix:")
for row in distances:
    print(row)
