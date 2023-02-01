"""
Return the hexadecimal representation of an integer.

>>> hex(12648430)
'0xc0ffee
"""

class MyDelAtt:
    def __init__(self, age):
        self.age = age

    def __index__(self):
        return self.age


c = MyDelAtt(23)
print(hex(c))
print(hex(10))
print(hex(15))