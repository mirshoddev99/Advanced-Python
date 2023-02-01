# lambda arguments: expression

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_nums = map(lambda x: x ** 2, nums)
print(list(square_nums))