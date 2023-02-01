"""
Note: Original object is not changed When you use sorted function. that returns a new sorted list etc.
"""
import random

lst = list(range(1, 11))
random.shuffle(lst)
lst_sorted = sorted(lst)
print(lst_sorted)


string = "Hello World"
string_sorted = sorted(string)
print(string_sorted)


lst = list(range(1, 11))
random.shuffle(lst)
lst_sorted = sorted(lst, reverse=True)  # Descending order
print(lst_sorted)


pairs = [[1, 2, 3], [4, 5, -6, 7], [8, 9, -10, 11, -12]]
sorted_pairs = sorted(pairs, key=sum)
print(sorted_pairs)
