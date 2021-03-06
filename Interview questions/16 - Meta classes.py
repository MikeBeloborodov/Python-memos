"""
Если классы являются шаблонами для объектов, то метаклассы являются шаблонами
для классов. На основе метаклассов строятся классы. Использовать их нужно
с осторожностью.
Метаклассы используются для перехвата создания классов и как-то его изменить.

В метаклассах 4 метода: new, init, prepare, call

prepare подготавливает данные
данные попадают в new, который создаёт класс
init отвечает за инициализацию
call отвечает за создание объекта класса

чаще всего используется new, потому что нам зачастую интересно перехватить
создание класса и что-то в нем поменять
"""

# как реализовать на пайтоне?

# если хотим метакласс с абстракциями наследуем от ABCMeta

from abc import ABCMeta


class OneMeta(ABCMeta):
    pass

# если хотим обычный метакласс, то наследуем от type
# type это базовый метакласс
# тут мы можем перегружать магию
class TwoMeta(type):
    def __new__(msc, name, bases, attrs):
        pass