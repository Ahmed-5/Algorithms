import math

ex_dict = dict()

def get_hash(a,b):
    a,b = min(a,b), max(a,b)
    return str(a)+str(b)

def ex_dict_init(exclusions):
    for ex in exclusions:
        hash_code = get_hash(ex[0], ex[1])
        ex_dict[hash_code] = [True, math.inf]

def stop_update(a,b):
    hash_code = get_hash(a,b)
    ex_dict[hash_code][0] = False

def enable_update(a,b):
    hash_code = get_hash(a,b)
    ex_dict[hash_code][0] = True

def update_all(cost):
    for key in ex_dict.keys():
        if ex_dict[key][0] == True:
            ex_dict[key][1] = min(ex_dict[key][1], cost)

class SparseGraph():
    def __init__(self, edges, n_vertices):
        self.edges = edges
        self.vertices = []
        for i in range(n_vertices):
            self.vertices.append([])
        self.visited = [False]*n_vertices
        for i, e in enumerate(edges):
            self.vertices[e[0]].append(i)
            self.vertices[e[1]].append(i)

    def get_edges(self):
        for i in self.edges:
            print(i)

    def get_vertices(self):
        for i in self.vertices:
            print(i)

    def brute_force(self, cost=0,node=0, destination=-1):
        # if node==destination:
            # update_all(cost)
            # return

        stack = [[None, node,0]]
        path = []
        total_cost = []
        cost = 0
        while len(stack)>0:
            parent, node, temp = stack.pop()
            cost += temp
            print(parent, node, cost)
            if node==destination:
                print(cost)
                continue
            if parent == None:
                path.append(node)
                total_cost.append(temp)
                self.visited[node] = True
            else:
                while (len(path)>0) and (path[-1] != parent):
                    rem_node = path.pop()
                    self.visited[rem_node] = False
                    c = total_cost.pop()
                    cost -= c
                path.append(node)
                total_cost.append(temp)
            for e in self.vertices[node]:
                next_node = self.edges[e][0]+ self.edges[e][1] - node
                if self.visited[next_node]:
                    continue
                temp = self.edges[e][2]
                stack.append([node, next_node, temp])


        # self.visited[node] = True
        # for e in self.vertices[node]:
        #     next_node = edges[e][0]+edges[e][1] - node
        #     temp = edges[e][2] + cost
        #     if self.visited[next_node]:
        #         continue
            # stop_update(node, next_node)
            # self.brute_force(temp, next_node, destination)
            # enable_update(node, next_node)
        # self.visited[node] = False
        return


edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [2, 4, 5], [3, 5, 8], [1, 3, 3], [0, 2, 4]]
n_vertices = 6
dest = 5
# exclusions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [2, 4], [3, 5], [1, 3], [0, 2]]
# ex_dict_init(edges)
# ex_dict_init(exclusions)
G = SparseGraph(edges, n_vertices)
G.brute_force(node=0, destination=dest)
# for ex in exclusions:
#     ex_hash = get_hash(ex[0], ex[1])
#     if ex_dict[ex_hash][1] == math.inf:
#         print("Infinity")
#     else:
#         print(ex_dict[ex_hash][1])