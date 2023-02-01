from my_class import Student


# Inheritance from Student class
class MyInheritance(Student):
    def __init__(self, first_name, last_name, birth_date, university, gpa):
        super().__init__(first_name, last_name, birth_date)
        self.university = university
        self.gpa = gpa

    def add_info(self):
        return \
            f""" 
        {self.first_name} is a student at {self.university} University. 
        (He/She)'s gpa is {str(self.gpa)}
            """


new_student = MyInheritance("Shoe", "Dog", "2003-08-08", "MIT", 4.5)
# print(new_student.full_info())
# print(new_student.add_info())


second_student = MyInheritance("Sitora", "Davlatovna", "1998-17-24", "Tashkent foreign language", 5.5)
# print(second_student.full_info())
# print(second_student.add_info())
