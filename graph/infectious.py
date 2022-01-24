import math


class SparseGraph():
    def __init__(self, edges, n_vertices, directed=False):
        self.Time = 0
        self.edges = edges
        self.vertices = []
        self.directed = directed
        self.V = n_vertices
        self.bridges = [False]*len(edges)
        for i in range(n_vertices):
            self.vertices.append([])
        self.visited = [False]*n_vertices
        for i, e in enumerate(edges):
            self.vertices[e[0]-1].append(i)
            if directed == False:
                self.vertices[e[1]-1].append(i)

    def shortest_path(self, source, dest):
        self.parent = [-1]*self.V
        queue = [source]
        while len(queue) > 0:
            node = queue.pop(0)
            self.visited[node-1] = True
            for e in self.vertices[node-1]:
                next_node = self.edges[e][0] + self.edges[e][1] - node
                if self.visited[next_node-1]:
                    continue
                self.parent[next_node-1] = e
                self.visited[next_node-1] = True
                if next_node == dest:
                    queue = []
                    break
                queue.append(next_node)
        if self.parent[dest-1] == -1:
            return []
        node = dest
        path = []
        while node != source:
            path.append(self.parent[node-1])
            node = self.edges[self.parent[node-1]][0] + \
                self.edges[self.parent[node-1]][1] - node
        return path

    def bridgeUtil(self, u, visited, parent, low, disc, edge=-1):

        visited[u-1] = True
        disc[u-1] = self.Time
        low[u-1] = self.Time
        self.Time += 1

        for e in self.vertices[u-1]:
            v = self.edges[e][0] + self.edges[e][1] - u
            if visited[v-1] == False:
                parent[v-1] = u
                self.bridgeUtil(v, visited, parent, low, disc, e)
                low[u-1] = min(low[u-1], low[v-1])
                if low[v-1] > disc[u-1]:
                    self.bridges[e] = True

            elif v != parent[u-1]:
                low[u-1] = min(low[u-1], disc[v-1])

    def bridge(self):

        self.bridges = [False]*len(self.edges)
        visited = [False] * (self.V)
        disc = [math.inf] * (self.V)
        low = [math.inf] * (self.V)
        parent = [-1] * (self.V)

        for i in range(1, self.V+1):
            if visited[i-1] == False:
                self.bridgeUtil(i, visited, parent, low, disc)


n, m = list(map(int, input().split()))
edges = []
for i in range(m):
    edge = list(map(int, input().split()))
    edges.append(edge)
g = SparseGraph(edges, n)
g.bridge()
q = int(input())
for i in range(q):
    b, e = list(map(int, input().split()))
    path = g.shortest_path(b, e)
    nodes = [False]*n
    nodes[b-1] = True
    nodes[e-1] = True
    for i in path:
        if g.bridges[i]:
            nodes[g.edges[i][0]-1] = True
            nodes[g.edges[i][1]-1] = True
    count = 0
    for i in nodes:
        if i:
            count += 1
    print(count)
