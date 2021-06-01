# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    idcliente = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    direccion = models.CharField(max_length=20)
    telefono = models.BigIntegerField()
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'cliente'


class Empleado(models.Model):
    idempleado = models.BigIntegerField(primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'empleado'


class Factura(models.Model):
    numero_factura = models.BigIntegerField(primary_key=True)
    nombre_empresa = models.CharField(max_length=20)
    run_empresa = models.CharField(max_length=12)
    fecha_venta = models.DateField()
    monto = models.BigIntegerField()
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa')

    class Meta:
        managed = False
        db_table = 'factura'


class OrdenCompra(models.Model):
    idorden_compra = models.BigIntegerField(primary_key=True)
    estado_orden = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    fecha_cierre = models.DateField()
    idempleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idempleado')
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor')

    class Meta:
        managed = False
        db_table = 'orden_compra'


class ProductoFamiliar(models.Model):
    idproductofamiliar = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'producto_familiar'


class Productos(models.Model):
    producto_id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    fecha_expiracion = models.DateField()
    descripcion = models.CharField(max_length=200)
    precio = models.BigIntegerField()
    stock = models.BigIntegerField()
    stock_critico = models.BigIntegerField()
    idtipoproducto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='idtipoproducto')
    idproductofamiliar = models.ForeignKey(ProductoFamiliar, models.DO_NOTHING, db_column='idproductofamiliar')

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedor(models.Model):
    idproveedor = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Recibo(models.Model):
    numero_recibo = models.BigIntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=10)
    rut_cliente = models.CharField(max_length=12)
    fecha_venta = models.DateField()
    monto = models.BigIntegerField()
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa')

    class Meta:
        managed = False
        db_table = 'recibo'


class Reporte(models.Model):
    idreporte = models.BigIntegerField(primary_key=True)
    fecha_reporte = models.DateField()
    total_ventas = models.BigIntegerField()
    monto_venta = models.BigIntegerField()
    total_visitas = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'reporte'


class TipoProducto(models.Model):
    idtipoproducto = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class Usuario(models.Model):
    idusuario = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'usuario'


class Vendedor(models.Model):
    idvendedor = models.BigIntegerField(primary_key=True)
    idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'vendedor'


class Venta(models.Model):
    idventa = models.BigIntegerField(primary_key=True)
    tipo = models.CharField(max_length=10)
    precio = models.BigIntegerField()
    discount = models.BigIntegerField()
    precio_final = models.BigIntegerField()
    metodo_pago = models.CharField(max_length=10)
    fecha = models.DateField()
    delivery = models.CharField(max_length=1)
    idvendedor = models.ForeignKey(Vendedor, models.DO_NOTHING, db_column='idvendedor')

    class Meta:
        managed = False
        db_table = 'venta'


class VentaProductos(models.Model):
    calidad_producto = models.CharField(primary_key=True, max_length=10)
    otros_detalles = models.CharField(max_length=10)
    idventa = models.ForeignKey(Venta, models.DO_NOTHING, db_column='idventa')

    class Meta:
        managed = False
        db_table = 'venta_productos'
