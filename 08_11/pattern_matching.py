
#python3 pattern matching

import re

source = '''I wish I may, Iwish I might... Have a dish of fish tonight.'''
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
