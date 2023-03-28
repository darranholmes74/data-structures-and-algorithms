class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __str__(self):

        while self.head is None:
            return f'{None}'

        while self.head is not None:
            return f"""{{ {self.head.value} }} -> {None}"""

        while self.head is not None:
            current = self.head
            new_current = self.head.next.value
            pre_value = self.head.value
            while current is pre_value:
                pre_value = new_current
            return f"""{{ {self.head.next.value} }} -> {{ {self.head.value} }} -> {None}"""

    def traverse_list(self):
        pass

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        pass


class Node:
    def __init__(self, value, _next=None):
        # value, next
        self.value = value
        self._next = _next
    # Node(3, node2)
    # Node.value = 3
    # Node._next = node2


class TargetError:
    pass


test = LinkedList()



