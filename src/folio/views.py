from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("<h1>Manuel Cespedes</h1>")

def home(request):
  return render(request, 'home.html', {})