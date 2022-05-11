# Strings

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

#You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)



"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""

#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1]) # result e




"""
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""

sentence = "Heldlo world"
twoLetters = ""
counter = 0

for letter in sentence:
    if (counter % 2 != 0):
        twoLetters = twoLetters + letter
        print(twoLetters)
        twoLetters = ""
    else:
        twoLetters = twoLetters + letter
    counter = counter + 1
    if(len(sentence) % 2 != 0):
        if(counter == len(sentence)):
            print(letter)


sentence2 = "Big red dog"

print(sentence2) #full
print(sentence2[0]) #B
print(sentence2[3]) #space
print(len(sentence2)) #10
print(sentence2[len(sentence2) - 1]) #g

# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)



my_favorite_animal = "cat"
the_worst_animal = "dog"

test_str = "The best animal is the Dog of course!"

while True:
    user_input = input("Enter text: ")
    user_input = user_input.casefold()
    the_worst_animal_start = user_input.find(the_worst_animal) # coordinates (int)
    the_worst_animal_end = the_worst_animal_start + len(the_worst_animal)
    if the_worst_animal_start != -1: 
        print(user_input[:the_worst_animal_start] + my_favorite_animal + user_input[the_worst_animal_end:])

