"""Задача 1.1 на оптимизацию времени"""


# оптимизация задачи №3 из Урока №3

from timeit import timeit

# Было:

from python_home_6.function import sum_big_value

if __name__ == "__main__":
    sum_big_value

print(timeit("sum_big_value", setup="from __main__ import sum_big_value",
                 number=1000))

# Новое решение_1:

def sum_big_value_new(arg_1, arg_2, arg_3):
    arr = [arg_1, arg_2, arg_3]
    a_mx = arr[0]
    a_mn = arr[0]
    a_mx_2 = arr[0]
    for i in range(len(arr)):
        if arr[i] > a_mx:
            a_mx = arr[i]
    for i in range(len(arr)):
        if arr[i] < a_mn:
            a_mn = arr[i]
    for i in range(len(arr)):
        if a_mn < arr[i] < a_mx:
            a_mx_2 = arr[i]
    return a_mx + a_mx_2

print(timeit("sum_big_value_new", globals=globals(), number=1000))

# Новое решение_2:

def get_max(*args):
    lst = list(args)
    i = 0
    res = 0
    while i != 2:
        max_val = max(lst)
        res += max_val
        lst.remove(max_val)
        i += 1

print(timeit("get_max", globals=globals(), number=1000))



