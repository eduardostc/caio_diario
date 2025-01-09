from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return render(request, 'home.html')


def escrever(request):
  if request.method == 'GET':
    return render(request, 'escrever.html')
  elif request.method == 'POST':
    titulo = request.POST.get('titulo')
    tags = request.POST.get('tags')
    pessoas = request.POST.get('pessoas')
    texto = request.POST.get('texto')
    return HttpResponse(f'{titulo}')