import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

person_json = json.dumps(person, indent=4)

# Convert back to Python Dict
my_py_dict = json.loads(person_json)
print(my_py_dict)

# Convert person.json file to Python Dict
# with open("person.json", "r") as f:
#     my_file_dict = json.load(f)
#     print(my_file_dict)