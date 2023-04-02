class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        if self.head is None:
            return f'{None}'

        current = self.head
        llstr = ''

        while current:
            llstr += '{ ' + str(current.value) + ' }' + ' -> '
            current = current.next

        if current is None:
            llstr += '' + str(None)

        return llstr

    def insert(self, value):
        node = Node(value, self.head)
        if self.head is not None:
            node._next = self.head
            self.head = node
        self.head = node

    def includes(self, value):
        itr = self.head
        while itr:
            if itr.value == value:
                return True
            else:
                itr = itr.next

            continue

    def append(self, new_value):
        # node = Node(new_value)
        if self.head is None:
            self.head = Node(new_value)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(new_value)

    def insert_before(self, value1, value2):
        if self.head is None:
            raise TargetError("Nothing")
            self.head = Node(value2)
            return

        if self.head.value == value1:
            self.head = Node(value2, self.head)
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value1:
                current.next = Node(value2, current.next)
                return
            current = current.next

        raise TargetError("Nothing")

    def insert_after(self, value1, value2):
        if self.head is None:
            raise TargetError("Nothing")
            self.head = Node(value2)
            return
        current = self.head
        while current is not None:
            if current.value == value1:
                new_node = Node(value2)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        raise TargetError("Nothing")





class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class TargetError(Exception):
    pass


if __name__ == '__main__':
    test = LinkedList()
    test.insert("apple")
    test.insert("banana")
    test.append("cucumber")
    test.insert_before("apple", "cucumber")
    print(test)
    test.__str__()





