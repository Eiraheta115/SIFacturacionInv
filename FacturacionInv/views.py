from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "../templates/index.html")

def new_product(request):
    return render(request, "../templates/products.html")