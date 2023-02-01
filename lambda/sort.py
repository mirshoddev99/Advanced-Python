# lambda arguments: expression

nums2D = [(33, 2), (44, 4), (6, 3), (7, 9)]
sorted_nums2D = sorted(nums2D, key=lambda x: sum(x))

print("Original list", nums2D)
print("The sorted list according to sum of elements of each tuple", sorted_nums2D)
