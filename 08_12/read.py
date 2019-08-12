
poem = '''There was a young lady named Bright,
	Whose speed was far faster than light;
	She started ond day
	In a relative way,
	And returned on the previous night.'''

fin open('relativity', 'rt')
poem = fin.read()
fin.close()
len(poem)

# read()
poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
	fragment = fin.read(chunk)
	if not fragment:
		break
	poem += fragment

fin.close()
len(poem)


# readline() 
poem = ''
fin = open('relativity', 'rt')
while True:
	line = fin.readline()
	if not line:
		break
	poem += line

fin.close()
len(poem)

# readlines()

fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
	print(line, end='')
