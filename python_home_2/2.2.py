"""Задача 2"""
# Для списка реализовать обмен значений соседних элементов, т.е. значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

arr = list(map(int, input('Введите несколько чисел через пробел: ').split()))
print(arr)
for el in range(0, len(arr) - 1, 2):
    arr[el], arr[el + 1] = arr[el + 1], arr[el]
print(arr)
