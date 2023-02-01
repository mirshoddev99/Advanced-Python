class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary = None

    # setter
    def set_salary(self, value):
        if value < 1000:
            self.__salary = 1000
        if value > 2000:
            self.__salary = value

    # getter
    def get_salary(self):
        return self.__salary



doe = Student("Doe", 22)
print(doe.name, doe.age)

doe.set_salary(500)
print(doe.get_salary())


# _x is called a "protected" attribute (one underscore)
# __x is called a "private" attribute (double underscore)