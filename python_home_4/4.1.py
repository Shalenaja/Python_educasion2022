"""Заадача №1"""


# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

from python_home_4.initial import wages

script_name, first_param, second_param, fhird_param = argv

print('Имя скрипта:', script_name)
print('выработка в часах:', first_param)
print('ставка в час:', second_param)
print('премия:', fhird_param)
a = int(first_param)
b = int(second_param)
c = int(fhird_param)
print(wages(a, b, c))