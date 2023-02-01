"""
Return the hash value for the given object.
Two objects that compare equal must also have the same hash value, but the reverse is not necessarily true.
"""

num_hash = hash((1, 2, 3, 4, 5))
num_hash2 = hash((1, 2, 3, 4, 5))
key = hash("mykeystring")

print(num_hash)
print(key)
print(num_hash == key)
print(num_hash == num_hash2)