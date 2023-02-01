"""
filter(function or None, iterable) –> filter object
Return an iterator yielding those items of iterable for which function(item) is true.
If function is None, return the items that are true
"""


# def filter_func(values):
#     return values % 2 == 0
#
#
# lst = list(range(1, 11))
# evens2 = filter(filter_func, lst)
# print(evens2)   # object
# print(list(evens2))
#
# evens = filter(lambda x: x % 2 == 0, lst)
# print(evens)     # object
# print(list(evens))


names = ["John", "Jenny", "Doe", "Jack", "Mir-shod", "Jonie", "Mike"]
name_filter = filter(lambda w: w.startswith("J"), names)
print(f"This is object {name_filter} in memory \n")
name_result = list(name_filter)
print(name_result)