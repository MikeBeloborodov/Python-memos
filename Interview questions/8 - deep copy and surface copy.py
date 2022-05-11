"""
Поверхностная копия копирует внешний объект (даёт им новый адрес в памяти), 
но внутренние объекты передаёт по ссылкам

Глубокое копирование копирует и внешний объект и внутренние объекты
"""

import copy

some_list = [1, [2], 3]

print(some_list is copy.copy(some_list)) # False

print(some_list[1] is copy.copy(some_list)[1]) # True

print(some_list is copy.deepcopy(some_list)) # False

print(some_list[1] is copy.deepcopy(some_list)[1]) # False