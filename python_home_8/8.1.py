"""Задача №1"""


# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# [[], [], []]
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода add() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, my_list_of_lists):
        self.matrix = my_list_of_lists

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):
        other = Matrix(other)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[i][j] + other[i][j], '\t', end='')
            print()


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m_1)
print()
print(m_2)
print()
m_1 + m_2
