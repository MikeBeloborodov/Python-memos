"""
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.


A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)


"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# illegal varibale names
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

# camel case
myVariableName = "John"

#pascal case
MyVariableName = "John"

#snake case
my_variable_name = "John"

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# result: Orange Banana Cherry


# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)
# result Orange Orange Orange