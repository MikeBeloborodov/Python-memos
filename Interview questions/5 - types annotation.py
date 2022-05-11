"""
Аннотации типов это подсказки к аргументам, переменным, функциям.
Аннотации это не строгая типизация, а подсказка для программиста, читающего код

Если нужно проверить типы, нужно использовать библиотеки pydentic...
"""

my_var : int = 10

def my_func(number: int, arg_string: str) -> list:
    return [number, arg_string]