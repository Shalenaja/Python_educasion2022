"""Дополнительные задания № 1"""
# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('Ведите вещественное число:'))
a = int(number)
b = round(number - int(number), 2)
c = 0
print(a, b)
while a != 0:
    c = c + (a % 10)
    a = a // 10
while b != 0:
    c = c + int(b * 10)
    b = b * 10 - int(b * 10)
print(c)