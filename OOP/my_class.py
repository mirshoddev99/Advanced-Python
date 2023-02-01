from uuid import uuid4


class Student:
    # This is a class attribute that only belongs to the Student class not objects of the Student class
    my_class_attribute = "Student class attribute"

    # These are instance attributes that only belong to every object of the Student class
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.id = uuid4()

    # this is called instance method
    def full_info(self):
        return \
            f""" 
        The Full name of student {self.first_name} {self.last_name}. 
        (He/She)'s birthday is {self.birth_date}. 
        (He/She)'s ID number is {str(self.id)}.
            """


doe = Student("Doe", "John", "1992-11-22")
# print(doe.full_info())

mirshod = Student("Mirshod", "Oripov", "1999-12-28")
# print(mirshod.full_info())
