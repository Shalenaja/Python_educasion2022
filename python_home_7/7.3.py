"""Задача №3"""


# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        a =[]
        for key, value in self._income.items():
            a.append(int(value))
            s = sum(a)
        print(f'заработная плата с учетом премии: {s} рублей')


human = Position('ivan', 'ivanov', 'programmer',
                 income={"wage": '2000', "bonus": '500'})
print(human.name, human.surname, human.position)
human.get_full_name()
human.get_total_income()
print('\n')
b = Position('petr', 'petrov', 'programmer',
             income={"wage": '3000', "bonus": '1000'})
print(b.name, b.surname, b.position)
b.get_full_name()
b.get_total_income()
