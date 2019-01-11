# Generated by Django 2.0.5 on 2019-01-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodegas',
            fields=[
                ('idbodega', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'managed': False,
                'db_table': 'bodegas',
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idcategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'managed': False,
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idcliente', models.AutoField(primary_key=True, serialize=False)),
                ('codigocli', models.CharField(max_length=50)),
                ('registro', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=50)),
                ('dui', models.CharField(max_length=9)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'managed': False,
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Correlativos',
            fields=[
                ('idcorrelativo', models.AutoField(primary_key=True, serialize=False)),
                ('resolucion', models.CharField(max_length=10)),
                ('prefijo', models.CharField(max_length=10)),
                ('minimo', models.IntegerField()),
                ('maximo', models.IntegerField()),
                ('fecha', models.DateField()),
                ('activo', models.BooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'correlativos',
            },
        ),
        migrations.CreateModel(
            name='Cxc',
            fields=[
                ('idcxc', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.DecimalField(decimal_places=8, max_digits=12)),
                ('cargo', models.DecimalField(decimal_places=8, max_digits=12)),
                ('abono', models.DecimalField(decimal_places=8, max_digits=12)),
                ('saldo', models.DecimalField(decimal_places=8, max_digits=12)),
                ('fecha', models.DateField()),
                ('fechavencimiento', models.DateField()),
            ],
            options={
                'managed': False,
                'db_table': 'cxc',
            },
        ),
        migrations.CreateModel(
            name='Cxcabonos',
            fields=[
                ('idcxcabono', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('fechapago', models.IntegerField()),
                ('valorpago', models.IntegerField()),
                ('saldoanterior', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'cxcabonos',
            },
        ),
        migrations.CreateModel(
            name='Detallefacturas',
            fields=[
                ('iddetallefac', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=8, max_digits=12)),
                ('subtotal', models.DecimalField(decimal_places=8, max_digits=12)),
                ('descuento', models.DecimalField(decimal_places=8, max_digits=12)),
            ],
            options={
                'managed': False,
                'db_table': 'detallefacturas',
            },
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('idfactura', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('concepto', models.CharField(max_length=256)),
                ('vencimiento', models.DateField()),
                ('total', models.DecimalField(decimal_places=8, max_digits=12)),
                ('exenta', models.DecimalField(decimal_places=8, max_digits=12)),
                ('descuento', models.DecimalField(decimal_places=8, max_digits=12)),
                ('anulado', models.BooleanField()),
                ('impreso', models.BooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'facturas',
            },
        ),
        migrations.CreateModel(
            name='Librocompras',
            fields=[
                ('idlibcom', models.AutoField(primary_key=True, serialize=False)),
                ('registro', models.CharField(max_length=20)),
                ('comprobante', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('afecta', models.DecimalField(decimal_places=8, max_digits=12)),
                ('exenta', models.DecimalField(decimal_places=8, max_digits=12)),
                ('iva', models.DecimalField(decimal_places=8, max_digits=12)),
                ('subtotal', models.DecimalField(decimal_places=8, max_digits=12)),
                ('total', models.DecimalField(decimal_places=8, max_digits=12)),
                ('descuento', models.DecimalField(decimal_places=8, max_digits=12)),
                ('retencion', models.DecimalField(decimal_places=8, max_digits=12)),
                ('percepcion', models.DecimalField(decimal_places=8, max_digits=12)),
            ],
            options={
                'managed': False,
                'db_table': 'librocompras',
            },
        ),
        migrations.CreateModel(
            name='Libroventascf',
            fields=[
                ('idlibvencf', models.AutoField(primary_key=True, serialize=False)),
                ('afecta', models.DecimalField(decimal_places=8, max_digits=12)),
                ('exenta', models.DecimalField(decimal_places=8, max_digits=12)),
                ('iva', models.DecimalField(decimal_places=8, max_digits=12)),
                ('total', models.DecimalField(decimal_places=8, max_digits=12)),
                ('exportacion', models.DecimalField(decimal_places=8, max_digits=12)),
                ('fecha', models.DateField()),
                ('anulado', models.BooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'libroventascf',
            },
        ),
        migrations.CreateModel(
            name='Libroventasfacturas',
            fields=[
                ('idlibvenfa', models.AutoField(primary_key=True, serialize=False)),
                ('afecta', models.DecimalField(decimal_places=8, max_digits=12)),
                ('exenta', models.DecimalField(decimal_places=8, max_digits=12)),
                ('iva', models.DecimalField(decimal_places=8, max_digits=12)),
                ('total', models.DecimalField(decimal_places=8, max_digits=12)),
                ('exportacion', models.DecimalField(decimal_places=8, max_digits=12)),
                ('fecha', models.DateField()),
                ('anulado', models.BooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'libroventasfacturas',
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('idmovimiento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('costomovimiento', models.DecimalField(decimal_places=8, max_digits=12)),
                ('costopromedio', models.DecimalField(decimal_places=8, max_digits=12)),
                ('concepto', models.CharField(max_length=250)),
                ('responsable', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'movimientos',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idproducto', models.AutoField(primary_key=True, serialize=False)),
                ('codigoprod', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=50)),
                ('existenciamax', models.DecimalField(decimal_places=8, max_digits=12)),
                ('existenciamin', models.DecimalField(decimal_places=8, max_digits=12)),
                ('existenciaactual', models.DecimalField(decimal_places=8, max_digits=12)),
            ],
            options={
                'managed': False,
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('idproveedor', models.AutoField(primary_key=True, serialize=False)),
                ('codigoprov', models.CharField(max_length=50)),
                ('registro', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=50)),
                ('dui', models.CharField(max_length=9)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'managed': False,
                'db_table': 'proveedores',
            },
        ),
        migrations.CreateModel(
            name='Tipodocumentos',
            fields=[
                ('idtdoc', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'managed': False,
                'db_table': 'tipodocumentos',
            },
        ),
        migrations.CreateModel(
            name='Tipomovimientos',
            fields=[
                ('idtmov', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'managed': False,
                'db_table': 'tipomovimientos',
            },
        ),
    ]
