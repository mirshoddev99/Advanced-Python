class MyDelAtt:
    def __init__(self, age):
        self.age = age


c = MyDelAtt(23)
print(c.age)
delattr(c, "age")
print(c.age)

"""
Deletes the named attribute from the given object.
delattr(x, 'y') is equivalent to ``del x.y'
"""