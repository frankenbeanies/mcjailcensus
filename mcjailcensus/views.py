from django.shortcuts import render_to_response
from django.template import RequestContext
from mcjailcensus.models import Inmate

def home_view(request):
	inmates = Inmate.objects.all()

	nm = 0
	nf = 0

	na = 0
	nb = 0
	ni = 0
	nu = 0
	nw = 0

	for inmate in inmates:
		if inmate.sex == 'M':
			nm += 1
		elif inmate.sex == 'F':
			nf += 1

		if inmate.race == 'A':
			na += 1
		elif inmate.race == 'B':
			nb += 1
		elif inmate.race == 'I':
			ni += 1
		elif inmate.race == 'U':
			nu += 1
		elif inmate.race == 'W':
			nw += 1

	return render_to_response('index.html', {'title': 'Home', 'inmates': inmates, \
		'nm': nm, 'nf': nf, 'mavg': 100*float(nm)/(nm+nf), 'favg': 100*float(nf)/(nm+nf), \
		'na': na, 'nb': nb, 'ni': ni, 'nu': nu, 'nw': nw, \
		'naavg': 100*float(na)/(na+nb+ni+nu+nw), \
		'nbavg': 100*float(nb)/(na+nb+ni+nu+nw), \
		'niavg': 100*float(ni)/(na+nb+ni+nu+nw), \
		'nuavg': 100*float(nu)/(na+nb+ni+nu+nw), \
		'nwavg': 100*float(nw)/(na+nb+ni+nu+nw)}, context_instance=RequestContext(request))