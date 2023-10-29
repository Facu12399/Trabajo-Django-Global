from django.shortcuts import render, redirect, get_object_or_404
from inventario.models import Productos, Categoria
from .forms import FormProducto, FormCategoria
from django.contrib.auth.decorators import login_required

# Create your views here.
def listarproductos(req):
    productos=Productos.objects.all()
    categoria=Categoria.objects.all()
    formulario=FormProducto()
    form_categoria=FormCategoria()
    contexto={"productos":productos,"categoria":categoria,"formulario":formulario,"form_categoria":form_categoria}
    return render(req,"index.html",contexto)

@login_required
def crearProducto(req):
    form_producto = FormProducto(req.POST,req.FILES)
    if form_producto.is_valid():
        form_producto.save()
    return redirect('index')

@login_required
def crearCategoria(req):
    form_categoria = FormCategoria(req.POST,req.FILES)
    if form_categoria.is_valid():
        form_categoria.save()
    return redirect('index')

@login_required
def editarProducto(req,id):
    producto=get_object_or_404(Productos,id=id)
    
    if req.method == "GET":
        formulario = FormProducto(instance=producto)
        contexto = {"productos":producto,"formulario":formulario}
        return render(req,'editar.html',contexto)
    elif req.method == "POST":
        form_producto = FormProducto(req.POST,req.FILES,instance=producto)
        if form_producto.is_valid():
            form_producto.save()
            return redirect('index')

@login_required
def eliminarProducto(req,id):
    producto=Productos.objects.get(id=id)
    producto.delete()
    return redirect('index')
    