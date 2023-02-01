import pickle
from modules.Pickle.pickle_01 import student_list


# working with pickle

std1 = {"name":"Mirshod", "age":22, "semester":2}
std2 = {"name":"John", "age":32, "semester":3}

# writing in binary
with open('info', 'wb') as file:
    pickle.dump(std1, file)
    pickle.dump(std2, file)
    pickle.dump(student_list, file)
    print("Students' information was successfully written in binary file")


# reading from binary
with open('info', 'rb') as file:
    t1 = pickle.load(file)
    t2 = pickle.load(file)
    students = pickle.load(file)

print(t1)
print(t2)
print(students)