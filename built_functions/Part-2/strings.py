# Strings: immutable, ordered, and text representation

from timeit import default_timer as timer

my_str_list = ["a"] * 500

my_strings = ""
# bad
start = timer()
for w in my_str_list:
    my_strings += w
stop = timer()
print(stop - start)

# good
start = timer()
my_strings = "".join(my_str_list)
stop = timer()
print(stop - start)