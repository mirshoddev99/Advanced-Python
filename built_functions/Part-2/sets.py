# Sets: unordered, mutable, no duplicates

# odds = {1, 3, 5, 7, 9}
# evens = {2, 4, 6, 8}
# primes = {1, 2, 3, 5, 7}
#
# u = odds.union(evens)
# print(u)
#
# intersection = odds.intersection(evens)                 # intersection = (odds/evens) kesishgan elemenlarnigina oladi.
# print(intersection)
#
# intersection2 = odds.intersection(primes)                 # intersection2 = (odds/primes)
# print(intersection2)

"""
Difference and Intersection methods are antonym
difference - Kesishmagan (tekshirilayotgan setda o'zining elementlari bo'lamagan elementlardan tashkil topgan yangi to'plam.)
Intersection - Kesishgan (tekshirilayotgan setda o'zining elementlari bo'lganlardan tashkil topgan yangi to'plam.)
"""

# Difference method
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}
#
# diff = setB.difference(setA)
# print(diff)



"""
Symmetric - 2-ta setda ham bo'lgan elementlardan tashqari elementlar. 
Ya'ni birida bor element ikkinchisida bo'lmasligi kerak.
"""
# symmetric_difference method
# setC = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setD = {1, 2, 3, 10, 11, 12}
#
# diff2 = setC.symmetric_difference(setD)
# print(diff2)
#


# Update method
# setE = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# setG = {1, 2, 3, 10, 11, 12}
# setE.update(setG)
# print(setE)


# intersection_update method
# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set2 = {1, 2, 3, 10, 11, 12}
# set1.intersection_update(set2)
# print(set1)


# difference_update method
# set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set4 = {1, 2, 3, 10, 11, 12}
# set3.difference_update(set4)
# print(set3)


# symmetric_difference_update method
# set5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set6 = {1, 2, 3, 10, 11, 12}
# set5.symmetric_difference_update(set6)
# print(set5)
#

# copy method
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_b = set_a.copy()
set_b.add(11)
print(set_a)
print(set_b)
set_b.remove(11)
print(set_b)