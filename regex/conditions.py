import re

my_string = """
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
Mirshod
Sitora
"""

# find only name that has a .
pattern = re.compile(r'Mr\.\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

print()

# find both names which have . or not
pattern2 = re.compile(r"Mr\.?\s\w+")
matches2 = pattern2.finditer(my_string)
for w in matches2:
    print(w)

print()

# apply | condition statement which means or in Python
pattern3 = re.compile(r"(Mr|Ms|Mrs)\.?\s\w+")
matches3 = pattern3.finditer(my_string)
for s in matches3:
    print(s)

print()

# find my name
pattern4 = re.compile(r"(Mirs|Sit)\w+")
matches4 = pattern4.finditer(my_string)
for m in matches4:
    print(m, m.group())
