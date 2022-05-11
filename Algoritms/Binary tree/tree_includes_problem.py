from importlib import import_module
from typing import Literal
import time

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

target = "f"

def tree_uncludes_recursive(root: Node, target: Literal) -> bool:
    if not root: return False
    if root.value == str(target): return True
    return tree_uncludes_recursive(root.left, target) or tree_uncludes_recursive(root.right, target)

def tree_includes_iterative(root: Node, target: Literal) -> bool:
    if not root: return []
    queue = [root]
    while queue:
        current = queue.pop(0)  
        if current.value == target: return True
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return False

print(tree_includes_iterative(a, target))
print(tree_uncludes_recursive(a, target))
