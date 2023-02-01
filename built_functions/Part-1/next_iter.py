"""
iter(iterable) -> iterator iter(callable, sentinel) -> iterator
Get an iterator from an object. In the first form, the argument must supply its own iterator, or be a sequence.
In the second form, the callable is called until it returns the sentinel
"""

words = ["hello", "world"]
l_iter = iter(words)
print(l_iter)

print(next(l_iter))
print(next(l_iter))


"""
next(iterator[, default])
Return the next item from the iterator. If default is given and the iterator is exhausted, 
it is returned instead of raising StopIteration.
"""
