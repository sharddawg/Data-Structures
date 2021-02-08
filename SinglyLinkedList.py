class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        new_node = Node(data)
        cur_node = self.head
        i = 0
        while i != index - 1:
            cur_node = cur_node.next
            i += 1
        new_node.next = cur_node.next
        cur_node.next = new_node

    def remove_beginning(self):
        cur_node = self.head
        self.head = cur_node.next
        cur_node = None

    def remove_end(self):
        cur_node = self.head
        prev_node = None
        while cur_node.next is not None:
            prev_node = cur_node
            cur_node = cur_node.next
        prev_node.next = None

    def remove(self, data):
        cur_node = self.head
        prev_node = None
        while cur_node.data != data:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_node.next is None:
                return print("Element does not exist in the linked list")
        prev_node.next = cur_node.next
        cur_node = None

    def remove_at_index(self, index):
        cur_node = self.head
        i = 0
        temp = cur_node
        if index == 0:
            self.head = cur_node.next
            cur_node = None
            return
        while i != index:
            temp = cur_node
            cur_node = cur_node.next
            i += 1
            if cur_node.next is None:
                return print("Index out of range")
        temp.next = cur_node.next
        cur_node = None

    def reverse(self):
        cur_node = self.head
        next_node = None
        prev_node = None
        while cur_node.next is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        cur_node.next = prev_node
        self.head = cur_node

    def print(self):
        cur_node = self.head
        while cur_node.next is not None:
            print(cur_node.data, "-> ", end='')
            cur_node = cur_node.next
        print(cur_node.data)

    def length(self):
        cur_node = self.head
        i = 1
        while cur_node.next is not None:
            cur_node = cur_node.next
            i += 1
        return i

    def get_element(self, index):
        cur_node = self.head
        if index == 0:
            return cur_node.data
        else:
            i = 0
            while i != index:
                cur_node = cur_node.next
                if cur_node.next is None:
                    return print("Index is out of range")
                i += 1
            return cur_node.data

    def get_index(self, data):
        cur_node = self.head
        if cur_node.data == data:
            return 0
        else:
            i = 0
            while cur_node.data != data:
                if cur_node.next is None:
                    return print("Element was not found in the linked list")
                cur_node = cur_node.next
                i += 1
            return i

    def update_element(self, index, data):
        cur_node = self.head
        i = 0
        while i != index:
            cur_node = cur_node.next
            i += 1
        cur_node.data = data

    def remove_duplicates(self):
        cur_node = self.head
        prev_node = None
        dic = {}
        while cur_node is not None:
            if cur_node.data in dic:
                prev_node.next = cur_node.next
            else:
                dic[cur_node.data] = 1
                prev_node = cur_node
            cur_node = cur_node.next


def merge(l1, l2):
    cur_node1 = l1.head
    cur_node2 = l2.head
    l3 = LinkedList()
    while True:
        if cur_node1 is None:
            while cur_node2.next is not None:
                l3.append(cur_node2.data)
                cur_node2 = cur_node2.next
            l3.append(cur_node2.data)
            break
        elif cur_node2 is None:
            while cur_node1.next is not None:
                l3.append(cur_node1.data)
                cur_node1 = cur_node1.next
            l3.append(cur_node1.data)
            break
        if cur_node1.data >= cur_node2.data:
            l3.append(cur_node2.data)
            cur_node2 = cur_node2.next
        elif cur_node1.data <= cur_node2.data:
            l3.append(cur_node1.data)
            cur_node1 = cur_node1.next
    return l3

# def merge(l1, l2):
#     cur_node1 = l1.head
#     cur_node2 = l2.head
#     l3 = LinkedList()
#     while cur_node1 is not None or cur_node2 is not None:
#         if cur_node1 is None or cur_node2 is not None and cur_node1.data > cur_node2.data:
#             l3.append(cur_node2.data)
#             cur_node2 = cur_node2.next
#         else:
#             l3.append(cur_node1.data)
#             cur_node1 = cur_node1.next
#     return l3


# ll1 = LinkedList()
# ll2 = LinkedList()
# ll1.append(1)
# ll1.append(5)
# ll1.append(7)
# ll1.append(9)
# ll1.append(10)
# ll2.append(2)
# ll2.append(3)
# ll2.append(4)
# ll2.append(6)
# ll2.append(8)
# ll3 = merge(ll1, ll2)
# ll3.print()

linked_list = LinkedList()
# linked_list.append(12)
# linked_list.append(23)
# linked_list.append(34)
# linked_list.append(45)
# linked_list.print()
# linked_list.prepend(1)
# linked_list.print()
# linked_list.append(56)
# linked_list.print()
# linked_list.insert_at_index(3, 67)
# linked_list.print()
# linked_list.remove_beginning()
# linked_list.print()
# linked_list.remove_end()
# linked_list.print()
# linked_list.remove(67)
# linked_list.print()
# linked_list.remove_at_index(2)
# linked_list.print()
# linked_list.update_element(2, 50)
# linked_list.print()
# linked_list.reverse()
# linked_list.print()
linked_list.append(1)
linked_list.append(6)
linked_list.append(1)
linked_list.append(4)
linked_list.append(2)
linked_list.append(2)
linked_list.append(4)
linked_list.print()
linked_list.remove_duplicates()
linked_list.print()
