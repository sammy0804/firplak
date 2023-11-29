from django.contrib import admin
from .models import Pedido, LineaPedido, Producto, DocumentoEntrega, GuiaTransporte, POD, Cliente, Transportista

# Registro básico
admin.site.register(Pedido)
admin.site.register(LineaPedido)
admin.site.register(Producto)
admin.site.register(DocumentoEntrega)
admin.site.register(GuiaTransporte)
admin.site.register(POD)
admin.site.register(Cliente)
admin.site.register(Transportista)

