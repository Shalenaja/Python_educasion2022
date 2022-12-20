"""Задача 3"""


# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum_big_value(arg_1, arg_2, arg_3):
    a = 0
    if arg_1 > arg_2 or arg_1 > arg_3:
        a += arg_1
    else:
        return arg_2 + arg_3

    if arg_2 > arg_3:
        return arg_1 + arg_2
    else:
        return arg_1 + arg_3


print(sum_big_value(5, 1, 4))
