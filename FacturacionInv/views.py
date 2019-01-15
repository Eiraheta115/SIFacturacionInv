from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
    return render(request, "../templates/index.html")

def buscar(listClientes, busqueda):
	for c in listClientes:
		if busqueda in c[0].nombre.lower():
			c.idcliente
		else:
			print("No existe")
	return c.idcliente

def nueva_venta(request):
	template = "../templates/nueva_venta.html"

	clientes2 = list()
	cliente = Clientes.objects.all()

	for cl in cliente:
		clientes2.append(cl.nombre)


	if request.method == 'POST':
		fecha = request.POST.get("fecha")
		codigo = request.POST.get("codigo")
		concepto = request.POST.get("concepto")
		vencimiento = request.POST.get("vencimiento")
		total = request.POST.get("total")
		exenta = request.POST.get("exenta")
		descuento = request.POST.get("descuento")
		anulado = request.POST.get("anulado")
		impreso = request.POST.get("impreso")
		buscando = request.POST.get("cliente_info")
		search = buscando.lower()
		idcliente = buscar(clientes2, search)

		cf = True if request.POST.get("credito_fiscal") else False
		if cf:
			idfactncred = idfactura
			# idtdoc = 1
		else:
			idfactncred = null
			# idtdoc = 2
		fatura = Facturas(codigo=codigo, fecha=fecha, concepto=concepto, vencimiento=vencimiento, 
				total=total, exenta=exenta, descuento=descuento, anulado=anulado, impreso=impreso, 
				idtdoc=idtdoc, idcliente=idcliente, idfactncred=idfactncred)
		factura.save()



	'''

	movimiento = Movimientos(fecha=fecha, costomovimiento=costomovimiento, costopromedio=costopromedio,
		concepto=concepto, responsable=responsable, cantidad=cantidad, bodega1=bodega1, bodega2=bodega2, 
		codproducto=codproducto, tmov=tmov, idfactura=idfactura, idtdoctransferencia=idtdoctransferencia, 
		idlibcom=idlibcom)
	movimiento.save()

	producto = Prodcutos(codigoprod=codigoprod, nombre=nombre, descripcion=descripcionproducto, marca=marcaproducto, 
		existenciamax=existenciamax, existenciamin=existenciamin, idcategoria=idcategoria, idbodega=idbodega)
	producto.save()
	'''
	context = {
			# 'codigoprod':codigoprod, 'descripcionproducto':descripcion
	}

	return render(request, template, context)

def buscar_prod(listProductos, busqueda):
	for p in listProductos:
		if busqueda in p.codigoprod.lower():
			p.codigoprod
		else:
			p.codigoprod = 0
	return p.codigoprod

def listarproductos(listp, busqueda):
	seleccionados = list()
	for p in listp:
		if p.codigoprod == busqueda:
			seleccionados.append(p)
	return seleccionados

def prueba(request):
	template = "../templates/busqueda.html"

	products = list()
	productos = Productos.objects.all()
	for p in productos:
		products.append(p)
	if request.method == 'POST':
		cprod = request.POST.get("codprod")
		search = cprod.lower()
		cod = buscar_prod(products, search)
		print (cod)
		new = list()
		new = listarproductos(products, search)
	context = {'new':new}
	'''
	if request.method == 'POST':
		buscar = request.POST.get("codprod")
		prods = Productos.objects.filter(codigoprod=buscar)
		print (prods)
	
	prods = list()
	productos = Productos.objects.all()
	for pr in productos:
		prods.append(pr)
	if request.method == 'POST':
		nameprod = request.POST.get("codprod")
		search = nameprod.lower()
		idprodname = buscar_prod(prods, search)
		print(idprodname)
	'''

	return render(request, template, context)

def nueva_compra(request):
	return render(request, "../templates/nueva_compra.html")

def modificar_factura(request):
	return render(request, "../templates/nueva_venta.html")

def modificar_compra(request):
	return render(request, "../templates/nueva_compra.html")

def listar_facturas(request):
	return render(request, "../templates/listar_facturas.html")