from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree_a, tree_b):

    ht = Hashtable()

    def add_to_ht(node):
        if node:
            ht.set(node.value, None)
            add_to_ht(node.left)
            add_to_ht(node.right)

    def check(node, result):
        if node:
            if ht.has(node.value):
                result.append(node.value)
            check(node.left, result)
            check(node.right, result)

    add_to_ht(tree_a.root)

    result = []
    check(tree_b.root, result)

    return result

