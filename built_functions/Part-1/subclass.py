"""
Return whether 'cls' is derived from another class or is the same class.
A tuple, as in issubclass(x, (A, B, ...)), may be given as the target to check against.
This is equivalent to issubclass(x, A) or issubclass(x, B) or ....
"""


class A:
    pass

class B(A):
    pass


class C(B):
    pass


class D(C, A):
    pass


print(issubclass(B, A))
print(issubclass(C, B))
print(issubclass(D, A))
