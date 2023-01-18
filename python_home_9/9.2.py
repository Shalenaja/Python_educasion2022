"""Тестирование функции из доп.задачи №3 Урока №3"""

# с использованием assert:

a = [1, 2, 6, 9, 5, 3]


def diff_max_min(arr):
    """ функция находит разницу между максимальным и минимальным значениями
    элементов

    :param arr: список, в котором нужно произвести операцию
    :return: значение разницы
    """
    a = arr[0]
    b = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > a:
            a = arr[i]
        if arr[i] < b:
            b = arr[i]
        i += 1
    return a - b


def test_diff_max_min():
    assert diff_max_min(a) == 8, 'неверно'


if __name__ == "__main__":
    test_diff_max_min()
