import re

# . operator
# test_string = 'python-engineer.com'
# pattern = re.compile(r'\.')
# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match)

# ^ and $ operators
test_string2 = 'mirshod oripov@gmail.com'
pattern2 = "^mirshod"
print(re.match(pattern2, test_string2))

if re.match(pattern2, test_string2):
    print("True")
else:
    print("False")

# test = "123abcABC"
# pattern3 = re.compile(r"ABC$")
# matches2 = pattern3.finditer(test)
# for w in matches2:
#     print(w)
