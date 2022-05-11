"""
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""

print(10 > 9) # true
print(10 == 9) # false
print(10 < 9) # false


# When you run a condition in an if statement, Python returns True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# The bool() function allows you to evaluate any value, and give you True or False in return,

# Evaluate a string and a number:

print(bool("Hello")) # result - True
print(bool(15))  # result - True

print(bool(0)) # result - False !!!!!!!!!!!!!


# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x)) # result - True
print(bool(y)) # result - True

"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

Example

"""

print(bool("")) # false 

# The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


bool(False) # false 
bool(None) # false 
bool(0) # false 
bool("") # false 
bool(()) # false 
bool([]) # false 
bool({}) # false 


# !!!!!!!!!!!!!!!! There is also another false object !!!!!!!!!!!!!   def __len__(self):
