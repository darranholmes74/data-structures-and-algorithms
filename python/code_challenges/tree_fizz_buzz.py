import copy


def fizz_buzz_tree(tree):
    if not tree:
        return []

    copy_kary = copy.deepcopy(tree)

    def walk(node):
        if node.value % 5 == 0 and node.value % 3 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)
        for child in node.children:
            walk(child)

    walk(copy_kary.root)
    return copy_kary

