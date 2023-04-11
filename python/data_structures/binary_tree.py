class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        # initialization here
        self.root = root

    def pre_order(self, values=[]):
        # method body here
        def walk(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def in_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            value_list.append(input_node.value)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def post_order(self, values = []):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
            value_list.append(input_node.value)

        walk(self.root, values)
        return values

    def find_maximum_value(self, value=[]):
        def walk(root, max_value):
            if root is None:
                return
            elif root.value > max_value:
                max_value[0] = root.value
            walk(root.left, max_value)
            walk(root.right, max_value)

        max_value = [value]
        walk(self.root, value)
        return max_value[0]

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
