from data_structures.binary_tree import BinaryTree


def breadth_first(tree):
    def walk(root, front, rear):
        if root is None:
            return None
        if root.value is not None:
            root.value == front
            walk(root.left)
            walk(root.right)
        if root.left is not None:
            front == root.left
            tree.append(front)
        if root.right is not None:
            rear == root.left
            tree.append(rear)

        return walk(root, front, rear)

