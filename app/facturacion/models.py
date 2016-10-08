from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    numero_de_documento = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.nombres

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    numero_factura = models.CharField(max_length=20)
    cliente = models.ForeignKey(Persona,related_name='facturas')
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s %s'%(self.numero_factura,self.cliente.nombres)

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura,related_name='detalles')
    producto = models.ForeignKey(Producto)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
