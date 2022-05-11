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

def tree_sum_recursion(root: Node) -> int:
    if not root: return 0
    return root.value + tree_sum_recursion(root.left) + tree_sum_recursion(root.right)

def tree_sum_iterative(root: Node) -> int:
    if not root: return 0
    stack = [root]
    value_sum = 0
    while stack:
        current = stack.pop()
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
        value_sum += current.value
    return value_sum

print(tree_sum_recursion(a))
print(tree_sum_iterative(a))