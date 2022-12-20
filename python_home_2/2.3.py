"""Задача 3"""
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
# времени года относится месяц (зима, весна, лето, осень). Напишите решения
# через list и через dict.

n = int(input('Вводите месяц в виде целого числа от 1 до 12: '))
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
    print('нет такого месяца')

# через dict

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
