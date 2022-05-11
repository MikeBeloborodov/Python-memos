class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def depth_first_values_iterative(root: Node):
    if not root: return []
    stack = [root]
    values = []
    while stack:
        current = stack.pop()
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
        values.append(current.value)
    return values

def depth_first_values_recursive(root: Node):
    if not root: return []
    left_node = depth_first_values_recursive(root.left)
    right_node = depth_first_values_recursive(root.right)
    return [root.value] + left_node + right_node

values_result_iterative = depth_first_values_iterative(a)

print(f"Iterative version: {values_result_iterative}")

values_result_recursive = depth_first_values_recursive(a)

print(f"Recursive version: {values_result_recursive}")