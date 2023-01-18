"""Тестирование функции из задачи №3 Урока №3"""

# на базе unittest:
# с использованием assertEqual:

import unittest


def sum_big_value(arg_1, arg_2, arg_3):
    a = 0
    if arg_1 > arg_2 or arg_1 > arg_3:
        a += arg_1
    else:
        return arg_2 + arg_3

    if arg_2 > arg_3:
        return arg_1 + arg_2
    else:
        return arg_1 + arg_3


def get_max(*args):
    lst = list(args)
    i = 0
    res = 0
    while i != 2:
        max_val = max(lst)
        res += max_val
        lst.remove(max_val)
        i += 1
    return res


class TestGetMax(unittest.TestCase):
    def test_sum_big_value(self):
        self.assertEqual(sum_big_value(2, 6, 8), 14)

    def test_get_max(self):
        self.assertEqual(get_max(2, 6, 8), 14)


if __name__ == "__main__":
    unittest.main()
