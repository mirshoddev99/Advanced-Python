import re

# find only digits
test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\d')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()

# find only non-digits
test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\D')
matches = pattern.finditer(test_string)
for match in matches:
    print(match.group(), end=" ")


patter_age = re.compile(r"\d")
age = input("\nEnter your age: ")
if patter_age.search(age):
    print("True")
else:
    print("False")


patter_name = re.compile(r"\D")
name = input("\nEnter your name: ")

if patter_name.search(name):
    print("True")
else:
    print("False")
