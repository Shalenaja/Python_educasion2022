"""Задача №1"""

# Создать класс TrafficLight (светофор) и определить у него один атрибут color
# (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    def __init__(self, color):
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
obj = TrafficLight(color={"red": 7, "green": 2, "yellow": 5})
print(obj._TrafficLight__color)
obj.running()
