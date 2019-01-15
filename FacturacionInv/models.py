# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bodegas(models.Model):
    idbodega = models.AutoField(primary_key=True)
    nombre = models.IntegerField()
    descripcion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bodegas'


class Categorias(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'categorias'


class Clientes(models.Model):
    idcliente = models.AutoField(primary_key=True)
    codigocli = models.CharField(max_length=50)
    registro = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    email = models.CharField(max_length=50)
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=50)
    dui = models.CharField(max_length=9)
    saldo = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'clientes'


class Correlativos(models.Model):
    idcorrelativo = models.AutoField(primary_key=True)
    resolucion = models.CharField(max_length=10)
    prefijo = models.CharField(max_length=10)
    minimo = models.IntegerField()
    maximo = models.IntegerField()
    fecha = models.DateField()
    activo = models.BooleanField()
    idtdoc = models.ForeignKey('Tipodocumentos', models.DO_NOTHING, db_column='idtdoc')

    class Meta:
        managed = False
        db_table = 'correlativos'


class Cxc(models.Model):
    idcxc = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=12, decimal_places=8)
    cargo = models.DecimalField(max_digits=12, decimal_places=8)
    abono = models.DecimalField(max_digits=12, decimal_places=8)
    saldo = models.DecimalField(max_digits=12, decimal_places=8)
    fecha = models.DateField()
    fechavencimiento = models.DateField()
    idfactura = models.ForeignKey('Facturas', models.DO_NOTHING, db_column='idfactura')

    class Meta:
        managed = False
        db_table = 'cxc'


class Cxcabonos(models.Model):
    idcxcabono = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    fechapago = models.IntegerField()
    valorpago = models.IntegerField()
    saldoanterior = models.IntegerField()
    idcxc = models.ForeignKey(Cxc, models.DO_NOTHING, db_column='idcxc')
    idtdoc = models.ForeignKey('Tipodocumentos', models.DO_NOTHING, db_column='idtdoc')

    class Meta:
        managed = False
        db_table = 'cxcabonos'


class Detallefacturas(models.Model):
    iddetallefac = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=8)
    subtotal = models.DecimalField(max_digits=12, decimal_places=8)
    descuento = models.DecimalField(max_digits=12, decimal_places=8)
    idfactura = models.ForeignKey('Facturas', models.DO_NOTHING, db_column='idfactura')
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto')
    idbodega = models.ForeignKey(Bodegas, models.DO_NOTHING, db_column='idbodega')

    class Meta:
        managed = False
        db_table = 'detallefacturas'


class Facturas(models.Model):
    idfactura = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    fecha = models.DateField()
    concepto = models.CharField(max_length=256)
    vencimiento = models.DateField()
    total = models.DecimalField(max_digits=12, decimal_places=8)
    exenta = models.DecimalField(max_digits=12, decimal_places=8)
    descuento = models.DecimalField(max_digits=12, decimal_places=8)
    anulado = models.BooleanField()
    impreso = models.BooleanField()
    idtdoc = models.ForeignKey('Tipodocumentos', models.DO_NOTHING, db_column='idtdoc')
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    idfactncred = models.ForeignKey('self', models.DO_NOTHING, db_column='idfactncred', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturas'


class Librocompras(models.Model):
    idlibcom = models.AutoField(primary_key=True)
    registro = models.CharField(max_length=20)
    comprobante = models.CharField(max_length=20)
    fecha = models.DateField()
    afecta = models.DecimalField(max_digits=12, decimal_places=8)
    exenta = models.DecimalField(max_digits=12, decimal_places=8)
    iva = models.DecimalField(max_digits=12, decimal_places=8)
    subtotal = models.DecimalField(max_digits=12, decimal_places=8)
    total = models.DecimalField(max_digits=12, decimal_places=8)
    descuento = models.DecimalField(max_digits=12, decimal_places=8)
    retencion = models.DecimalField(max_digits=12, decimal_places=8)
    percepcion = models.DecimalField(max_digits=12, decimal_places=8)
    idproveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='idproveedor')
    idtdoc = models.ForeignKey('Tipodocumentos', models.DO_NOTHING, db_column='idtdoc')

    class Meta:
        managed = False
        db_table = 'librocompras'


