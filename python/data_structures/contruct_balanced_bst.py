from data_structures.binary_search_tree import BinarySearchTree
# from data_structures.binary_tree import BinaryTree

def construct_balanced_bst(values):
    if not values:
        return None

    mid = len(values) // 2
    root = BinarySearchTree(values[mid])

    root.left = construct_balanced_bst(values[:mid])
    root.right = construct_balanced_bst(values[mid + 1:])

    return root


values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root = construct_balanced_bst(values)

# Printing the tree in in-order traversal for verification
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=" ")
        in_order_traversal(node.right)

in_order_traversal(root)  # Output: 1 2 3 4 5 6 7 8 9
