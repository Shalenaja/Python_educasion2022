from copy import deepcopy

from memory_profiler import profile


@profile
def function_1():
    x = list(range(100000))
    y = deepcopy(x)
    del x
    y = None

    return "fnfn"

function_1()


###############
from random import randint
from pympler import asizeof
from numpy import array

lst_obj = [randint(-100, 100) for _ in range(50000)]
print(type(lst_obj))
print(asizeof.asizeof(lst_obj))

lst_obj = array([randint(-100, 100) for _ in range(50000)])
print(type(lst_obj))
print(asizeof.asizeof(lst_obj))