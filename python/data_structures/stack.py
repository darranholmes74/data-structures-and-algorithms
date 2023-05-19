from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        # initialization here
        self.top = top

    def push(self, value):
        # method body here
        node = Node(value)
        node._next = self.top
        self.top = node



    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            value = self.top.value
            self.top = self.top._next
            return value

    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        try:
            self.peek()
            return False
        except InvalidOperationError:
            return True

