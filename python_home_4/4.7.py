"""Заадача №7"""


# Реализовать генератор с помощью функции с ключевым словом yield, создающим
# очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24

from itertools import count

def num_factorial(m):
    f = 1
    for i in gener(m):
        f = f * i
    for i in count(1):
        if i > m:
            break
        else:
            print(i)
    return(f)

def gener(num):
    gen = (i for i in range(1, num + 1))
    for i in gen:
        yield i


x = int(input('введите число для нахождения факториала:'))
print(f'факториал числа {x}! = {num_factorial(x)}')
