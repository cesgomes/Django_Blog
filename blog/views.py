from django.shortcuts import render

#Primeiro: Criar a função que irá ter a página home
def home(request):
    return render (request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')
