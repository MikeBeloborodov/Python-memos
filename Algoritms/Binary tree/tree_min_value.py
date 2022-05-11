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
e = Node(4)
f = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def tree_min_value(root: Node) -> int:
    if not root: return 0
    min_value = Infinity
    stack = [root]
    while stack:
        current = stack.pop()
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
        if current.value < min_value: min_value = current.value
    return min_value

def tree_min_value_recursion(root: Node) -> int:
    if not root: return Infinity
    min_value_left = tree_min_value_recursion(root.left)
    min_value_right = tree_min_value_recursion(root.right)
    return min(root.value, min_value_left, min_value_right)

print(tree_min_value(a))
print(tree_min_value_recursion(a))