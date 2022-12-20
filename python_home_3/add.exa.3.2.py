"""Дополнительня задача № 2"""


# Напишите программу, которая найдёт произведение пар чисел списка. Парой
# считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

arr = list(map(int, input('Введите несколько чисел:').split()))
print(arr)
s = 0
res = []
if len(arr)% 2 == 0:
    for el in range(0, len(arr)//2):
        s = arr[el] * arr[len(arr)-el-1]
        res.append(s)
        el += 1
else:
    for el in range(0, len(arr)//2 + 1):
        s = arr[el] * arr[len(arr)-el-1]
        res.append(s)
        el += 1
print(res)
