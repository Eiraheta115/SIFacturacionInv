from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientesForm
from .forms import ProveedoresForm
from .models import Clientes
from django.forms import ModelForm
from django.views.generic import ListView

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


    return render(request, "../templates/products.html")

def clientes_list(request, template_name='../templates/clientes_list.html'):
    clientes = Clientes.objects.all()
    data = {}
    data['object_list'] = clientes
    return render(request, template_name, data)

def clientes_create(request, template_name='../templates/clientes_form.html'):
    form = ClientesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('templates:clientes_list')
    return render(request, template_name, {'form': form})

def clientes_update(request, pk, template_name='../templates/clientes_form.html'):
    clientes = get_object_or_404(Clientes, pk=pk)
    form = ClientesForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('templates:clientes_list')
    return render(request, template_name, {'form': form})

def clientes_delete(request, pk, template_name='../templates/clientes_delete.html'):
    clientes = get_object_or_404(Clientes, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('templates:clientes_list')
    return render(request, template_name, {'object': post})

def proveedores_list(request, template_name='../templates/proveedores_list.html'):
    proveedores = Proveedores.objects.all()
    data = {}
    data['object_list'] = proveedores
    return render(request, template_name, data)

def proveedores_create(request, template_name='../templates/proveedores_form.html'):
    form = ProveedoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('templates:proveedores_list')
    return render(request, template_name, {'form': form})

def proveedores_update(request, pk, template_name='../templates/proveedores_form.html'):
    proveedores = get_object_or_404(Proveedores, pk=pk)
    form = ProveedoresForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('templates:proveedores_list')
    return render(request, template_name, {'form': form})

def proveedores_delete(request, pk, template_name='../templates/proveedores_delete.html'):
    proveedores = get_object_or_404(Proveedores, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('templates:proveedores_list')
    return render(request, template_name, {'object': post})

class BodegasList(ListView):
    model = Bodegas
    template_name = "../templates/bodegaslist.html"

class CategoriasList(ListView):
    model = Categorias
    template_name = "../templates/categorialist.html"

class ProductosList(ListView):
    model = Productos
    template_name = "../templates/productlist.html"