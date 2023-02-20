class Parent:
    def say_hello(self) -> str:
        return "Hello, world!"


class Child(Parent):
    def greet(self) -> str:
        return super().say_hello()


child = Child()
print(child.greet())
