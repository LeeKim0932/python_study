
poem = '''There was a young lady named Bright,
	Whose speed was far faster than light,
	She started ond day,
	In a relative way,
	And returned on the previous night.'''
len(poem)

fout = open('relativity','wt')
fout.write(poem) #write()는 파일에 쓴 바이트수를 반환
fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
	if offset > size:
		break
	fout.write(poem[offset:offset+chunk])
	offset += chunk

fout.close()

# mode x 
fout = open('relativity', 'xt') # error

try:
	fout = open('relativity', 'xt')
	fout.write('stomp stomp stomp')
except FileExistsError:
	print('relativity already exists!. That was a close one.')
