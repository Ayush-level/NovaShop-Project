from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Store page</h1>')

def about(request):
    return HttpResponse('<h1>About store<h1>')
