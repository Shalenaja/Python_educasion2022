"""Дополнительные задания № 3"""


# Реализуйте алгоритм перемешивания списка.

import random

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr, '\n')
for i in range(len(arr)):
    index_i = random.randint(0, len(arr) - 1)
    temp = arr[i]
    arr[i] = arr[index_i]
    arr[index_i] = temp
print(arr)

