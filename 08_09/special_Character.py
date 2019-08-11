
import string
import re

printable = string.printable
len(printable)
print(printable[0:50])
print(printable[50:])
print(re.findall('\d', printable))
