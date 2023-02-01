from itertools import combinations
from math import comb

a = [1, 2, 3, 4, 5]
MyComb = combinations(a, 3)
print(MyComb)
print(list(MyComb))

my_comb = comb(5, 2)
print(my_comb)

