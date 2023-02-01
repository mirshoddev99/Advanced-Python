"""
Return True if bool(x) is True for all values x in the iterable.
If the iterable is empty, return True.
"""

nums = [1, 2, 3]
print(all(nums))

nums = [1, 2, False]
print(all(nums))

nums = [1, 2, 0]
print(all(nums))