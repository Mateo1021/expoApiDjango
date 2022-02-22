

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer

class HelloApiView(APIView):
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
        'Se pueden usar metodos de HTTP como funciones(Get, Post, Patch, Put, Delete)',
        'Es similar a una vista tradicional de django',
        'Da una mayor control de la logica de la aplicacion',
        'los urls se mapean manual mente ',
        ]
        return Response({'message': 'Ventajas de usar APIView', 'an_apiview': an_apiview})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            message= f'hola {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

