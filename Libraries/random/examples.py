import random

# float
# a = random.uniform(1, 10)
# print(a)


# int
# b = random.randint(1, 10)
# print(b)


# randrange: do not include upper bound (10) in this case
# c = random.randint(1, 10)
# print(c)


# choice
my_list = list("ABCDEFG")
d = random.choice(my_list)
print(d)

# multiple time not unique
my_list = list("ABCDEFG")
d = random.choices(my_list, k=3)
print(d)

# multiple time unique
my_list = list("ABCDEFG")
d = random.sample(my_list, 3)
print(d)