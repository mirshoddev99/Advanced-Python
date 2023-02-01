
student_list = []
filename = "talabalar.txt"

with open(filename, "r") as file:
    for line in file.readlines():
        student_list.append(line)

# print(student_list)

# removing whitespaces with (rstrip) method
# student_list = [student.rstrip() for student in student_list]
# print(student_list)


# removing whitespaces with (join & split) methods
student_list = "".join(student_list).split("\n")
# print(student_list)



