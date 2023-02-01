# zeros = [0] * 5
# print(zeros)
#
# zeros = [0, 2] * 5
# print(zeros)
#
# tuples = [()] * 3
# print(tuples)
#
#
# def foo(a, b, *args, **kwargs):
#     print(a, b)
#     for arg in args:
#         print(arg)
#
#     for key in kwargs:
#         print(key, kwargs[key])
#
#
# foo(1, 2, 3, 4, 5, six=6, seven=7)
#
# print()
#
# my_list = [1, 2, 3, 4]
# print(*my_list)
#
# print()


# Separating
my_nums = [1, 2, 3, 4, 5, 6]
*beginning, last = my_nums
print(beginning)
print(last)

my_nums = [1, 2, 3, 4, 5, 6]
beginning, *middle, last = my_nums
print(beginning)
print(middle)
print(last)


print()


# Merging
my_tuple = (1, 2, 3)
my_list = (4, 5, 6)
new_list = [*my_tuple, *my_list]
print(new_list)
print()

dict_a = {"a": 1, "b":2}
dict_b = {"c": 3, "d":4}
new_dict = {**dict_a, **dict_b}
print(new_dict)









