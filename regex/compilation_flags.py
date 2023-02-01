import re

string = "Hello World"
pattern = re.compile(r"world", re.IGNORECASE)  # Also, you can write re.I
matches = pattern.finditer(string)
for match in matches:
    print(match)

print()

# ignore ASCII characters
string2 = "Python one of the best programming $language"
pattern2 = re.compile(r"language", re.ASCII)  # Also, you can write re.A
matches2 = pattern2.finditer(string2)
for match in matches2:
    print(match)
