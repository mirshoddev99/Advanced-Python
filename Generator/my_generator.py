def mygenerator():
    yield 1
    yield 2
    yield 3


gen1 = mygenerator()
print("Sum of generator elements is", sum(gen1))

gen2 = mygenerator()
for i in gen2:
    print(i)
