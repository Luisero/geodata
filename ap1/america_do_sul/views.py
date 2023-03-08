from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index_america(request):
    return render(request, 'america_do_sul/index.html')


def brasil(request):
    return render(request, 'america_do_sul/paises/brasil.html')

def chile(request):
    return render(request, 'america_do_sul/paises/chile.html')

def uruguai(request):
     return render(request, 'america_do_sul/paises/uruguai.html')