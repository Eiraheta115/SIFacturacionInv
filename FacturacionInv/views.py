from django.shortcuts import render
from .forms import *

# Create your views here.

def inicio(request):
    return render(request, "../templates/index.html")

def new_product(request):
    template = "../templates/Cproducts.html"

    categorias = list()
    cates = Categorias.objects.all()
    for c in cates:
        categorias.append(c)

    bodegas = list()
    cellars = Bodegas.objects.all()
    for b in cellars:
        bodegas.append(b)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        bodega = Bodegas.objects.get(idbodega=request.POST.get('bodega'))
        categoria = Categorias.objects.get(idcategoria=request.POST.get('categoria'))
        maxima = request.POST.get('maxima')
        minima = request.POST.get('minima')
        actual = request.POST.get('actual')
        product = Productos(codigoprod=codigo, nombre=nombre, descripcion=descripcion, marca=marca,
                            existenciamax=maxima, existenciamin=minima, existenciaactual=actual,
                            idcategoria=categoria, idbodega=bodega)
        product.save()

    context = {
        'categorias': categorias,
        'bodegas': bodegas,
    }
    return render(request, template, context)

def new_categoria(request):
    template = "../templates/Ccategoria.html"

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        descripcion = request.POST.get('descripcion')
        categoria = Categorias(nombre=nombre, codigo=codigo, descripcion=descripcion)
        categoria.save()

    context = {}
    return render(request, template, context)

def new_bodega(request):
    template = "../templates/CBodega.html"

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        bodega = Bodegas(nombre=nombre, descripcion=descripcion)
        bodega.save()

    context = {}
    return render(request, template, context)

