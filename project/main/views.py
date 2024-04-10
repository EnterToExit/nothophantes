from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'main/login.html')

def signup(request):
    return render(request, 'main/signup.html')

def product(request):
    return render(request, 'main/product.html')