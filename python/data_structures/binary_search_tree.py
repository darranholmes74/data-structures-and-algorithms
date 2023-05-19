from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                else:
                    self.add(current.left, value)
            else:
                if value > current.value:
                    if current.right is None:
                        current.right = Node(value)
                    else:
                        self.add(current.right, value)
                else:
                    if value > current.value:
                        if current.right is None:
                            current.right = Node(value)
                        else:
                            self.add(current.right, value)

    def contains(self, value):
        """
        Returns True if the value is in the tree, False otherwise.
        """
        def walk(root):
            if root is None:
                return False
            elif root.value == value:
                return True
            elif value < root.value:
                return walk(root.left)
            else:
                return walk(root.right)
        return walk(self.root)
