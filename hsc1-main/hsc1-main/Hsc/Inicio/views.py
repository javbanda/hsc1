from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import (Usuario, Direccion, Comuna, Region, TipoUsuario, 
                     Producto, Marca, Categoria, TipoProd)
from .Carrito import Carrito
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

# --- Vistas de Inicio y Admin ---
def inicio(request):
    return render(request, 'Inicio/index.html')

def inicioadmin(request):
    return render(request, 'Inicio/index_admin.html')

def menuadmin(request):
    return render(request, 'Inicio/dashboard-admin.html')

# --- Sesiones y Registro ---
def iniciar(request):
    return render(request, 'Inicio/inicio_sesion.html')

def iniciar_sesion(request):
    usuario1 = request.POST['usuario']
    contra1 = request.POST['contra']
    try:
        usuario2 = Usuario.objects.get(username=usuario1, contrasennia=contra1)
        if usuario2.tipousuario.idTipoUsuario == 1:
            return redirect('menu_admin')
        else:
            return render(request, 'Inicio/index.html', {"usuario": usuario2})
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario o contraseña incorrectos')
        return redirect('iniciar')

def registrarse(request):
    contexto = {
        "comunas_m": Comuna.objects.all(),
        "regiones_m": Region.objects.all()
    }
    return render(request, "Inicio/registrarse.html", contexto)

def registrar_m(request):
    user = request.POST['usuario']
    if Usuario.objects.filter(username=user).exists():
        messages.error(request, 'El usuario ya existe')
        return redirect('registrarse')
    usuario = Usuario.objects.create(
        username=user,
        contrasennia=request.POST['contra'],
        nombre=request.POST['nombre'],
        apellido=request.POST['apellido'],
        email=request.POST['email'],
        tipousuario=TipoUsuario.objects.get(idTipoUsuario=2)
    )
    Direccion.objects.create(
        descripcionDir=request.POST['direccion'],
        usuario=usuario,
        region=Region.objects.get(idRegion=request.POST['region'])
    )
    return redirect('iniciar')

# --- Perfil de Usuario ---
def perfilusuario(request, id):
    usuario = Usuario.objects.get(username=id)
    return render(request, 'Inicio/perfil-user.html', {"usuario": usuario})

def mostrarperfil(request, id):
    contexto = {
        "usuario": Usuario.objects.get(username=id),
        "direccion": Direccion.objects.get(usuario=id),
        "region": Region.objects.all(),
        "comuna": Comuna.objects.all()
    }
    return render(request, 'Inicio/perfil_usuario.html', contexto)

def modificarPerfil(request, id):
    usuario = Usuario.objects.get(username=id)
    usuario.username = request.POST['username']
    usuario.nombre = request.POST['nomusu']
    usuario.apellido = request.POST['apepusu']
    usuario.email = request.POST['mailusu']
    usuario.save()
    messages.success(request, 'Perfil modificado correctamente!')
    return render(request, 'Inicio/perfil-user.html', {"usuario": usuario})

# --- Productos por Categoría ---
def productos_categoria(request, id, tipo_id, template_user, template_admin):
    productos = Producto.objects.filter(tipoprod=tipo_id)
    usuario = Usuario.objects.get(username=id)
    contexto = {"productos": productos, "usuario": usuario}
    template = template_user if usuario.tipousuario.idTipoUsuario == 2 else template_admin
    return render(request, template, contexto)

def detalle_producto(request, idp, usuario):
    contexto = {
        "prod": Producto.objects.get(idProducto=idp),
        "usuario": Usuario.objects.get(username=usuario)
    }
    return render(request, "Inicio/mic1.html", contexto)

# --- Agregar / Editar / Eliminar Productos ---
def addprod(request):
    contexto = {
        "tipoProd": TipoProd.objects.all(),
        "Marca": Marca.objects.all()
    }
    return render(request, 'Inicio/agregar_producto.html', contexto)

def newProd(request):
    if Producto.objects.filter(nombreProducto=request.POST['nomprod']).exists():
        messages.error(request, 'El producto ya existe')
        return redirect('addprod')
    Producto.objects.create(
        nombreProducto=request.POST['nomprod'],
        precioProducto=request.POST['precio'],
        especificacionProd=request.POST['descprod'],
        stockProd=request.POST['stockprod'],
        imagenProd=request.FILES['imgprod'],
        tipoprod=TipoProd.objects.get(idTiporod=request.POST['tipoprod']),
        marca=Marca.objects.get(idMarca=request.POST['marcaprod'])
    )
    return redirect('menu_admin')

def eliminarProducto(request, idProducto):
    Producto.objects.get(idProducto=idProducto).delete()
    messages.success(request, 'Producto eliminado')
    return redirect('indexadmin')

def edicionProducto(request, idProducto):
    contexto = {
        "producto": Producto.objects.get(idProducto=idProducto),
        "tipoProd": TipoProd.objects.all(),
        "Marca": Marca.objects.all()
    }
    return render(request, 'Inicio/edicionProducto.html', contexto)

def editarProducto(request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    producto.nombreProducto = request.POST['nomprod']
    producto.tipoprod = TipoProd.objects.get(idTiporod=request.POST['tipoprod'])
    producto.marca = Marca.objects.get(idMarca=request.POST['marcaprod'])
    producto.stockProd = request.POST['stockprod']
    producto.precioProducto = request.POST['precio']
    producto.especificacionProd = request.POST['descprod']
    if request.FILES.get("imgprod"):
        producto.imagenProd = request.FILES['imgprod']
    producto.save()
    messages.success(request, 'Producto modificado')
    return redirect('indexadmin')

# --- Carrito ---
def carrito_view(request, id):
    return render(request, 'Inicio/carrito.html', {"usuario": Usuario.objects.get(username=id)})

def modificar_carrito(request, idProducto, usuario, accion):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=idProducto)
    acciones = {
        'agregar': carrito.agregar,
        'eliminar': carrito.eliminar,
        'restar': carrito.restar,
        'limpiar': carrito.limpiar
    }
    if accion in acciones:
        if accion == 'limpiar':
            acciones[accion]()
        else:
            acciones[accion](producto)
    return render(request, 'Inicio/carrito.html', {"usuario": Usuario.objects.get(username=usuario)})

# --- API Externa Dólar ---
@api_view(['GET'])
def obtener_dolar(request):
    try:
        response = requests.get('https://mindicador.cl/api/dolar')
        data = response.json()
        return Response({
            'valor_dolar': data['serie'][0]['valor'],
            'fecha': data['serie'][0]['fecha']
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)

def ver_dolar_chart(request):
    return render(request, 'Inicio/dolar_chart.html')

# --- API Externa MercadoLibre + Chart.js ---
def productos_mercadolibre(request):
    query = request.GET.get('query', 'gamer')
    try:
        response = requests.get(f"https://api.mercadolibre.com/sites/MLC/search?q={query}")
        data = response.json()
        productos = data.get("results", [])[:12]
        nombres = [p['title'] for p in productos]
        precios = [p['price'] for p in productos]
        return render(request, "productos_mercadolibre.html", {
            "productos": productos,
            "nombres": nombres,
            "precios": precios,
            "query": query,
        })
    except Exception as e:
        messages.error(request, f"Error al obtener datos de MercadoLibre: {e}")
        return redirect('inicio')
