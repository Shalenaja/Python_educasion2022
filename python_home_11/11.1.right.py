# 1.Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
# формате и проверить тип и содержание соответствующих переменных. Затем с помощью
# онлайн-конвертера преобразовать строковые представление в формат Unicode и
# также проверить тип и содержимое переменных.

list_my = ['разработка', 'сокет', 'декоратор']
for e in list_my:
    print(e, type(e))
print()
e_new1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
e_new2 = '\u0441\u043e\u043a\u0435\u0442'
e_new3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
list_my_new = [e_new1, e_new2, e_new3]
for e in list_my_new:
    print(e, type(e))