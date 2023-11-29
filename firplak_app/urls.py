from django.urls import path
from . import views

urlpatterns = [

    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('pedidos/<int:pedido_id>/editar/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/<int:pedido_id>/eliminar/', views.eliminar_pedido, name='eliminar_pedido'),

    path('documentos-entrega/', views.lista_documentos_entrega, name='lista_documentos_entrega'),
    path('documentos-entrega/<int:documento_id>/', views.detalle_documento_entrega, name='detalle_documento_entrega'),
    path('guias-transporte/', views.lista_guias_transporte, name='lista_guias_transporte'),
    path('pods/', views.lista_pods, name='lista_pods'),
    path('index/', views.dashboard_view, name='dashboard'),
]
