import re

urls = """
http://python-engineer.com
http://www.pyeng.net
http://english.com
https://www.python-engineer.org
https://www.mirshod-dev.com
"""

pattern = re.compile(r'https?://(www\.)?(\w|-)+\.\w+')
pattern2 = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)

subbed_urls = pattern2.sub(r"\2\3", urls)
print(subbed_urls)

print()


# print only http urls
http_pattern = re.compile(r"http://(www\.)?([a-zA-Z-]+)(\.\w+)")
matches2 = http_pattern.finditer(urls)
for h in matches2:
    print(h)
    print(f"middle group in the http_pattern -> {h.group(2)}")
    print(f"last group in the http_pattern -> {h.group(3)}")
print()




my_string = 'abc123ABCDEF123abc'
pattern3 = re.compile(r'123') #  no escape for the . here in the set
matches3 = pattern3.split(my_string)
print(matches3)

print()

# replace mirshod to world with sub method
my_string2 = "hello mirshod, you are the best mirshod"
pattern4 = re.compile(r"mirshod")
subbed_string = pattern4.sub(r"world", my_string2)
print(subbed_string)



print()

# replace Java to Python with sub method
my_string3 = "hi, I am a Java developer"
pattern5 = re.compile(r"Java")
subbed_string2 = pattern5.sub(r"Python", my_string3)
print(subbed_string2)