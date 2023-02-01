# lambda arguments: expression
# reduce(function, sequences)
import operator
from functools import reduce

"""
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
This function is defined in “functools” module.

Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
"""

a = [1, 2, 3, 4]
product_nums = reduce(lambda x, y: x*y, a)
print(f"Product of nums is {product_nums}")

a = [1, 2, 3, 4]
product_nums = reduce(lambda x, y: operator.add(x, y), a)       # this is equal to (x + y)
print(f"Sum of nums is {product_nums}")