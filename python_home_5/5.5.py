"""Задание № 5"""


# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.

from python_home_5.tunction import sum_num


my_f = open('with 5.txt', 'w', encoding='utf-8')
n = input('Введите числа через пробел:').split()
my_f.writelines(f'{n}')
print(n)

s = [int(i) for i in n]
print(sum_num(s))

my_f.close()
