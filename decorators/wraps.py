import math
from timeit import default_timer as tm
import time
from functools import wraps


def my_fac_decorator(original_func):

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = tm()
        result = original_func(*args, **kwargs)
        t2 = tm() - t1
        print("{} ran in {:.4f} seconds".format(original_func.__name__, t2))
        return result

    return wrapper


@my_fac_decorator
def factorial(x):
    time.sleep(2)
    print(f"{x} factorial is equal to {math.factorial(x)}")


factorial(15)
print(factorial.__name__)