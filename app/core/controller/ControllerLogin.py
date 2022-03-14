from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework.authtoken.models import Token

class ControllerLogin:
    def login(request):
        datosLogin = request.data
        try: 
            username = datosLogin['username']
            password = datosLogin['password']
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return ({'result': 'Nombre de usuario incorrecto.'})
        
        if not password == user.password:
            return ({'result': 'Contraseña incorrecta.'})

        token, created = Token.objects.get_or_create(user=user)
        
        return({"Token:" : token.key})