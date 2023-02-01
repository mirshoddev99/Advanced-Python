from uuid import uuid4


class Student:

    def __init__(self, age):
        self.age = age

    # (x < y) comparison operator between instances of class
    def __lt__(self, other):
        if self.age < other.age:
            return f"Other's age is greater than you"
        return f"False"

    # (x <= y) comparison operator between instances of class
    def __le__(self, other):
        if self.age <= other.age:
            return f"Other's age is greater or equal"
        else:
            return f"False"

    # (x > y) comparison operator between instances of class
    def __gt__(self, other):
        if self.age > other.age:
            return f"your age is greater than other"
        else:
            return f"False"

    # (x >= y) comparison operator between instances of class
    def __ge__(self, other):
        if self.age >= other.age:
            return f"your age is greater or equal"
        else:
            return f"False"

    # (x == y) comparison operator between instances of class
    def __eq__(self, other):
        if self.age == other.age:
            return f"Both ages are equal"
        else:
            return f"False"

    # (x != y) comparison operator between instances of class
    def __ne__(self, other):
        if self.age != other.age:
            return f"Both ages are not equal"
        else:
            return f"False"


# s1 = Student(22)
# s2 = Student(40)
# print(s1 < s2)
# s1 = Student(60)
# s2 = Student(40)
# print(s1 <= s2)


# s1 = Student(60)
# s2 = Student(40)
# print(s1 > s2)
# s1 = Student(60)
# s2 = Student(60)
# print(s1 >= s2)

# s1 = Student(60)
# s2 = Student(60)
# print(s1 == s2)
#
# s1 = Student(80)
# s2 = Student(60)
# print(s1 != s2)


class Avto:
    def __init__(self, make, model, rang, yil, price, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.price = price
        self.__km = km
        self.__id = uuid4()

    def info_of_car(self):
        cars = f"Make: {self.make}, Model: {self.model}, rang: {self.rang}, yil: {self.yil}, price: {self.price}"
        return cars

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def __repr__(self):
        return f"{self.make} {self.model} {self.rang}"


class AvtoSalon:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def __repr__(self):
        return f"{self.name} {self.cars}"

    # __call__ method allows you to call your object in outside like obj_name()
    # as print or another built function(object) in Python.
    def __call__(self, *value):
        if value:
            for car in value:
                self.add_car(car)
        else:
            return self.cars[:]

    # __add__ method allows us to add attributes of two objects
    def __add__(self, other):
        if isinstance(other, AvtoSalon):
            new_salon = AvtoSalon(f"{self.name} {other.name}")
            new_salon.cars = self.cars + other.cars
            return new_salon

        elif isinstance(other, Avto):
            self.add_car(other)

    # __len__ method returns us length of (list/dict/set/tuple) from an object.
    def __len__(self):
        return len(self.cars)

    # __getitem__ method allows us to get item from a list
    def __getitem__(self, index):
        return self.cars[index]

    # __setitem__ method allows us to set item to a list
    def __setitem__(self, index, qiymat):
        self.cars[index] = qiymat

    # adding a car into the list
    def add_car(self, *values):
        for car in values:
            if isinstance(car, Avto):
                self.cars.append(car)


salon1 = AvtoSalon("MaxAuto")
avto_1 = Avto("GM", 'MALIBU', 'BLACK', 2022, '50.000$')
avto_2 = Avto("GM", 'TESLA', 'RED', 2000, '30.000$')

salon1.add_car(avto_1, avto_2)
print(salon1)

# get a particular item from the list using __getitem__ method
print(salon1[0])

# change values of an item using __setitem__ method
salon1[0] = Avto("BMW", "X7", "GREEN", 2012, '100.000$')
print(salon1[0])

# using __call__ method
avto_3 = Avto("VOLKSWAGEN", 'GEP', 'YELLOW', 1000, '300.000$')
salon1(avto_3)
print(salon1)

# get the length of the list in the object
print(f"The length of the list {salon1.__len__()}")

salon2 = AvtoSalon(" Lider")
avto_4 = Avto("MERS", 'BENZ', 'YELLOW', 7000, '140.000$')
avto_5 = Avto("GM", 'MAZDA', 'WHITE', 9000, '141.000$')
salon2(avto_4, avto_5)

# adding salon1 and salon2 together
salon3 = salon1 + salon2
print("\n-----Result is after adding two objects_____\n")
print(salon3)
