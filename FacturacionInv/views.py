from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientesForm
from .forms import ProveedoresForm
from .models import Clientes
from django.forms import ModelForm

# Create your views here.

def inicio(request):
    return render(request, "../templates/index.html")

def new_product(request):
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
