# 1.Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
# формате и проверить тип и содержание соответствующих переменных. Затем с помощью
# онлайн-конвертера преобразовать строковые представление в формат Unicode и
# также проверить тип и содержимое переменных.

list_my = ['разработка', 'сокет', 'декоратор']
for e in list_my:
    print(e, type(e))

for el in list_my:
    e_new = str(el.encode())
    print(e_new, type(e_new))
