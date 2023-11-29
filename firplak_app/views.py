from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido
from .forms import PedidoForm
from .models import DocumentoEntrega
from .models import GuiaTransporte
from .models import POD
from .models import Cliente
from .models import Producto


def dashboard_view(request):
    total_pedidos = Pedido.objects.count()
    total_productos = Producto.objects.count()
    total_clientes = Cliente.objects.count()

    context = {
        'total_pedidos': total_pedidos,
        'total_productos': total_productos,
        'total_clientes': total_clientes
    }
    return render(request, 'dashboard.html', context)


def lista_pedidos(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()

    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos, 'form': form})



def actualizar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'actualizar_pedido.html', {'form': form})


def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'GET':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'lista_pedidos.html', {'pedido': pedido})


def detalle_pedido(request, pedido_id):
    pedido = Pedido.objects.get(pk=pedido_id)
    lineas_pedido = pedido.lineapedido_set.all()
    return render(request, 'detalle_pedido.html', {'pedido': pedido, 'lineas_pedido': lineas_pedido})


def lista_documentos_entrega(request):
    documentos = DocumentoEntrega.objects.all()
    return render(request, 'lista_documentos_entrega.html', {'documentos': documentos})


def detalle_documento_entrega(request, documento_id):
    documento = DocumentoEntrega.objects.get(pk=documento_id)
    return render(request, 'detalle_documento_entrega.html', {'documento': documento})


def lista_guias_transporte(request):
    guias = GuiaTransporte.objects.all()
    return render(request, 'lista_guias_transporte.html', {'guias': guias})


def lista_pods(request):
    pods = POD.objects.all()
    return render(request, 'lista_pods.html', {'pods': pods})