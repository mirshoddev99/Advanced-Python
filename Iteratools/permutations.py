from itertools import permutations
from math import factorial

# a = [1, 2, 3, 4, 5, 6, 7]
# perm = permutations(a)
# print(perm)
# print(len(list(perm)))

# fac = factorial(7)
# print(fac)

"""
the length of a = 7
the permutations of (a) is equal to 7!

O'rin almashtirishlar soni 7! ga teng
"""


# prime_nums = [1, 2, 3]
# perm2 = list(permutations(prime_nums, 3))
# print(perm2)
# print(perm2[0][0])


def find_integer_triplets(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**(1/2))+1):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    triplets = []
    for i in range(2, n+1):
        for j in range(len(primes)):
            for k in range(j, len(primes)):
                for l in range(k, len(primes)):
                    if i == primes[j]*primes[k]*primes[l]:
                        triplets.append([primes[j], primes[k], primes[l]])
    return triplets

print(find_integer_triplets(50))


