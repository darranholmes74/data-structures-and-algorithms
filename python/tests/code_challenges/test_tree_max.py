from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value(30)
    expected = 30

    assert actual == expected


def test_max_val2():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(1)
    tree.root.right = Node(-20)
    tree.root.right = Node(20)

    actual = tree.find_maximum_value(20)
    expected = 20

    assert actual == expected


def test_max_val3():
    tree = BinaryTree()
    tree.root = Node(-4)
    tree.root.left = Node(-12)
    tree.root.left = Node(-20)
    tree.root.right = Node(-2)

    actual = tree.find_maximum_value(-2)
    expected = -2

    assert actual == expected
