import re

'''
match --> check if pattern matches at the beginning of a string
search--. searches the entire string for a match
finall --> returns list of all matches
sub -->  substitute/ replaces pattern with something else

'''

text = "Hello, Santhosh . my mobile number is 9874561236"

match = re.search(r"\d{10}", text)
if match:
    print(match.group())


# """
# \d --> any digit 0-9
# \D --> any non digit
# \w --> any word character --. a-z A-Z 0-9,_
# \W --> Non word character
# \s --> any whitespace
# . --> any character except new line
# * --> 0 or more repetitions
# ? --> 0 or 1 repetition
#
# """

sen = "Hello, Santhosh . my mobile number is 9874561236 sivanesh8392@gmail.com"

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

mat = re.search(pattern, sen)
if mat:
    print(mat.group())