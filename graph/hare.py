import math
from heapq import heappop, heappush

class SparseGraph():
    def __init__(self, edges, n_vertices, directed=False):
        self.edges = edges
        self.vertices = []
        self.n_vertices = n_vertices
        for i in range(n_vertices):
            self.vertices.append([])
        self.visited = [False]*n_vertices
        for i, e in enumerate(edges):
            self.vertices[e[0]].append(i)
            if not directed:
                self.vertices[e[1]].append(i)

    def get_edges(self):
        for i in self.edges:
            print(i)

    def get_vertices(self):
        for i in self.vertices:
            print(i)

    def dijkstra(self, destination, node=0, exclude=None):
        self.visited = [False]*self.n_vertices
        self.q = [[0, node, node]] 
        self.cost_vertices = [math.inf]*len(self.vertices)
        while self.q != []:
            (cost, src, v1) = heappop(self.q)
            if self.visited[v1] == False:
                self.visited[v1] = True
                # if src != v1:
                #     stop_update(src, v1)
                if v1 == destination:
                    return cost

                for e in self.vertices[v1]:
                    v2 = self.edges[e][0]+self.edges[e][1] - v1
                    c = self.edges[e][2]
                    if self.visited[v2]==True or ((exclude != None) and (v2 == exclude)): 
                        continue
                    prev = self.cost_vertices[v2]
                    next_cost = cost + c
                    if next_cost < prev:
                        self.cost_vertices[v2] = next_cost
                        heappush(self.q, (next_cost, v1, v2))
        return -1


n = 9
arr = [[0, 1, 2], [1, 2, 4], [1, 5, 3], [1, 6, 5], [2, 3, 8], [
    5, 7, 9], [3, 7, 20], [6, 8, 10], [3, 8, 100], [3, 4, 16]]

s = 1
t = 5


g = SparseGraph(arr, n)

sol = []

for i in range(n):
    if i == s-1 or i == t-1:
        continue
    cost = g.dijkstra(t-1, s-1, i)
    if cost == -1:
        continue
    sol.append([cost, i])

sol.sort(key = lambda x: -x[0])
print(sol[0][-1]+1)