"""Задача 2.1 на оптимизацию памяти"""


# оптимизация задачи №3 из Урока №2 (решение через dict)

from json import dumps
from pympler import asizeof

# Было:

n = int(input('Вводите месяц в виде целого числа от 1 до 12: '))
my_dict = {"key_1": "winter", "key_2": "spring", "key_3": "summer",
           "key_4": "autumn"}
if n == 12 or n == 1 or n == 2:
    print(my_dict['key_1'])
elif n == 3 or n == 4 or n == 5:
    print(my_dict["key_2"])
elif n == 6 or n == 7 or n == 8:
    print(my_dict.get("key_3"))
elif n == 9 or n == 10 or n == 11:
    print(my_dict.get("key_4"))
else:
    print('нет такого месяца')

print('Размер dict: ', asizeof.asizeof(my_dict))

# Стало:

n = int(input('Вводите месяц в виде целого числа от 1 до 12: '))
my_dict = {"key_1": "winter", "key_2": "spring", "key_3": "summer",
           "key_4": "autumn"}
dumped_my_dict = dumps(my_dict) # словарь записан в виде строки
if n == 12 or n == 1 or n == 2:
    print(my_dict['key_1'])
elif n == 3 or n == 4 or n == 5:
    print(my_dict["key_2"])
elif n == 6 or n == 7 or n == 8:
    print(my_dict.get("key_3"))
elif n == 9 or n == 10 or n == 11:
    print(my_dict.get("key_4"))
else:
    print('нет такого месяца')

print('Размер json: ', asizeof.asizeof(dumped_my_dict))


