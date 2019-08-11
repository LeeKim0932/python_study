import re

source = ''' I wish I may, I wish I might... Have a dish of fish tonight.'''

save = re.findall('wish', source)
print(save)

save = re.findall('wish|fish',source)
print(save)

save = re.findall('^wish',source)
print(save)

save = re.findall('^I wish', source)
print(save)

save = re.findall('fish$',source)
print(save)

save= re.findall('[fw]ish',source)
print(save)

save = re.findall('a',source)
print(save)
