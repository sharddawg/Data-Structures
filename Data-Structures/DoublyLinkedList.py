class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.butt = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.butt = self.head
            return
        cur_node = self.head
        while cur_node.right is not None:
            cur_node = cur_node.right
        cur_node.right = new_node
        new_node.left = cur_node
        self.butt = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.right = self.head
        self.head.left = new_node
        self.head = new_node

    def print(self):
        cur_node = self.head
        while cur_node.right is not None:
            print(cur_node.data, "<-> ", end='')
            cur_node = cur_node.right
        print(cur_node.data)

    def print_reverse(self):
        cur_node = self.butt
        while cur_node.left is not None:
            print(cur_node.data, "<-> ", end='')
            cur_node = cur_node.left
        print(cur_node.data)


linked_list = LinkedList()
linked_list.append(12)
linked_list.append(23)
linked_list.append(34)
linked_list.append(45)
linked_list.print()
linked_list.print_reverse()
linked_list.prepend(1)
linked_list.print()
linked_list.print_reverse()
