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
                    v2 = edges[e][0]+edges[e][1] - v1
                    c = edges[e][2]
                    if self.visited[v2]==True or ((exclude != None) and (v2 == exclude)): 
                        continue
                    prev = self.cost_vertices[v2]
                    next_cost = cost + c
                    if next_cost < prev:
                        self.cost_vertices[v2] = next_cost
                        heappush(self.q, (next_cost, v1, v2))
        return -1


edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [2, 4, 5], [3, 5, 8], [1, 3, 3], [0, 2, 4]]
n_vertices = 6
dest = 5
exclusions = [2, 1, 3]
G = SparseGraph(edges, n_vertices, directed=True)
G.dijkstra(dest ,node=0)
indicies = []
for i in exclusions:
    print(i, G.dijkstra(dest, 0, i))
# for i in indicies:
#     G.dijkstra(dest ,node=0, exclude=exclusions[i])

arr = []