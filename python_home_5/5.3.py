"""Задание № 3"""


# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

from python_home_5.tunction import sum_num

my_f = open("with 3.txt", "r", encoding='utf-8')
wages = my_f.readlines()
print(wages)

a = []
b = []
s = []
for count, value in enumerate(wages):
    value = value.split()
    s.append(value[1])
    if float(value[1]) < 20000:
        a.append(value[0])
        b.append(value[1])
print(s)
people = count + 1
s_f = [float(i) for i in s]
s_w = round((sum_num(s_f)/(people)), 2)
print('\n')
print(f'менее 20000 руб. у сотрудников:{a}, соответственно:{b}')
print(f'средняя величина дохода на сотрудника составила:{s_w} рублей')

my_f.close()

