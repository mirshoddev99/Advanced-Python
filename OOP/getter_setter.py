class Student:

    class_variable = "This is class variable for understanding @classmethod decorator"

    # Bu method Student class dan instance yaratmasdan turib class o'zi bilan interact qilish imkonini beradi.
    @classmethod
    def print_it(cls):
        return f"{cls.class_variable}"

    def __init__(self, name):
        self.name = name
        self._age = None

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def get_age(self, age):
        self._age = age

    def __repr__(self):
        return f"Your name is {self.name}, age is {self._age} years old."


print(Student.print_it())
print("")
s = Student("John")
s.get_age = 23
print(s.get_age)
print(s)

"""
@property --> Bu decorator ishlatilinishi __init__ method ichida objectning propertylarini yozib keyin ularga tashqarida () ishlatmasdan murojaat qila olish bilan bir xil.
@get_age.setter --> Bu decorator ishlatayotganimizda __init__ ichidagi propertyga qiymat uzatgandek bu decorator tashqarida s.get_age = 23 bo'ladi. 
Keyin object ichidagi @property ishlab undan qaytgan ya'ni 23 qiymatni olib (age)ga set(o'rnatish) qiladi.

Yuqoridagilar <s.name = "Mirshod"> misoliga equivalient.

"""
