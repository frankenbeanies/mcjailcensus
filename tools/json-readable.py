#Parse json to csv with format last,dob,sex,middle,race,mcid,first
import re

f = open('docs/census16.pdf.json')
w = open('docs/readable.csv', 'w')

prev = ''

for line in f:
	line = re.findall(r'\"(.*?)\"', line)

	i = 0

	for item in line:
		if 'last' in prev and item is not '':
			w.write(item + ',')
		if 'dob' in prev or 'sex' in prev or 'middle' in prev or 'race' in prev or 'mcid' in prev:
			w.write(item + ',')
		elif 'first' in prev:
			w.write(item + '\n')

		prev = item
		i += 1

f.close()
w.close()

f = open('docs/readable.csv')

lst = []

for line in f:
	if len(line.split(',')) is 7:
		lst.append(line)

f.close()

f = open('docs/readable.csv', 'w')

f.write('Last Name, Date of Birth, Sex, Middle Name, Race, MCID, First Name\n' )
for line in lst:
	f.write(line)

f.close()