import math
from heapq import heappop, heappush

ex_dict = dict()


def get_hash(a, b):
    a, b = min(a, b), max(a, b)
    return str(a)+str(b)


def ex_dict_init(exclusions):
    for ex in exclusions:
        hash_code = get_hash(ex[0], ex[1])
        ex_dict[hash_code] = [True, math.inf]


def stop_update(a, b):
    hash_code = get_hash(a, b)
    ex_dict[hash_code][0] = False


def update_all(cost):
    for key in ex_dict.keys():
        if ex_dict[key][0] == True:
            ex_dict[key][1] = min(ex_dict[key][1], cost)
        else:
            ex_dict[key][0] = True


class SparseGraph():
    def __init__(self, edges, n_vertices, directed=False):
        self.Time = 0
        self.edges = edges
        self.vertices = []
        self.directed = directed
        self.bridges = [False]*len(self.edges)
        self.V = n_vertices
        for i in range(n_vertices):
            self.vertices.append([])
        self.visited = [False]*n_vertices
        for i, e in enumerate(edges):
            self.vertices[e[0]].append(i)
            if directed == False:
                self.vertices[e[1]].append(i)

    def get_edges(self):
        for i in self.edges:
            print(i)

    def reverse_edges(self):
        if self.directed == False:
            return
        vertices = []
        for i in range(len(self.vertices)):
            vertices.append([])
        for i, v in enumerate(self.vertices):
            for e in v:
                vertices[self.edges[e][1]+self.edges[e][0]-i].append(e)
        self.vertices = vertices

    def get_vertices(self):
        for i in self.vertices:
            print(i)

    def brute_force(self, node=0, destination=-1):
        # print(node, "down")
        if node == destination:
            # print(node, "up")
            return
        self.visited[node] = True
        for e in self.vertices[node]:
            next_node = edges[e][0]+edges[e][1] - node
            if self.visited[next_node]:
                continue
            self.dfs(next_node, destination)
        self.visited[node] = False
        # print(node, "up")
        return

    def dfs(self, node=0, destination=-1):
        self._dfs(node, destination)
        self.visited = [False for i in self.visited]
        return

    def _dfs(self, node=0, destination=-1):
        # print(node, "down")
        if node == destination:
            # print(node, "up")
            return
        self.visited[node] = True
        for e in self.vertices[node]:
            next_node = edges[e][0]+edges[e][1] - node
            if self.visited[next_node]:
                continue
            self._dfs(next_node, destination)
        # print(node, "up")
        return

    def topo_sort(self):
        topo = []
        for i in range(len(self.vertices)):
            if self.visited[i] == False:
                temp = self._topo_sort(i)
                temp.extend(topo)
                topo = temp
        self.visited = [False for i in self.visited]
        return topo

    def _topo_sort(self, node=0):
        nodes = [node]
        index = 1
        # print(node, "down")
        self.visited[node] = True
        for e in self.vertices[node]:
            next_node = edges[e][0]+edges[e][1] - node
            if self.visited[next_node]:
                continue
            temp = self._topo_sort(next_node)
            for i in range(len(temp)):
                nodes.insert(index+i, temp[i])
        # print(node, "up")
        return nodes

    def strongly_connected(self):
        self.reverse_edges()
        sort_topo = self.topo_sort()
        self.reverse_edges()
        scc = []
        for i in sort_topo:
            if self.visited[i]:
                continue
            scc.append(self._topo_sort(i))
        self.visited = [False for i in self.visited]
        return scc

    def bfs(self, node=0, destination=-1):
        nodes = [node]
        self.layer_vertices = [math.inf]*len(self.vertices)
        self.layer_vertices[node] = 0
        self._bfs(nodes, destination)
        return

    def _bfs(self, nodes, destination=-1, layer=0):
        # print(*nodes)
        next_nodes = []
        if destination in nodes or nodes == []:
            return
        for i in nodes:
            self.visited[i] = True
            self.layer_vertices[i] = layer
        for i in nodes:
            for e in self.vertices[i]:
                next_node = edges[e][0]+edges[e][1] - i
                if self.visited[next_node]:
                    continue
                next_nodes.append(next_node)
        self._bfs(next_nodes, destination, layer+1)
        for i in nodes:
            self.visited[i] = False
        return

    def bfs_con(self, node=0):
        nodes = [node]
        return self._bfs_con(nodes)

    def _bfs_con(self, nodes):
        # print(*nodes)
        next_nodes = []
        connections = []
        for i in nodes:
            self.visited[i] = True
            connections.append(i)
        for i in nodes:
            for e in self.vertices[i]:
                next_node = edges[e][0]+edges[e][1] - i
                if self.visited[next_node]:
                    continue
                next_nodes.append(next_node)
        if next_nodes != []:
            connections.extend(self._bfs_con(next_nodes))
        return list(set(connections))

    def connectivity(self):
        connections = []
        for i in range(len(self.vertices)):
            if self.visited[i] == False:
                c = self.bfs_con(i)
                connections.append(c)
        self.visited = [False for i in self.visited]
        return connections

    def bridgeUtil(self, u, visited, parent, low, disc, edge=-1):
        print(u)

        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for e in self.vertices[u]:
            v = self.edges[e][0] + self.edges[e][1] - u
            if visited[v] == False:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc, e)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    self.bridges[e] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridge(self):

        self.bridges = [False]*len(self.edges)
        visited = [False] * (self.V)
        disc = [math.inf] * (self.V)
        low = [math.inf] * (self.V)
        parent = [-1] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc)

    def dijkstra(self, destination, node=0, exclude=None):
        self.visited = [False]*self.n_vertices
        self.q = [[0, node, node]]
        self.cost_vertices = [math.inf]*len(self.vertices)
        while self.q != []:
            (cost, src, v1) = heappop(self.q)
            if self.visited[v1] == False:
                self.visited[v1] = True
                if src != v1:
                    stop_update(src, v1)
                if v1 == destination:
                    update_all(cost)
                    return

                for e in self.vertices[v1]:
                    v2 = edges[e][0]+edges[e][1] - v1
                    c = edges[e][2]
                    if self.visited[v2] == True or ((exclude != None) and (v1 in exclude) and (v2 in exclude)):
                        continue
                    prev = self.cost_vertices[v2]
                    next_cost = cost + c
                    if next_cost < prev:
                        self.cost_vertices[v2] = next_cost
                        heappush(self.q, (next_cost, v1, v2))
        return


edges = [[0, 1, 2], [1, 2, 4], [1, 5, 3], [1, 6, 5], [2, 3, 8], [5, 7, 9], [3, 7, 20], [6, 8, 10], [3, 8, 100], [3, 4, 16]]
n_vertices = 9
G = SparseGraph(edges, n_vertices, True)
# G.get_edges()
# print()
# G.get_vertices()
# G.dfs()
# G.bfs()
# print(* G.layer_vertices)
# print(G.topo_sort())
# print(G.strongly_connected())
# G.get_vertices()
# print(G.connectivity())
# G.bridge()
print(*G.bridges)
