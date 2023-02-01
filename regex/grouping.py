import re

emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
mirshodpnu22@gmail.com
oripovmirshod9@gmail.com
"""


# printing results by group

pattern = re.compile('([a-zA-Z1-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')
matches = pattern.finditer(emails)
for match in matches:
    print(f"Match object: {match.group(0)}")
    print(f"First group: {match.group(1)}")
    print(f"second group: {match.group(2)}")
    print(f"last group: {match.group(3)}")
    print("\n")
