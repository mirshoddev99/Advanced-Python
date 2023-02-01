

def countdown(n):
    yield "Starting.."
    while n > 0:
        yield n
        n -= 1


cd = countdown(4)


print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
