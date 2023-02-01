import re

test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\w')
matches = pattern.finditer(test_string)
for match in matches:
    print(match.group())

print()

test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\W')
matches = pattern.finditer(test_string)
for match in matches:
    print(match.group())

# practice check email which have only alpha numeric characters
patter3 = "\S([a-zA-Z0-9]+)@.\w+"
user = input("\nEnter your email address: ")

if re.search(patter3, user):
    print("True")
else:
    print("False")
