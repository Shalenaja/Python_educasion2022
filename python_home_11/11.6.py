# 6.Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла
# по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

import chardet


with open('test_file.txt', 'rb') as f:
    content_bytes = f.read()
    detected = chardet.detect(content_bytes)
    print(detected)
encoding = detected['encoding']
content_text = content_bytes.decode(encoding).split('\r')
print(content_text)
print()
with open('test_file.txt', encoding='utf-8') as f:
    content = f.read()
    print(content)
