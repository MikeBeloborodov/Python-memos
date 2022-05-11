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

def breadth_first_values_iterative(root: Node):
    if not root: return []
    queue = [root]
    values = []
    while queue:
        current = queue.pop(0)  
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
        values.append(current.value)
    return values

# because breadth uses queue and not a stack, there is no easy way
# to implement a recursive solution
def breadth_first_values_recursive(root: Node):
    pass

values_breadth_iterative = breadth_first_values_iterative(a)
print(values_breadth_iterative)