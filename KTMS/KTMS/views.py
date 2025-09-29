from django.shortcuts import render

def pos_dashboard(request):
    return render(request, 'pos_app/dashboard.html')

def products(request):
    return render(request, 'pos_app/products.html')