"""Задача №3"""


# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
# """
# """

class Divide:
    def __init__(self, divisible, divider):
        self.divisible = divisible
        self.divider = divider

    def divide_by_zero(self):
        try:
            self.divisible / self.divider
        except ZeroDivisionError:
            print("вы ввели делитель = 0.Делить на ноль нельзя")
        else:
            print(f'результат деления {self.divisible} на {self.divider}'
                  f'= {self.divisible / self.divider}')
        finally:
            print("Программа завершена")


dm = int(input('Введите число-делимое:'))
dl = int(input('Введите число-делитель:'))
div = Divide(dm, dl)
print(div.divisible, div.divider)
div.divide_by_zero()
