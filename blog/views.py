from django.shortcuts import render

posts = [
    {"author": "CESGomes",
     "Title": "Blog Post 1",
     "Content": "First Post Content",
     "DatePost": "09-Set-2024"},
    {"author": "John Doe",
     "Title": "Blog Post 2",
     "Content": "Second Post Content",
     "DatePost": "10-Set-2024"}
    ]

#Primeiro: Criar a função que irá ter a página home
def home(request):
    context = {
        'posts': posts
    }
    return render (request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
