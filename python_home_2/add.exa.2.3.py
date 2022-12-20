"""Дополнительные задания № 3"""
# Реализуйте алгоритм перемешивания списка.

import random

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr, '\n')
for el in range(len(arr)):
    index_al = random.randint(0, len(arr) - 1)
    temp = arr[el]
    arr[el] = arr[index_al]
    arr[index_al] = temp
print(arr)

# ИЛИ:

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for el in a:
    random.shuffle(a)
print(a)
