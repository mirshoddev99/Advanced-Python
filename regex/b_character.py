import re



# (\b example) is found when string has any white space before (example)
test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\bhey')
matches = pattern.finditer('heyho hohey')
for match in matches:
    print(match)


print()



# (\B example) is opposite of above example
test_string = 'hello 123_ heyho hohey'
pattern = re.compile(r'\Bhey')
matches = pattern.finditer('heyho hohey')
for match in matches:
    print(match)