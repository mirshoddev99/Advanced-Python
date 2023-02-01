import sys

my_generator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(my_generator))

my_list = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(my_list))
