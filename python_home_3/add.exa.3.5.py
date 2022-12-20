"""Дополнительня задача № 5"""


# Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
# Пример:- для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib_positive(m):
    f1 = 0
    f2 = 1
    i = 1
    b = [1]
    while i < m:
        f_sum = f1 + f2
        f1 = f2
        f2 = f_sum
        i = i + 1
        b.append(f2)
    return b


n = int(input('введите число:'))
if n > 0:
    print(fib_positive(n))
else:
    n = n * -1
    a = fib_positive(n)
    a.reverse()
    for i in range(0, len(a)-1):
        a[i] = a[i] * -1
    a.append(0)
    print(a + fib_positive(n))