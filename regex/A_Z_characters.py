import re

# \A example is found at the beginning of the string
test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\Ahello')
matches = pattern.finditer(test_string)
for match in matches:
    print(match, match.group())

print()



# \Z example is found at the end of the string
test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'hohey\Z')
matches = pattern.finditer(test_string)
for match in matches:
    print(match, match.group())


# practice
my_string = "Mirshod Oripov"
end = re.compile(r"Oripov\Z")
beginning = re.compile(r"\AMirshod")

if re.search(end, my_string) and re.search(beginning, my_string):
    print("True")
else:
    print("False")