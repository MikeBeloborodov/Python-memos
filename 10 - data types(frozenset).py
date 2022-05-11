# frozen set is just like set but it's immutable
# so in a normal set you can add and remove things
# but you can't change values
# in frozen set you can't add and remove


a = set()
a.add(1)
a.remove(1)

# frozenset takes an iterable data

b = frozenset([1, 2 ,3])
print(b)

# b.add and b.remove are not working