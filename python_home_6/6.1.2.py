"""Задача 1.2 на оптимизацию времени"""


# оптимизация задачи №1 из Урока №2

from timeit import timeit

# Было:

print(timeit("""list = [1.1, 25, 5, 'element', 2.5, 'PEP 8']
for item in list:
    print(item, " ", end='')
    print(type(item))""", number=10))

print('\n')

# Стало:
'''Вместо листа данные представлены в кортеже'''

print(timeit("""list = (1.1, 25, 5, 'element', 2.5, 'PEP 8') 
for item in list:
    print(item, " ", end='')   
    print(type(item))""", number=10))

