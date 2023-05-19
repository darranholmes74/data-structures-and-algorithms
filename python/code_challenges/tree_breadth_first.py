def breadth_first(tree):
    if tree.root is None:
        return []

    queue = []
    queue.append(tree.root)

    result = []
    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.value)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return result




