from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, Django!</h1>")

def data(request):
    return HttpResponse("<h2>Содержимое страницы data</h2>")

def test(request):
    return HttpResponse("<h2>Содержимое страницы test</h2>")
