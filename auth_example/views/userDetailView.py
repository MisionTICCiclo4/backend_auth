from rest_framework                    import status, generics
from rest_framework.response           import Response
from rest_framework.permissions        import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf                       import settings

from auth_example.models.user          import User
from auth_example.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer #Al retornar usa el to_representation del serializer
    permission_classes = (IsAuthenticated,) #Si no está autenticado, no tiene permisos 

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:] #Bearer TOKEN. El Token empieza en el caracter 7 de la cadena.
        token_backend =  TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) #Algoritmo con el que haremos la decodificación
        valid_data = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['pk']:       #El usuario sobre el cual está generado el token esté pidiendo información de su propio usuario y no de otro
            string_response = {'detail': "Acceso no autorizado"}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(self, request, *args, **kwargs)

class UserUpdateView(generics.UpdateAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer #Al retornar usa el to_representation del serializer
    permission_classes = (IsAuthenticated) #Si no está autenticado, no tiene permisos 

    def update(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:] #Bearer TOKEN. El Token empieza en el caracter 7 de la cadena.
        token_backend =  TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) #Algoritmo con el que haremos la decodificación
        valid_data = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['pk']:       #El usuario sobre el cual está generado el token esté pidiendo información de su propio usuario y no de otro
            string_response = {'update': "Acceso no autorizado"}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(self, request, *args, **kwargs)

class UserDeleteView(generics.DestroyAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer #Al retornar usa el to_representation del serializer
    permission_classes = (IsAuthenticated) #Si no está autenticado, no tiene permisos 

    def delete(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:] #Bearer TOKEN. El Token empieza en el caracter 7 de la cadena.
        token_backend =  TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) #Algoritmo con el que haremos la decodificación
        valid_data = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['pk']:       #El usuario sobre el cual está generado el token esté pidiendo información de su propio usuario y no de otro
            string_response = {'delete': "Acceso no autorizado"}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(self, request, *args, **kwargs)