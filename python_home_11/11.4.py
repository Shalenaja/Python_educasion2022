# 4. Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить обратное
# преобразование (используя методы encode и decode).

list_my = ['разработка', 'администрирование', 'protocol']
list_my_new = []
for e in list_my:
    e_new = e.encode()
    print(e_new, type(e_new))
    list_my_new.append(e_new)
print(list_my_new)
print()
list_my_back = []
for e_new in list_my_new:
    e_back = e_new.decode()
    print(e_back, type(e_back))
    list_my_back.append(e_back)
print(list_my_back)
