from django.contrib import admin
from app.facturacion.models import *

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'numero_de_documento', 'direccion', 'telefono')
    #list_filter = ('pais',)
    search_fields = ('nombres','numero_de_documento' )
    #list_editable = ('facturas')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    # list_filter = ('pais',)
    search_fields = ('nombre',)
    #list_editable = ('nombre')

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'fecha', 'total')
    list_filter = ('cliente',)
    #search_fields = ('numero_factura')
    #list_editable = ('detalles')

class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'cantidad', 'subtotal')
    list_filter = ('producto__nombre',)
    #search_fields = ('producto__nombre' )
    #list_editable = ('producto')

admin.site.register(Persona,PersonaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(DetalleFactura,DetalleFacturaAdmin)