"""Задача №5"""


# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов метод должен выводить уникальное сообщение. Создать экземпляры
# классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
         print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
         print('Пуск отрисовки.')


class Pencil(Stationery):
    def draw(self):
         print('Начало отрисовки.')


class Handle(Stationery):
    def draw(self):
         print('Отрисовка.')


a = Stationery('stationery')
print(a.title)
a.draw()
print('\n')

b = Pen('pen')
print(b.title)
b.draw()
print('\n')

c = Pencil('pencil')
print(c.title)
c.draw()
print('\n')

d = Handle('handle')
print(d.title)
d.draw()
