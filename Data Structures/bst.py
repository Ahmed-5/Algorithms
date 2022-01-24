import math

class BinNode:
    def __init__(self, value):
        self.value = value
        self.size = 1
        self.height = 0
        self.parent = None
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        new_node = BinNode(value)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = None
            current = self.root
            while current != None:
                current.size += 1
                parent = current
                if value > current.value:
                    current = current.right
                else:
                    current = current.left
            new_node.parent = parent
            if value > parent.value:
                parent.right = new_node
            else:
                parent.left = new_node
            height = 0
            while parent != None and parent.height <= height:
                parent.height = max(parent.height, height+1)
                height = parent.height
                parent = parent.parent

    def add_node_diff_k(self, value, k):
        new_node = BinNode(value)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = None
            current = self.root
            while current != None:
                if abs(value-current.value) <= k:
                    print(
                        "can not be added because abs({} - {}) is less than or equal to than {}".format(value, current.value, k))
                    return
                parent = current
                if value > current.value:
                    current = current.right
                else:
                    current = current.left
            new_node.parent = parent
            if value > parent.value:
                parent.right = new_node
            else:
                parent.left = new_node

            height = 0
            while parent != None:
                parent.size += 1
                parent.height = max(parent.height, height+1)
                height = parent.height
                parent = parent.parent

    def traverse(self, node):
        if node == None:
            return

        self.traverse(node.left)
        print("value {} size {} height {}".format(node.value, node.size, node.height))
        self.traverse(node.right)

    def successor(self, value):
        '''to make things work as i implmented the BST the successor 
        is the next value that is strictly bigger than to the value'''
        successor = math.inf
        if self.root != None:
            current = self.root
            while current != None:
                if current.value > value:
                    successor = min(current.value, successor)
                    current = current.left
                if current.value > value:
                    successor = min(current.value, successor)
                    current = current.left
                else:
                    current = current.right
        return successor

    def predecessor(self, value):
        '''to make things work as i implmented the BST the predecessor 
        is the next value that is less than or equal to the value'''
        predecessor = -math.inf
        if self.root != None:
            current = self.root
            while current != None:
                if current.value < value:
                    predecessor = max(current.value, predecessor)
                    current = current.right
                    # print(current)
                elif predecessor == value:
                    predecessor = max(current.value, predecessor)
                    current = current.left
                else:
                    current = current.left
        return predecessor

    def predecessor_node(self, value, root:BinNode):
        '''to make things work as i implmented the BST the predecessor 
        is the next value that is less than or equal to the value'''
        predecessor = -math.inf
        node = None
        if root != None:
            current = root
            while current != None:
                if current.value < value:
                    predecessor = max(current.value, predecessor)
                    node = current
                    current = current.right
                elif current.value == value:
                    predecessor = max(current.value, predecessor)
                    node = current
                    current = current.left
                else:
                    current = current.left
        return node

    def delete(self, value):
        if self.root != None:
            current = self.root
            while current != None:
                if current.value == value:
                    if current.left and current.left.value == value:
                        current = current.left
                    else:
                        break
                elif current.value > value:
                    current = current.left
                else:
                    current = current.right
            if current == None:
                print("value not found")
            else:
                if not current.left and not current.right:
                    parent = current.parent
                    start_aug = parent
                    if parent:
                        if parent.left and parent.left.value == current.value:
                            parent.left = None
                        else:
                            parent.right = None
                    else:
                        self.root = None
                    
                    del current
                elif not current.left or not current.right:
                    start_aug = current.parent
                    child = current.left if current.left else current.right
                    parent = current.parent
                    child.parent = parent
                    if parent:
                        if parent.left and parent.left.value == current.value:
                            parent.left = child
                        else:
                            parent.right = child
                    else:
                        self.root = child
                    
                    del current
                else:
                    start_aug = None
                    pred_node = self.predecessor(value)
                    print(pred_node)
                    self.delete(pred_node)
                    current.value = pred_node
                
                while start_aug != None:
                    start_aug.size -= 1
                    h_right = -1 if not start_aug.right else start_aug.right.height
                    h_left = -1 if not start_aug.left else start_aug.left.height
                    start_aug.height = max(h_left+1, h_right+1)
                    start_aug = start_aug.parent



    def asc_rank(self, value):
        rank = 0
        if self.root != None:
            current = self.root
            while current != None:
                if current.value > value:
                    current = current.left
                else:
                    rank += 1
                    if current.left:
                        rank += current.left.size
                    current = current.right
        return rank



bst = BinarySearchTree()
bst.add_node(15)
# bst.add_node(10)
# bst.add_node(11)
bst.add_node(16)
# bst.add_node(16)
# bst.add_node_diff_k(22, 1)
# bst.add_node(18)
# bst.traverse(bst.root)
# print(bst.asc_rank(10))
# print(bst.asc_rank(16))
# print(bst.successor(17))
# print(bst.predecessor(13))
# print(bst.successor(16))
# print(bst.predecessor(16))
# print()
bst.delete(15)
bst.traverse(bst.root)
# print()
# bst.delete(10)
# bst.traverse(bst.root)
# print()
# bst.delete(15)
# bst.traverse(bst.root)