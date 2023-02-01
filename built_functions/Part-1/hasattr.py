"""
Return whether the object has an attribute with the given name.
This is done by calling getattr(obj, name) and catching AttributeError.

"""


class MyDelAtt:
    def __init__(self, age):
        self.age = age


c = MyDelAtt(23)
print(hasattr(c, "age"))
print(hasattr(c, "name"))
