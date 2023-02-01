"""
getattr(object, name[, default]) -> value
Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
When a default argument is given, it is returned when the attribute doesn't exist; without it, an exception is raised in that case.
"""


class MyDelAtt:
    def __init__(self, age):
        self.age = age


c = MyDelAtt(23)
print(getattr(c, "age"))
