"""
1. Shallow copy: one level deep, only reference of nested child objects
2. Deep copy: Full independent copy
"""

import copy


# org = [1, 2, 3, 4]
# cpy = copy.copy(org)
# cpy[0] = -10
# print(org)
# print(cpy)


# Shallow copy in nested list
# org = [[1, 2, 3, 4], [5, 6, 7, 8]]
# cpy = copy.copy(org)
# cpy[0][-1] = 40
# print(org)  # original list got effect too. Because (copy.copy) is only possible to copy one level depp.
# print(cpy)


# Deep copy in nested list
# org = [[1, 2, 3, 4], [5, 6, 7, 8]]
# cpy = copy.deepcopy(org)
# cpy[0][-1] = 40
# print(org)  # original list did not get effect.
# print(cpy)


# using deep copy among objects of a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Jack", 55)
p2 = copy.copy(p1)
p2.name = "Jobs"
p2.age = 22
print('p1.name: ', p1.name)
print('p2.name: ', p2.name)
print()


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


company = Company(p1, p2)
clone_company = copy.deepcopy(company)
clone_company.boss.age = 33
print("clone_company.boss.age: ", clone_company.boss.age)
print("company.boss.age: ", company.boss.age)
