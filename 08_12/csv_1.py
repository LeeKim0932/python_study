
# number1 writer
import csv
villains = [
	['Doctor', 'No'],
	['Rosa', 'klebb'],
	['Mister', 'Big'],
	['Auric', 'Goldfinger']
with open('villains', 'wt') as fout:
	csvout = csv.writer(fout)
	csvout.writerows(villains)

#number2 reader
with open('villains', 'rt') as fin:
	cin = csv.reader(fin)
	villains = [row for row in cin] # list comprehension
print(villains)

#number3 DictReader
import csv
with open('villains', 'rt') as fin:
	cin = csv.DictReader(fin, fieldnames=['first', 'last']
	villains = [row for row in cin]

print(villains)

#number4 Dictreader_2
import csv
with open('villains', 'rt') as fin:
	cin = csv.DictReader(fin)
	villains = [row for row in cin]
print(villains)
