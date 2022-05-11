from numpy import Infinity


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node(11)
b = Node(5)
c = Node(3)
d = Node(2)
e = Node(10)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

"""
def max_root_to_leaf_path_iterative(root: Node) -> int:
    if not root: return Infinity
    stack = [root]
    current_path = 0
    max_path_to_leaf = 0
    while stack:
        current = stack.pop()
        current_path += current.value
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
        if not current.left and not current.right:
            if max_path_to_leaf < current_path:
                max_path_to_leaf = current_path
                current_path -= current.value
    return max_path_to_leaf
    """

def max_root_to_leaf_path_recursive(root: Node) -> int:
    if not root: return -Infinity
    if root.left == None and root.right == None: return root.value
    max_value = max(max_root_to_leaf_path_recursive(root.left), max_root_to_leaf_path_recursive(root.right))
    return root.value + max_value

print(max_root_to_leaf_path_recursive(a))

