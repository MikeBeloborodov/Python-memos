"""
Декоратор это паттерн проектирования, по канону реализуется через класс,
с помощью этого класса меняется поведение какого-то кода, без изменения
исходного кода

функции в пайтоне это объекты, как и любая сущность в пайтоне
поэтому их можно хранить в переменных, пробрасывать в другие функции

функция может принимать функцию и возвращать функцию

декораторы - синтаксический сахар
"""

def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def some_func():
    pass

def some_func2():
    pass

decorated_some_func2 = my_decorator(some_func2) # декорируем без сахара


"""
Можно сделать декоратор, который будет считать время всех функций
"""

import time

def timer_decor(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start
        print(end_time)
        return result
    return wrapper

@timer_decor
def test_func():
    for i in range(1, 1000):
        [x*2 for x in range(1, 1000)]

@timer_decor
def test_func_2():
    time.sleep(2)

test_func()
test_func_2()