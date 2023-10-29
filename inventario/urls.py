from django.urls import path
from inventario.views import listarproductos,crearProducto,crearCategoria,editarProducto,eliminarProducto

urlpatterns = [
    path('',listarproductos,name="index"),
    path('crearP',crearProducto,name="crearP"),
    path('crearC',crearCategoria,name="crearC"),
    path('editar/<id>',editarProducto,name="editar"),
    path('eliminar/<id>',eliminarProducto,name="eliminar"),
]
