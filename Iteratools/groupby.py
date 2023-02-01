from itertools import groupby

a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x >= 3)

for k, v in group_obj:
    print(k, list(v))

print()
# GroupBy with dict
persons = [
    {"name": "John", "age": 22},
    {"name": "Jobs", "age": 22},
    {"name": "Gates", "age": 22},
    {"name": "Jenny", "age": 33},
    {"name": "Doe", "age": 55}
           ]
my_gr_obj = groupby(persons, key=lambda p: p["age"])
for key, values in my_gr_obj:
    print(key, list(values))