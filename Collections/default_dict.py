from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d)
print(d['a'])
print(d['b'])
print(d['c'])  # it does not raise a key error
