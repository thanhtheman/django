from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Welcome to Django')

def project(request, pk):
    return HttpResponse('This is project' + str(pk))