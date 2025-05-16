from django.shortcuts import render

def index(request):
    data = {
        'caption': "CatDjango"
    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')