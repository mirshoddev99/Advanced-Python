from collections import namedtuple

"""
collections def namedtuple(typename: str,
               field_names: str | Iterable[str],
               *,
               verbose: bool = ...,
               rename: bool = ...,
               module: str | None = ...) -> Type[tuple]
Returns a new subclass of tuple with named fields.
>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point.__doc__                   # docstring for the new class
'Point(x, y)'
>>> p = Point(11, y=22)             # instantiate with positional args or keywords
>>> p[0] + p[1]                     # indexable like a plain tuple
33
>>> x, y = p                        # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y                       # fields also accessible by name
33
>>> d = p._asdict()                 # convert to a dictionary
>>> d['x']
11
>>> Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
>>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)
"""

# This is the same with (Struct) in C
Point = namedtuple('Point', 'x, y')
my_point = Point(22, 33)
print(my_point)
print("x = {} y = {}".format(my_point.x, my_point.y))
print("x + y = {}".format(my_point.x + my_point.y))