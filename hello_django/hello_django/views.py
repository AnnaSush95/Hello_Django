from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a=5+6
    return render(request, 'about.html', {'gretting':a}) # На страницу выводится все, что написано в документе about.html

def home(request):
    return HttpResponse('This is my home')

def test(request):
    return HttpResponse('This is page for test')

