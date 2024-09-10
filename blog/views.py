from django.shortcuts import render
from django.http import HttpResponse

#Primeiro: Criar a função que irá ter a página home
def home(request):
    return render (request, 'blog/home.html')

def about(request):
    return HttpResponse('<H2>About Page</h2')