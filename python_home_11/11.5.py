# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
# из байтовового в строковый тип на кириллице.

import subprocess
import chardet


yandex = ['ping', 'yandex.ru']
subp_ping = subprocess.Popen(yandex, stdout=subprocess.PIPE)
print(subp_ping.stdout)
for byte in subp_ping.stdout:
    result = chardet.detect(byte)
    byte = byte.decode(result['encoding'])
    print(byte)

youtube = ['ping', 'youtube.com']
subp_ping = subprocess.Popen(youtube, stdout=subprocess.PIPE)
print(subp_ping.stdout)
for byte in subp_ping.stdout:
    result = chardet.detect(byte)
    byte = byte.decode(result['encoding'])
    print(byte)
