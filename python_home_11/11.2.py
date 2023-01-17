# Каждое из слов «class», «function», «method» записать в байтовом типе без
# преобразования в последовательность кодов (не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

f = 'class'
s = 'function'
t = 'method'
f_new = b'class'
s_new = b'function'
t_new = b'method'

list_my = [f_new, s_new, t_new]
for e in list_my:
    print(e, type(e), len(e))
