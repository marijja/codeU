def print_ancestors(node, searched_node):
    if node == None:
        return False

    if node._data == searched_node:
        print(searched_node)
        return True

    if node._left == None and node._right == None:
        return False

    should_print = print_ancestors(node._left, searched_node)

    if not should_print:
        should_print = print_ancestors(node._right, searched_node)

    if should_print:
        print(node._data)

    return should_print

