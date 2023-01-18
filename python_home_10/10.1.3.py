"""Задача № 1.3"""


# Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ

# по заданию №1 урока №7:

from time import sleep


class NonNegative:
    def __set__(self, instance, value):
        a = []
        for key, el in value.items():
            a.append(key)
            if key not in ('red', 'yellow', 'green'):
                raise ValueError("цвет не соответствует палитре")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class TrafficLight:
    color = NonNegative()

    def __init__(self, color):
        a = []
        for key, value in color.items():
            a.append(key)
            if key not in ('red', 'yellow', 'green'):
                raise ValueError("цвет не соответствует палитре")
        self.__color = color

    def running(self):
        a = []
        for key, value in self.__color.items():
            a.append(key)
        for i in range(len(a)):
            if a[0] == "yellow" or a[0] == "green" \
                    or a[len(a) - 1] == "yellow":
                print('неверная последовательность. выход')
                exit()
            else:
                print('верная последовательность!')
                for key, value in self.__color.items():
                    print(key)
                    sleep(value)
                break

obj = TrafficLight(color={"red": 7, "yellow": 2, "green": 5})
print(obj._TrafficLight__color)
obj.running()
print('\n')
obj = TrafficLight(color={"red": 7, "yellow": 2, "blue": 5})
print(obj._TrafficLight__color)
obj.running()