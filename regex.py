import re

'''
Identifiers:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any char
\W anything but a character
.  any character except for a new line
\b the whitespace around words
\. a period

Modifiers:
{1,3} we're expecting 1-3 
{x} expecting x amount
+ match 1 or more
? match 0 or 1
* match 0 or more
$ match the end of a string
^ matching the beginning of a string
| either or
[] range 

White Space Characters:
\n new lines 
\s space
\t tab
\e escape
\f form feed
\r return 

'''


example = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar is 102.
'''

ages = re.findall(r'\d{1,3}', example)
names = re.findall(r'[A-Z][a-z]+', example)

print(ages)
print(names)

d = {}
i = 0
for name in names:
    d[name] = ages[i]
    i += 1
print(d)

