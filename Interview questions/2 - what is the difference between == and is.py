"""
== сравнивает значение операнда
is сравнивает адреса в памяти
"""

string1 = "hello"
string2 = "hello"

print(string1 == string2) # True
print(string1 is string2) # True

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2) # True
print(list1 is list2) # False