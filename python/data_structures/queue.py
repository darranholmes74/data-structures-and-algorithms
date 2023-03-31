from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

# class InvalidOperationError(Exception):
#     pass


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None):
        self.front = front
        self.back = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        # adding to the back of the queue
        # if the queue is empty, the new node becomes the front and the back.
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.back.next = node
        # check if the queue is empty
        # self.back.next = node
        self.back = node
        self.size += 1
        # if not self.front:
        #     self.front = node

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Cannot dequeue from an empty queue")

        result = self.front.value
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.back = None
        return result

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Cannot peek an empty queue")
        return self.front.value
