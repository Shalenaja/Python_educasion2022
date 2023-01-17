# 3. Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе.

list_my = ['attribute', 'класс', 'функция', 'type']
for el in list_my:
    try:
        el.encode('ascii')
    except:
        print(el, '- невозможно записать в байтовом типе')
