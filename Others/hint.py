def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows = meow(number)
print(meows, end="")