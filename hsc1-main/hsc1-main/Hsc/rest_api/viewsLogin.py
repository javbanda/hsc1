from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

from Inicio.models import Usuario
from .serializers import UsuarioSerializer

@csrf_exempt
@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data.get('username')
    password = data.get('password')

    try:
        user = Usuario.objects.get(username=username)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario inválido'}, status=status.HTTP_400_BAD_REQUEST)

    if user.contrasennia == password:
        token, created = Token.objects.get_or_create(user=user)
        serializer = UsuarioSerializer(user)
        return Response({
            'token': token.key,
            'usuario': serializer.data,
            'mensaje': 'Login exitoso'
        })
    else:
        return Response({'error': 'Contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
