"""
Return True if bool(x) is True for any x in the iterable.
If the iterable is empty, return False.
"""

nums = [1, 2, 3]
print(any(nums))

nums = []
print(any(nums))