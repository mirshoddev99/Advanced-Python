from uuid import uuid4


class Student:
    def __init__(self, first_name, last_name, birth_date, age):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.age = age
        self.id = uuid4()

    # 1. __str__ method returns us all attributes of an object only string format
    def __str__(self):
        return \
            f""" 
        The Full name of student {self.first_name} {self.last_name}. 
        (He/She)'s birthday is {self.birth_date}.
         (He/She)'s age is {self.age} years old.
        (He/She)'s ID number is {str(self.id)}.
            """

    # 2. __eq__ (equal) method compares attributes of two objects
    def __eq__(self, other):
        return self.age > other.age

    # 3. This method works only for the Student class because there is no (self) argument that passed check_age function.
    def check_age(age):
        if age < 25:
            return f"You are a Junior Engineer"
        return f"You are a Senior Engineer"


mirshod = Student("Mirshod", "Oripov", "1999-12-28", 23)
doe = Student("Doe", "John", "1992-11-22", 28)
print(doe.age > mirshod.age)


# print check_age function of Student class
print(Student.check_age(23))

"""  
    (self) ishlatilmagan har qanday attributga tashqaridan murojaat qilib bolmaydi. 
        Faqatgina Class nomi orqali murojaat qila olamiz. 
         Chunki self ishlatilmagan attributlar faqatgina 
         Classning instance hisoblanadi.
 """
