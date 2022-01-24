class Node():
    def __init__(self, value, start, end):
        self.left:Node = None
        self.right:Node = None
        self.parent:Node = None
        self.value = value
        self.s = start
        self.e = end

class SegmentTree():
    def op(self, a, b = None):
        if b and a:
            return a+ b
        elif a:
            return a
        else:
            return b


    def __init__(self, arr:list):
        self.root = None
        current = [Node(j, i, i) for i,j in enumerate(arr)]
        while len(current) != 1:
            n = len(current)
            new_arr = []
            if n == 2:
                node = Node(
                    self.op(current[0].value, current[1].value),
                    current[0].s,
                    current[1].e
                )
                current[0].parent = node
                current[1].parent = node
                node.left = current[0]
                node.right = current[1]
                new_arr.append(node)
            else:
                for i in range(0,n//2+1,2):
                    if i < n//2:
                        node = Node(
                            self.op(current[i].value, current[i+1].value),
                            current[i].s,
                            current[i+1].e
                        )
                        current[i].parent = node
                        current[i+1].parent = node
                        node.left = current[i]
                        node.right = current[i+1]
                        new_arr.append(node)
                    else:
                        node = Node(
                            current[i].value,
                            current[i].s,
                            current[i].e
                        )
                        current[i].parent = node
                        node.left = current[i]
                        new_arr.append(node)
                for i in range(n//2+1, n, 2):
                    if i < n-1:
                        node = Node(
                            self.op(current[i].value, current[i+1].value),
                            current[i].s,
                            current[i+1].e
                        )
                        current[i].parent = node
                        current[i+1].parent = node
                        node.left = current[i]
                        node.right = current[i+1]
                        new_arr.append(node)
                    else:
                        node = Node(
                            current[i].value,
                            current[i].s,
                            current[i].e
                        )
                        current[i].parent = node
                        node.left = current[i]
                        new_arr.append(node)
            current = new_arr
        self.root = current[0]

    def traverse(self, node:Node):
        if node == None:
            return
        self.traverse(node.left)
        print(node.value, node.s, node.e)
        self.traverse(node.right)

    def __query__(self, sq, eq, node:Node):
        # print(sq, eq, node.s, node.e)
        # print()
        if not node or sq<node.s or eq>node.e or sq>eq:
            return None
        if sq == node.s:
            if eq == node.e:
                # print(node.value)
                return node.value
            elif eq<node.e:
                el = node.left.e
                if eq<el:
                    return self.__query__(sq, eq, node.left)
                elif eq == el:
                    return node.left.value
                else:
                    return self.op(
                        node.left.value,
                        self.__query__(node.right.s, eq, node.right)
                    )
        elif sq>node.s:
            if eq == node.e:
                has_right = True if node.right else False
                if not has_right:
                    return self.__query__(sq, eq, node.left)
                else:
                    # print(sq, eq, node.s, node.e)
                    right = node.right
                    sr = node.right.s
                    if sq>sr:
                        return self.__query__(sq, eq, right)
                    elif sr == sq:
                        return right.value
                    else:
                        return self.op(
                            self.__query__(sq, node.left.e, node.left),
                            right.value
                        )
            elif eq<node.e:
                has_right = True if node.right else False
                if not has_right:
                    return self.__query__(sq, eq, node.left)
                else:
                    sr = node.right.s
                    el = node.left.e
                    if sq<sr and eq>el:
                        return self.op(
                            self.__query__(sq, el, node.left),
                            self.__query__(sr, eq, node.right)
                        )
                    elif eq<el:
                        return self.__query__(sq, eq, node.left)
                    elif sq>sr:
                        return self.__query__(sq, eq, node.right)
                    elif sq == sr:
                        return self.__query__(sq, eq, node.right)
                    elif eq == el:
                        return self.__query__(sq, eq, node.left)


    def query(self, start, end):
        if start < 0 or start > end or end > self.root.e or end<0 or start > self.root.e:
            return None
        return self.__query__(start, end, self.root)
                
n = 5076
arr = [i+1 for i in range(n)]

st = SegmentTree(arr)
# st.traverse(st.root)
# print(st.query(1,1))
for i in range(n):
    a = 0
    for j in range(i, n):
        a += arr[j]
        b = st.query(i,j)
        # print("{}\t{}\t{}\t{}\t{}".format(i,j,a,b,a==b))
        if a!=b:
            print(i,j,False)