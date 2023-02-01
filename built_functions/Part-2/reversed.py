"""
Return a reverse iterator over the values of the given sequence.
"""

lst = list(range(1, 11))
lst_reversed = reversed(lst)            # this method returns us a reversed object as map function
print(list(lst_reversed))

string = "Hello World"
string_reversed = reversed(string)
print(list(string_reversed))

