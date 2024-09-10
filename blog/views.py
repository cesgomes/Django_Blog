from django.shortcuts import render
from django.http import HttpResponse

#Primeiro: Criar a função que irá ter a página home
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<H2>About Page</h2')