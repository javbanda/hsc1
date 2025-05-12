from django.shortcuts import render
from Inicio.models import Usuario
from .serializers import UsuarioSerializer,TipoUsuarioSerializer, UsuarioSerializer, ComunaSerializer, RegionSerializer, DireccionSerializer, VentaSerializer, CategoriaSerializer, TipoProdSerializer, MarcaSerializer, ModeloSerializer,ProductoSerializer, DetalleSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))

def lista_usuario(request):
    if request.method == 'GET':
        usuario = usuario.objects.all()
        serializer = UsuarioSerializer (usuario, many=True)
        return Response(serializer.data)
   
    elif request.method == 'POST':
        data = JASONParser().parser(request)
        serializer = UsuarioSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Responde(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print ('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def lista_tipousuario(request):
    tipousuarios = TipoUsuario.objects.all()
    serializer = TipoUsuarioSerializer(tipousuarios, many=True)
    return Response(serializer.data)


def lista_comuna(request):
    comunas = Comuna.objects.all()
    serializer = ComunaSerializer(comunas, many=True)
    return Response(serializer.data)


def lista_region(request):
    regiones = Region.objects.all()
    serializer = RegionSerializer(regiones, many=True)
    return Response(serializer.data)


def lista_direccion(request):
    direcciones = Direccion.objects.all()
    serializer = DireccionSerializer(direcciones, many=True)
    return Response(serializer.data)


def lista_venta(request):
    ventas = Venta.objects.all()
    serializer = VentaSerializer(ventas, many=True)
    return Response(serializer.data)


def lista_categoria(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)


def lista_tipoprod(request):
    tipoprods = TipoProd.objects.all()
    serializer = TipoProdSerializer(tipoprods, many=True)
    return Response(serializer.data)


def lista_marca(request):
    marcas = Marca.objects.all()
    serializer = MarcaSerializer(marcas, many=True)
    return Response(serializer.data)


def lista_modelo(request):
    modelos = Modelo.objects.all()
    serializer = ModeloSerializer(modelos, many=True)
    return Response(serializer.data)


def lista_producto(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)


def lista_detalle(request):
    detalles = Detalle.objects.all()
    serializer = DetalleSerializer(detalles, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def vista_usuario(request, id):
    try:
        usuario = Usuario.objects.get(username=id)  # O usa id si tu clave primaria fuera diferente
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