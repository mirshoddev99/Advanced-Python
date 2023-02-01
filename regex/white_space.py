import re

# \s means that white space characters
# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r'\s')
# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match.span())

print()

# \S means that without white space characters
test_string = 'a,b,c,d,e,f,g,h,i,j'
pattern = re.compile(r'\s')
matches = pattern.finditer(test_string)
# for match in matches:
#     print(match.group())

if re.search(r"\s", test_string):
    print("True")
else: 
    print("False")