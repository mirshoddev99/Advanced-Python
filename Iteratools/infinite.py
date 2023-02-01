from itertools import cycle, repeat, count

# Count
# my_nums = list(range(1, 11))
# for i in count(1):
#     print(i)
#     if i == len(my_nums):
#         break
#


# Cycle
# b = [22, 33, 44]
# for k in cycle(b):
#     print(k)


# Repeat
b = [22, 33, 44]
for k in repeat(b, 4):
    print(k)
