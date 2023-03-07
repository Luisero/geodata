from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_africa(request):
    return render(request, 'africa/index.html')

def quenia(request):
    return render(request,'africa/paises/quenia.html')

def angola(request):
    return  render(request, 'africa/paises/angola.html')