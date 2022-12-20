"""Задание № 2"""


# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_f = open('with 2.txt', 'r', encoding='utf-8')
poem = my_f.readlines()
print(poem)

for count, value in enumerate(poem):
    if count == 0:
       count = 1
    else:
        count += 1
    a = len(value.split())
    print(f'{count} {value} слов в строке:{a}')

my_f.close()
