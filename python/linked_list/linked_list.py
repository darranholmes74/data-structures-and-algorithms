class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        if self.head is None:
            return f'{None}'

        itr = self.head
        llstr = ''

        while itr:
            llstr += '{ ' + str(itr.value) + ' }' + ' -> '
            itr = itr._next

            if itr is None:
                llstr += '' + str(None)

        return llstr



    def traverse_list(self):
        pass

    def insert(self, value):
        node = Node(value, self.head)
        self.head = node

    def includes(self, value):
        itr = self.head
        while itr:
            if itr.value == value:
                return True
            else:
                itr = itr._next
            continue


class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next



class TargetError:
    pass


if __name__ == '__main__':
    test = LinkedList()
    test.insert(5)
    test.__str__()






