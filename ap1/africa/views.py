from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_africa(request):
    return HttpResponse('index')

def kenya(request):
    return HttpResponse('kenya')

def angola(request):
    return  HttpResponse('angola')