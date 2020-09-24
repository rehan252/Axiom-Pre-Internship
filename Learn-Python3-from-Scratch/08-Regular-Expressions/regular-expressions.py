"""
In this Doc we'll go through some basics regular expressions used in Python.
^ start with, ^a anything that starts with a
. match with any single character except /n new line
[] set of elements
- range of elements a-c means abc
$ ends with, a$ means must ends with a
* matches zero or more occurrences of the pattern left to it.
+ matches one or more occurrences of the pattern left to it.
? matches zero or one occurrence of the pattern left to it.
{}  {n,m}. This means at least n, and at most m repetitions of the pattern left to it.
| is used for alternation (or operator).
() is used to group sub-patterns. For example, (a|b|c)xz match any string that matches either a or b or c followed by xz
\ is used to escape various characters including all metacharacters. For example, \$a match if a
string contains $ followed by a

SPECIAL SEQUENCE:
\A - Matches if the specified characters are at the start of a string.
\b - Matches if the specified characters are at the beginning or end of a word.
\B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.
\d - Matches any decimal digit. Equivalent to [0-9]
\D - Matches any non-decimal digit. Equivalent to [^0-9]
\s - Matches where a string contains any whitespace character
\S - Matches where a string contains any non-whitespace character.
\w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]
"""

import re

txt = "Fire are in the house"
print(re.search("^Fire", txt))  # check if strings start with Fire
print(re.search("house$", txt))  # check if strings ends with house
print(re.search("^[a-z|A-Z]", txt))  # match with any upper and lower case char
print(re.search("^[0-9]", txt))  # check if there any number in string
print(re.findall("re", txt))  # return all match

# check if string is a valid email

email = input("Enter a valid email\n")
matching_string = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

if re.search(matching_string, email):
    print('{} is validated'.format(email))
else:
    print('Invalid Email...')


