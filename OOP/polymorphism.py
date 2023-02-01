from inheritence import MyInheritance


# Polymorphism
class MyPolymorphism(MyInheritance):
    def __init__(self, first_name, last_name, birth_date, university, gpa, major):
        super().__init__(first_name, last_name, birth_date, university, gpa)
        self.major = major

    def full_info(self):
        return \
            f""" 
        The Full name of student {self.first_name} {self.last_name}. 
        (He/She)'s birthday is {self.birth_date}. 
        (He/She)'s ID number is {str(self.id)}.
        (He/She)'s a student at a {self.university} University.
        (He/She)'s major is {self.major}.
        (He/She)'s gpa is {str(self.gpa)}.
            """


new_poly_student = MyPolymorphism("Anvar", "Narzullayev", "1979-09-30", "Islam", 4.4, "Computer science and AI")
# print(new_poly_student.full_info())
# print(new_poly_student.add_info())
# print(MyPolymorphism.my_class_attribute)