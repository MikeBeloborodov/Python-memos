"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

"""


# example create a list

thislist = ["apple", "banana", "cherry"]
print(thislist)

"""
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
"""


"""
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
"""


"""
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
"""

"""
Since lists are indexed, lists can have items with the same value:
"""

# To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#From Python's perspective, lists are defined as objects with the data type 'list':

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)





# our example

class Color:
    def __init__(self, bright, color_name):
      self.bright = bright 
      self.color_name = color_name

    def print_color_name(self):
        print(self.color_name)

blue_steel = Color(True, "Blue steel")
print(blue_steel.color_name)
list_huini = ["Obama", 54, False, blue_steel]

for item in list_huini:
    if type(item) == type(blue_steel):
        item.print_color_name()
    else:
        print(item)
