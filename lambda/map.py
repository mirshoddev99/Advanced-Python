# lambda arguments: expression
# filter(function, sequences)

a = [1, 2, 3, 4, 5, 6, 7]
b = filter(lambda x: x % 2 == 0, a)
filter_result = list(b)
print("Filter function", filter_result)

c = [i for i in a if i % 2 == 0]
print("List comprehension", c)

print()

# some more example with names
names = ["Jane", "Jenny", "Mike", "Jobs", "Julia", "Mister"]
name_res = filter(lambda w: w.startswith("J"), names)
res = list(name_res)
print("All names are started with (J)->> ", res)

name_res = filter(lambda w: w.__contains__("e"), names)
res = list(name_res)
print("Each name has (e)->> ", res)