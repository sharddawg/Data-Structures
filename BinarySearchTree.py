class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            cur_node = self.root
            while True:
                while data < cur_node.data:
                    if cur_node.left is None:
                        cur_node.left = new_node
                        break
                    else:
                        cur_node = cur_node.left
                while data > cur_node.data:
                    if cur_node.right is None:
                        cur_node.right = new_node
                        break
                    else:
                        cur_node = cur_node.right
                if cur_node.left == new_node or cur_node.right == new_node:
                    break

    def preorder(self, start):
        if start is not None:
            print(str(start.data) + "-", end='')
            self.preorder(start.left)
            self.preorder(start.right)


tree = BinarySearchTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)
tree.preorder(tree.root)
