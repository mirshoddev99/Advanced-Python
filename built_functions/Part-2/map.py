"""
map(func, *iterables) –> map object
Make an iterator that computes the function using arguments from each of the iterables.
Stops when the shortest iterable is exhausted.
"""

square_num = map(lambda x: x ** 2, list(range(1, 11)))
square_ls = list(square_num)
print(square_ls)

items = {"A": 1, "B": 2, "C": 3, "D": 5}
my_string = map(lambda key: items[key] * key, items)
print(tuple(my_string))
