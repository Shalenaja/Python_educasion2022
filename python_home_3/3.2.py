"""Задача № 2"""


# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать
# вывод данных о пользователе одной строкой.

def user_data(name, surname, year_birth, city, email, telephone):
    return f'{name}; {surname}; {year_birth}; {city}; {email}; {telephone}'


print(user_data(name='anna', surname='sh', year_birth='01.01.01', city='SPb',
                email='1245hfd.mail.ru', telephone=9218888888))