class Libroventascf(models.Model):
    idlibvencf = models.AutoField(primary_key=True)
    afecta = models.DecimalField(max_digits=12, decimal_places=8)
    exenta = models.DecimalField(max_digits=12, decimal_places=8)
    iva = models.DecimalField(max_digits=12, decimal_places=8)
    total = models.DecimalField(max_digits=12, decimal_places=8)
    exportacion = models.DecimalField(max_digits=12, decimal_places=8)
    fecha = models.DateField()
    anulado = models.BooleanField()
    facturas_idfactura = models.ForeignKey(Facturas, models.DO_NOTHING, db_column='facturas_idfactura')

    class Meta:
        managed = False
        db_table = 'libroventascf'


class Libroventasfacturas(models.Model):
    idlibvenfa = models.AutoField(primary_key=True)
    afecta = models.DecimalField(max_digits=12, decimal_places=8)
    exenta = models.DecimalField(max_digits=12, decimal_places=8)
    iva = models.DecimalField(max_digits=12, decimal_places=8)
    total = models.DecimalField(max_digits=12, decimal_places=8)
    exportacion = models.DecimalField(max_digits=12, decimal_places=8)
    fecha = models.DateField()
    anulado = models.BooleanField()
    idfactura = models.ForeignKey(Facturas, models.DO_NOTHING, db_column='idfactura', related_name='factura')
    idfactncred = models.ForeignKey(Facturas, models.DO_NOTHING, db_column='idfactncred', related_name='ncred')

    class Meta:
        managed = False
        db_table = 'libroventasfacturas'


class Movimientos(models.Model):
    idmovimiento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    costomovimiento = models.DecimalField(max_digits=12, decimal_places=8)
    costopromedio = models.DecimalField(max_digits=12, decimal_places=8)
    concepto = models.CharField(max_length=250)
    responsable = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    bodega1 = models.ForeignKey(Bodegas, models.DO_NOTHING, db_column='bodega1', related_name='bodega1')
    bodega2 = models.ForeignKey(Bodegas, models.DO_NOTHING, db_column='bodega2', related_name='bodega2')
    codproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='codproducto')
    tmov = models.ForeignKey('Tipomovimientos', models.DO_NOTHING, db_column='tmov')
    idfactura = models.ForeignKey(Facturas, models.DO_NOTHING, db_column='idfactura', null=True)
    idtdoctransferencia = models.ForeignKey('Tipodocumentos', models.DO_NOTHING, db_column='idtdoctransferencia', null=True)
    idlibcom = models.ForeignKey(Librocompras, models.DO_NOTHING, db_column='idlibcom', null=True)

    class Meta:
        managed = False
        db_table = 'movimientos'


class Productos(models.Model):
    idproducto = models.AutoField(primary_key=True)
    codigoprod = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    marca = models.CharField(max_length=50)
    existenciamax = models.DecimalField(max_digits=12, decimal_places=8)
    existenciamin = models.DecimalField(max_digits=12, decimal_places=8)
    existenciaactual = models.DecimalField(max_digits=12, decimal_places=8)
    idcategoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='idcategoria')
    idbodega = models.ForeignKey(Bodegas, models.DO_NOTHING, db_column='idbodega')

    class Meta:
        managed = False
        db_table = 'productos'

    def __str__(self):
        return self.codigoprod


class Proveedores(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    codigoprov = models.CharField(max_length=50)
    registro = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    email = models.CharField(max_length=50)
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=50)
    dui = models.CharField(max_length=9)
    saldo = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'proveedores'


class Tipodocumentos(models.Model):
    idtdoc = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipodocumentos'


class Tipomovimientos(models.Model):
    idtmov = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipomovimientos'
