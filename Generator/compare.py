import sys


def my_list(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def my_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(my_list(1000)))
print(sys.getsizeof(my_generator(1000)))
