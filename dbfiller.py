from django.core.management import setup_environ
from mcjailcensus import settings

setup_environ(settings)

from mcjailcensus.models import Inmate

f = open('docs/readable.csv')
first = True

for line in f:
	if not first and not line is '':
		line = line.split(',')
		a = Inmate(last=line[0], dob=line[1], sex=line[2], middle=line[3], race=line[4], mcid=line[5], first=line[6])
		a.save()
	else:
		first = False

f.close()