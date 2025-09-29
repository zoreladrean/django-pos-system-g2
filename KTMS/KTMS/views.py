from django.http import HttpResponse
from django.shortcuts import render

def pos_dashboard(request):
    return render(request, 'pos_app/dashboard.html')

def products(request):
    return render(request, 'pos_app/products.html')

def index(request):
    return HttpResponse("Hello, world! This is my POS system.")