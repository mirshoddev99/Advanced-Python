"""
Create and return a new object. See help(type) for accurate signature.
"""

widths = [4, 5, 6, 7, 2, 11]
heights = [3, 2, 4, 6, 4, 12]
zipped = zip(widths, heights)
print(zipped)
print(list(zipped))

keys = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
values = [11.2, 22.3, 15.3, -22, -1, -44, 5.1]
weather = dict(zip(keys, values))
print(weather)