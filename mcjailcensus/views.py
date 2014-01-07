from django.shortcuts import render_to_response
from django.template import RequestContext
from mcjailcensus.models import Inmate

def home_view(request):
	inmates = Inmate.objects.all()

	nm = 0
	nf = 0

	for inmate in inmates:
		if inmate.sex == 'M':
			nm += 1
		elif inmate.sex == 'F':
			nf += 1


	return render_to_response('index.html', {'title': 'Home', 'inmates': inmates, 'nm': nm, 'nf': nf, 'mavg': 100*float(nm)/(nm+nf), 'favg': 100*float(nf)/(nm+nf)}, context_instance=RequestContext(request))