"""Задача 4"""
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

arr = list(input('Введите несколько слов через пробел: ').split())
print(arr)
for i, el in enumerate(arr):
    if len(el) >= 10:
        el = el[:10]
    if len(el) < 10:
        el = el[:]
    print(i + 1, el)
