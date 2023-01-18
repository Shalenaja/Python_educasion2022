"""Тестирование функции из задачи №3 Урока №3"""


# с использованием assert:

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


def test_sum_big_value():
    assert sum_big_value(2, 6, 8) == 14, 'неверно'


def test_get_max():
    assert get_max(2, 6, 8) == 14, 'неверно'


if __name__ == "__main__":
    test_sum_big_value()
    test_get_max()
