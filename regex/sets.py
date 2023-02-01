import re

test_string = 'hello 123_'
pattern = re.compile(r'[a-z]')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()

test_string2 = "hello 456_"
pattern2 = "[a-zA-Z_]"
matches2 = re.finditer(pattern2, test_string2)
for w in matches2:
    print(w)