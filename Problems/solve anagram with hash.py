# check if these are anagrams (if they have the same
# letters with the same frequency)

input_1 = "nameless"
input_2 = "salesmen"

# it's nice to use hash (key and values) to solve this problem

# key is the letter and value is it's appearence frequency

def make_input_dict(user_input: str) -> dict:
    dict_input = {}
    for letter in user_input:
        try:
            dict_input[letter] += 1
        except:
            dict_input.update({letter : 1})
    return dict_input


#another variant

def are_anagrams(str_1: str, str_2: str) -> bool:
    if len(str_1) != len(str_2): return False
    dict_1 = {}
    dict_2 = {}
    for char in str_1:
        if char in dict_1: dict_1[char] += 1
        else: dict_1[char] = 1
    for char in str_2:
        if char in dict_2: dict_2[char] += 1
        else: dict_2[char] = 1
    return dict_1 == dict_2

input_3 = "accountant"
input_4 = "accumulate"
print(make_input_dict(input_1) == make_input_dict(input_2)) # True
print(make_input_dict(input_3) == make_input_dict(input_4)) # False

print(are_anagrams(input_1, input_2))
print(are_anagrams(input_3, input_4))