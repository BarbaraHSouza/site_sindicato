from django.shortcuts import render
from django.http import HttpResponse

def agentedesaude (request):
	return render(request, 'acseace/agentedesaude.html')

def conquistas (request):
	return render(request, 'acseace/conquistasacseace.html')

def faq (request):
	return render(request, 'acseace/faqacseace.html')

def juntese (request):
	return render(request, 'acseace/junteseanosacseace.html')

def pccv (request):
	return render(request, 'acseace/pccvacseace.html')

def ifa (request):
	return render(request, 'acseace/ifaacseace.html')

def quemsomos (request):
	return render(request, 'acseace/quemsomosacseace.html')

def proximoseventos(request):
	return render (request, 'acseace/proximoseventos.html')

