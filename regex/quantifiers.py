import re

# my_string = 'hello_123_456'
# pattern = re.compile(r'\d*')
# matches = pattern.finditer(my_string)
# for match in matches:
#     print(match)

print()

# pattern2 = re.compile(r'\d+')
# matches2 = pattern2.finditer(my_string)
# for match in matches2:
#     print(match)
#

print()

# my_string = 'hello_1_2-3'
# pattern = re.compile(r'_?\d')
# matches = pattern.finditer(my_string)
# for match in matches:
#     print(match)


print()

# my_string2 = 'hello_123'
# pattern2 = re.compile(r'\d{3}')
# matches2 = pattern2.finditer(my_string2)
# for match in matches2:
#     print(match)


# practice with dates
dates = '''
2020.04.01
01.04.2020

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_08_09
1999/12/28
'''

# find year0000.month00.day00
pattern_date = re.compile(r"\d{4}.\d{2}.\d{2}")
match_dates = pattern_date.finditer(dates)
for d in match_dates:
    print(d)

print()

# find between 5 and 8 months only
patten_months = re.compile(r"\d{4}.0[5-8].\d{2}")
match_mon = patten_months.finditer(dates)
for m in match_mon:
    print(m)

# find my birthday
patten_months = re.compile(r"\d{4}.12.\d{2}")
match_mon = patten_months.finditer(dates)
for m in match_mon:
    print(f"\n{m}")

print()

# find day00.month00.year0000
pattern_date = re.compile(r"\d+.\d+.\d{4}")
match_dates = pattern_date.finditer(dates)
for d in match_dates:
    print(d)

print()

# find pattern like year_month_day
pattern_date = re.compile(r"\d{4}_\d{2}_\d{2}")
match_dates = pattern_date.finditer(dates)
for d in match_dates:
    print(d)
