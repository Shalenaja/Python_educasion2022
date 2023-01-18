"""Тестирование функции из задачи №1 Урока №3"""

# на базе unittest:

import unittest


def divide_num(var_a, var_b):
    if var_b == 0:
        print('Делить на ноль нельзя!')
        exit()
    else:
        return var_a / var_b


class TestMyFunction(unittest.TestCase):
    def testequal(self):
        self.assertEqual(divide_num(20, 5), 4)

    def testnotequal(self):
        self.assertNotEqual(divide_num(20, 5), 6)

    def testtrue(self):
        self.assertTrue(4)

    def testin(self):
        self.assertIn(4, [1, 4, 10, 12])

    def testnotin(self):
        self.assertNotIn(4, [0, 2, 3])

    def testraises(self):
        with self.assertRaises(Exception):
            20 / 0


if __name__ == '__main__':
    unittest.main()
