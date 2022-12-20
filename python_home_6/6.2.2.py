"""Задача 2.2 на оптимизацию памяти"""


# оптимизация задачи №4 из Урока №4

from pympler import asizeof
from numpy import array

# Было:

arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
a = []
gen = (arr[i] for i in range(len(arr)) if arr.count(arr[i]) == 1)
for i in gen:
    a.append(i)
print(a)

print(asizeof.asizeof(a))
print(type(a))

# Стало:

arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
arr_new = array(arr)
a = []
gen = (arr[i] for i in range(len(arr)) if arr.count(arr[i]) == 1)
for i in gen:
    a.append(i)
a_new = array(a) # лист передан в функцию array для его изменения в объект numpy.ndarray
print(a)

print(asizeof.asizeof(a_new))
print(type(a_new))

