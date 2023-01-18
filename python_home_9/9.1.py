"""Тестирование функции из задачи №6 Урока №3"""


# с использованием assert:

def capital_let(word):
    st = word
    return st.title()


def assert_equal(text_1, text_2):
    assert text_1 == text_2, f"{text_1} != {text_2}"


assert_equal(capital_let("test"), 'Test')
