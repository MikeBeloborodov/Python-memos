"""
В пайтоне нет модификаторов доступа как в плюсах или си, но есть договоренность,
что если у меня есть некий атрибут с обычным именем, то это public атрибут, и все
атрибуты в пайтоне по умолчанию публичные.

protected атрибуты доступны в классе и его дочках, 
имеют перед собой одно подчеркивание, однако эта вещь
все равно будет доступна

private атрибуты доступны только внутри одного класса, имеют перед собой
два подчеркивания   
"""

class My_class:
    public_attr = 1 # public attribute
    _protected_attribute = 2 # protected attribute
    __private_attribute = 3 # private attribute

inst_of_my_class = My_class()
inst_of_my_class.public_attr
inst_of_my_class._protected_attribute
# inst_of_my_class.__private_attribute    # это выдаст ошибку
inst_of_my_class._My_class__private_attribute   # подчеркивание, имя класса, имя атрибута не выдаст ошибку
