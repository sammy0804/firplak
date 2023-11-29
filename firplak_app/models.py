from django.db import models

class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pedido_id)


class LineaPedido(models.Model):
    linea_pedido_id = models.AutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_id = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_entrega_estimada = models.DateField()

    def __str__(self):
        return str(self.linea_pedido_id)


class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)  # MTO o MTS

    def __str__(self):
        return self.descripcion


class DocumentoEntrega(models.Model):
    documento_entrega_id = models.AutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return str(self.documento_entrega_id)


class GuiaTransporte(models.Model):
    guia_transporte_id = models.AutoField(primary_key=True)
    documento_entrega_id = models.ForeignKey(DocumentoEntrega, on_delete=models.CASCADE)
    transportista_id = models.ForeignKey('Transportista', on_delete=models.CASCADE)
    fecha_despacho = models.DateField()

    def __str__(self):
        return str(self.guia_transporte_id)


class POD(models.Model):
    pod_id = models.AutoField(primary_key=True)
    guia_transporte_id = models.ForeignKey(GuiaTransporte, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField()
    estado = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pod_id)


class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre


class Transportista(models.Model):
    transportista_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
