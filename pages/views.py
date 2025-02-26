from django.shortcuts import render
from django.http import HttpResponse
from .models import Convocacao, postagem

def index (request):
	post = postagem.objects.all().order_by('-data_publicacao')
	return render(request, 'pages/index.html')

def convocacoes (request):
	convocacoes = Convocacao.objects.all().order_by('-data_publicacao')
	return render(request, 'pages/convocacoespage.html')

def denuncia (request):
	return render(request, 'pages/denunciapage.html')

def documentos(request):
	return render(request, 'pages/documentospage.html')

def faleconosco (request):
	return render(request, 'pages/faleconoscopage.html')

def filiese (request):
	return render (request, 'pages/filiesepage.html')

def sobrenos (request):
	return render(request, 'pages/sobrenospage.html')


