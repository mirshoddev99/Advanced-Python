import re


# finditer method
test_string  = "33Thus far, In both cases, putting one in a regex will123sdad12"
pattern = re.compile(r"123")
matches = pattern.finditer(test_string)

for match in matches:
    print("finditer method-> ", match)


# findall method
pattern = re.compile(r"cases")
matches_all = pattern.findall(test_string)

for match in matches_all:
    print("\nFindall method-> ", match)



# search method
pattern = re.compile(r"33")
search = pattern.search(test_string)
print("\nsearch method-> ", search)



# span, start, end group methods
string_test = "123abc4567def89abc"
pattern = re.compile(r"abc")
matches = pattern.finditer(string_test)

for w in matches:
    print("\nspan, start, end methods-> ", w.span(), w.start(), w.end())
    print("\nGroup method-> ", w.group())
