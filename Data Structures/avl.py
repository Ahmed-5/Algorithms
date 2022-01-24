import math

class BinNode:
    def __init__(self, value):
        self.value = value
        self.size = 1
        self.height = 0
        self.parent:BinNode = None
        self.right:BinNode = None
        self.left:BinNode = None


class AVL:
    def __init__(self):
        self.root = None


    def update_aug(self, node:BinNode):
        while node != None:
            size_l = 0 if not node.left else node.left.size
            size_r = 0 if not node.right else node.right.size
            node.size = 1 + size_l + size_r

            height_l = -1 if not node.left else node.left.height
            height_r = -1 if not node.right else node.right.height
            node.height = 1 + max(height_l, height_r)

            node = node.parent


    def rotate_left(self, node:BinNode):
        if node == None:
            return
        if node.right:
            if not node.parent:
                self.root = node.right
            elif node.parent.left.value == node.value:
                node.parent.left = node.right
            elif node.parent.right.value == node.value:
                node.parent.right = node.right
            right = node.right
            B = right.left
            right.parent, node.parent = node.parent, right
            right.left, node.right = node, B
            if B:
                B.parent = node
            
            self.update_aug(node)


    def rotate_right(self, node):
        if node == None:
            return
        if node.left:
            if not node.parent:
                self.root = node.left
            elif node.parent.right.value == node.value:
                node.parent.right = node.left
            elif node.parent.left.value == node.value:
                node.parent.left = node.left
            left = node.left
            B = left.right
            left.parent, node.parent = node.parent, left
            left.right, node.left = node, B
            if B:
                B.parent = node
            
            self.update_aug(node)


    def rebalance(self, node:BinNode):
        while node != None:
            left = node.left
            right = node.right
            height_l = -1 if not left else left.height
            height_r = -1 if not right else right.height
            if height_l >= height_r + 2:
                hll = -1 if not left.left else left.left.height
                hlr = -1 if not left.right else left.right.height
                if hll > hlr:
                    self.rotate_right(node)
                else:
                    self.rotate_left(left)
                    self.rotate_right(node)
            elif height_r >= height_l + 2:
                hrl = -1 if not right.left else right.left.height
                hrr = -1 if not right.right else right.right.height
                if hrr > hrl:
                    self.rotate_left(node)
                else:
                    self.rotate_right(left)
                    self.rotate_left(node)
            
            node = node.parent

    
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
            
            self.rebalance(new_node)


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
            
            self.rebalance(new_node)


    def traverse(self, node):
        if node == None:
            return

        self.traverse(node.left)
        print("value {} size {} height {}".format(node.value, node.size, node.height))
        self.traverse(node.right)


    def successor(self, value):
        '''to make things work as i implmented the BST the successor 
        is the next value that is strictly bigger than the value'''
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
        is the next value that is strictly less than the value'''
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
        is the next value that is strictly less than the value'''
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
                    # print(pred_node)
                    self.delete(pred_node)
                    current.value = pred_node
                
                start_rebalance = start_aug
                while start_aug != None:
                    start_aug.size -= 1
                    h_right = -1 if not start_aug.right else start_aug.right.height
                    h_left = -1 if not start_aug.left else start_aug.left.height
                    start_aug.height = max(h_left+1, h_right+1)
                    start_aug = start_aug.parent

                self.rebalance(start_rebalance)


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



avl = AVL()
avl.add_node(15)
avl.traverse(avl.root)
print()
avl.add_node(10)
avl.traverse(avl.root)
print()
avl.add_node(11)
avl.traverse(avl.root)
print()
avl.add_node(16)
avl.traverse(avl.root)
print()
avl.add_node(16)
avl.traverse(avl.root)
print()
avl.add_node(22)
avl.traverse(avl.root)
print()
avl.add_node(18)
avl.traverse(avl.root)
print()
avl.add_node(23)
avl.traverse(avl.root)
# print()
# avl.rotate_left(avl.root.right)
# avl.traverse(avl.root)
# print()
# avl.rotate_right(avl.root.right)
# avl.traverse(avl.root)
# print(avl.asc_rank(10))
# print(avl.asc_rank(16))
# print(avl.successor(17))
# print(avl.predecessor(13))
# print(avl.successor(16))
# print(avl.predecessor(16))
# print()
print("DELETE")
avl.delete(15)
avl.traverse(avl.root)
print()
avl.delete(10)
avl.traverse(avl.root)
print()