import requests
from django.shortcuts import render
from rest_api.models import Producto as ProductoSimple, Cliente
from rest_api.serializers import ProductoSerializer, ClienteSerializer
from django.shortcuts import render
from Inicio.models import Usuario, TipoUsuario, Comuna, Region, Direccion, Venta, Categoria, TipoProd, Marca, Modelo, Producto, Detalle
from .serializers import (
    UsuarioSerializer, TipoUsuarioSerializer, ComunaSerializer, RegionSerializer, DireccionSerializer,
    VentaSerializer, CategoriaSerializer, TipoProdSerializer, MarcaSerializer, ModeloSerializer,
    ProductoSerializer, DetalleSerializer
)

from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_usuario(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def lista_tipousuario(request):
    tipousuarios = TipoUsuario.objects.all()
    serializer = TipoUsuarioSerializer(tipousuarios, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_comuna(request):
    comunas = Comuna.objects.all()
    serializer = ComunaSerializer(comunas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_region(request):
    regiones = Region.objects.all()
    serializer = RegionSerializer(regiones, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_direccion(request):
    direcciones = Direccion.objects.all()
    serializer = DireccionSerializer(direcciones, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_venta(request):
    ventas = Venta.objects.all()
    serializer = VentaSerializer(ventas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_categoria(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_tipoprod(request):
    tipoprods = TipoProd.objects.all()
    serializer = TipoProdSerializer(tipoprods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_marca(request):
    marcas = Marca.objects.all()
    serializer = MarcaSerializer(marcas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_modelo(request):
    modelos = Modelo.objects.all()
    serializer = ModeloSerializer(modelos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_producto(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lista_detalle(request):
    detalles = Detalle.objects.all()
    serializer = DetalleSerializer(detalles, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def vista_usuario(request, id):
    try:
        usuario = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = UsuarioSerializer(usuario, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print('Error:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def lista_producto_simple(request):
    if request.method == 'GET':
        productos = ProductoSimple.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def lista_cliente(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import requests  # Asegúrate de tenerlo importado arriba

@api_view(['GET'])
def obtener_clima(request):
    ciudad = request.query_params.get('ciudad', 'Santiago')
    api_key = 'TU_API_KEY_AQUI'  # Reemplaza esto con tu verdadera API Key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'

    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        return Response({
            'ciudad': ciudad,
            'temperatura': datos['main']['temp'],
            'descripcion': datos['weather'][0]['description']
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# API externa
def productos_mercadolibre(request):
    query = "gamer"  # puedes cambiar por "teclado gamer", "auriculares gamer", etc.
    url = f"https://api.mercadolibre.com/sites/MLC/search?q={query}"

    response = requests.get(url)
    data = response.json()

    productos = data.get("results", [])[:10]  # Tomamos los primeros 10 resultados

    return render(request, "productos_mercadolibre.html", {"productos": productos})
