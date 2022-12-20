"""Задание № 4"""


# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_f = open('with 4.txt', 'r', encoding='utf-8')
wttf = my_f.readlines()
print(wttf)
my_f_1 = open('with 4.new.txt', 'w', encoding='utf-8')

for value in wttf:
    if 'One' in value:
        value = 'Один - 1'
    elif 'Two' in value:
        value = 'Два - 2'
    elif 'Three' in value:
        value = 'Три - 3'
    elif 'Four' in value:
        value = 'Четыре - 4'
    my_f_1.writelines(value)
    my_f_1.writelines('\n')
    print(value)

my_f.close()
my_f_1.close()
