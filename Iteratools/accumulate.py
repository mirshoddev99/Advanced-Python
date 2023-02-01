from itertools import accumulate
import operator
"""
Module operator
Operator Interface
This module exports a set of functions corresponding to the intrinsic operators of Python. 
For example, operator.add(x, y) is equivalent to the expression x+y. 
The function names are those used for special methods; variants without leading and trailing '__' are also provided for convenience.
This is the pure Python implementation of the module.
"""

"""
Accumulate - Jamlash/To'plash/Yig'ish

"""


# a = [1, 2, 3, 4]
# my_acc = accumulate(a)
# print(a)
# print(list(my_acc))


# print(f"\n............Multiply................\n")
# # Multiply
# b = [1, 2, 3, 4]
# my_acc2 = accumulate(a, func=operator.mul)
# print(b)
# print(list(my_acc2))

factor = [11, 2, 2]
result = list(accumulate(factor, func=operator.mul))
print(result[-1])