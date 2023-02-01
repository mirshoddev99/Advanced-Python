"""
Return a dictionary containing the current scope's local variables.
NOTE: Whether updates to this dictionary will affect name lookups in the local scope.
Vice-versa is implementation dependent and not covered by any backwards compatibility guarantees.
"""

print(locals())
print(locals()["__file__"])
print(locals()["__loader__"])
