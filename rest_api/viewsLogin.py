from django.shortcuts import render

from Hsc.Inicio.models import Modelo
from Inicio.models import usuario
from .serializers import UsuarioSerializer,TipoUsuarioSerializer, UsuarioSerializer, ComunaSerializer, RegionSerializer, DireccionSerializer, VentaSerializer, CategoriaSerializer, TipoProdSerializer, MarcaSerializer, ModeloSerializer,ProductoSerializer, DetalleSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@csrf_exempt
@api_view(['POST'])

def login(request):
    data = JSONParser().parse(request)
    
    username = data['username']
    password = data['password']
    
    try: 
        user = Usuario.objects.get(username=username)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario inválido'}, status=400)
    
    if user.contrasennia == password:
        return Response({'mensaje': 'Login exitoso'})
    else:
        return Response({'error': 'Contraseña incorrecta'}, status=400)
