class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        print(self.items[-1])

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def length(self):
        return len(self.items)

    def print_stack(self):
        print(self.items)
