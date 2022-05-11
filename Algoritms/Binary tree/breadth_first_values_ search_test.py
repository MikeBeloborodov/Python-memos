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
    # let's return all the values
    values = []
    # let's search for 2 targets 
    target1 = 'd'
    target1_search = False
    target2 = 'f'
    target2_search = False
    target1_node = ''
    target2_node = ''

    while queue:
        current = queue.pop(0)  
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
        values.append(current.value)
        if current.left and current.left.value == target2:
            target2_node = current.value
            target2_search = True
        if current.right and current.right.value == target2:
            target2_node = current.value
            target2_search = True
        if current.left and current.left.value == target1:
            target1_node = current.value
            target1_search = True
        if current.right and current.right.value == target1:
            target1_node = current.value
            target1_search = True

    return {"values" : values,
     "target 1" : {"searched value" : target1, "is it there" : target1_search, "parent_node" : target1_node},
     "target 2" : {"searched value" : target2, "is it there" : target2_search, "parent_node" : target2_node}}

# because breadth uses queue and not a stack, there is no easy way
# to implement a recursive solution
def breadth_first_values_recursive(root: Node):
    pass

values_breadth_iterative = breadth_first_values_iterative(a)
for info in values_breadth_iterative:
    if type(values_breadth_iterative.get(info)) is dict:
        print(f"{info}: ")
        for item in values_breadth_iterative.get(info):
            print(f"{item} : {values_breadth_iterative.get(info).get(item)}")
    else:
        print(f"{info} : {values_breadth_iterative.get(info)}")
    