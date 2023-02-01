"""
Return the identity of an object.
This is guaranteed to be unique among simultaneously existing objects. (CPython uses the object's memory address.)
"""

# this method almost the same pointer in C
a = list(range(1, 11))
b = a
print(id(a))
print(id(b))
