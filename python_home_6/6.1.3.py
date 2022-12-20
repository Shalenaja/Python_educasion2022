"""Задача 1.1 на оптимизацию времени"""


# оптимизация задачи №3 из Урока №2

from timeit import timeit

# Для тестирования, значение n принято равным 11. Его можно менять.

print(timeit("""n = 11
wi = [12, 1, 2]
sp = [3, 4, 5]
su = [6, 7, 8]
au = [9, 10, 11]

if n in wi:
    print('зима')
elif n in sp:
    print('весна')
elif n in su:
    print('лето')
elif n in au:
    print('осень')
else:
    print('нет такого месяца')""", number=10))

# Второе решение реализовано через создание справочника. Оно более быстрое.

print(timeit("""n = 11
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
    print('нет такого месяца')""", number=10))



