"""Задача № 2"""


# Создать метакласс для паттерна Синглтон (см. конец вебинара)

class Meta_Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Meta_Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Meta_Singleton):
    pass


mc_1 = MyClass()
mc_2 = MyClass()
print('object 1', mc_1)
print('object 2', mc_2)
print(mc_1 is mc_2)
print(id(mc_1), id(mc_2))