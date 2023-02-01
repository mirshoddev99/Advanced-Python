# def square(x):
#     return x ** 2
#
#
# print(square(2))
# res = square
# print(res(2))
# print()
#
# print("name of res function object: ", res.__name__)
# print("name of square function object: ", square.__name__)
#
# print()
#
# print("Type of res function object", type(res))
# print("Type of square function object", type(square))
#
# print()
#
# print("the ID of res function object", id(res))
# print("the ID of square function object", id(square))
#


# Above the example of the function is the same as below the example of a class
class CustomClass:
    def __init__(self, age):
        self.age = age


a = CustomClass(22)
b = CustomClass
b = b(22)

print(a.age)
print(b.age)

print("a class->> ", a.__class__)
print("b class->> ", b.__class__)
