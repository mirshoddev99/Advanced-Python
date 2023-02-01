import math
from timeit import default_timer as tm
import time


def my_fac_decorator(original_func):

    def wrapper(*args, **kwargs):
        t1 = tm()
        original_func(*args, **kwargs)
        t2 = tm()
        res = t2 - t1
        print("{} ran in {:.4f} seconds".format(original_func.__name__, res))
        return original_func

    return wrapper


@my_fac_decorator
def factorial(x):
    time.sleep(2)
    print(f"{x} factorial is equal to {math.factorial(x)}")


factorial(5)
