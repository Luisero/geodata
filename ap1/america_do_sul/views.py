from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index_america(request):
    return render(request, 'america_do_sul/index.html')


def brasil(request):
    return HttpResponse('brasil')

def chile(request):
    return HttpResponse('chile')

def uruguai(request):
    return HttpResponse('uruguay')