from django.shortcuts import render
from django.http import HttpRequest

def index (request):
   # return (request, 'index.html')
   return render (request, 'index.html')