"""Задача 2.3 на оптимизацию памяти"""


# оптимизация функции из задачи №7 из Урока №4

'''
Перебрала все функции из предыдущих уроков, при проверке результат у всех 
один и тот же - память на вход и выход одинаковая. Ниже одна из функций 
с проверкой памяти. Работа по проверке и желанию улучшить функции проводилась!
'''

from itertools import count

from memory_profiler import profile

@profile
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

num_factorial(5)

num_factorial