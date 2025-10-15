from django.shortcuts import render 
from django.http import HttpResponse 

# Create your views here. 
def index(request): 
    return render(request, 'core/index.html')

def identidad(request): 
    return render(request, 'core/identidad.html')
    
def contactanos(request): 
    return render(request, 'core/contactanos.html')

def noticia(request): 
    return render(request, 'core/noticia.html')
