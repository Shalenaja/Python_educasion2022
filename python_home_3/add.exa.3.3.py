"""Дополнительня задача № 3"""


# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def diff_max_min(arr):
    """ функция находит разницу между максимальным и минимальным значениями
    элементов

    :param arr: список, в котором нужно произвести операцию
    :return: значение разницы
    """
    a = arr[0]
    b = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > a:
            a = arr[i]
        if arr[i] < b:
            b = arr[i]
        i += 1
    return a - b


def fractional_num(num):
    num = round(num - int(num), 2)
    return num


m = list(map(float, input('Введите несколько чисел через пробел:').split()))
res_1 = []
for el in m:
    res_1.append(fractional_num(el))
res_2 = []
for el in res_1:
    if el != 0:
        res_2.append(el)
print(diff_max_min(res_2))
