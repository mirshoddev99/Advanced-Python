from collections import Counter

"""
Create a new, empty Counter object. And if given, count elements from an input iterable. 
Or, initialize the count from another mapping of elements to their counts.

>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
>>> c = Counter(a=4, b=2)                   # a new counter from keyword args
"""

a = "aaaaabbbcccdddiieeeeooowww"
my_counter = Counter(a)
# print(my_counter)
# print("These are all keys: ", my_counter.keys())
# print("These are all values: ", my_counter.values())
# print("These are most commot keys&values: ", my_counter.most_common())
# print("These are most commot 3 keys&values: ", my_counter.most_common(3))


strs = "one two three six six".split()
my_cnt = Counter(strs)
# print(my_cnt)
# print(my_cnt.values())
# print(my_cnt.keys())

my_list = [11, 11, 12, 3, 4, 5, 5, 9, 9]
MyCount = Counter(my_list)
print(MyCount)
for key, value in MyCount.items():
    print(f"{key} is occurred {value} times in the list")