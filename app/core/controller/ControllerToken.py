from ..serializers import TokenSerializer  
from ..models import Token, Usuario


class ControllerToken:
    def creartoken(request):
        datosToken = request.data
        try:
            usuario = Usuario.objects.get(id_usuario = datosToken['usuario'])

            hashNuevo = Token.objects.create(
                usuario = usuario,
                hash =    datosToken['hash']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_has': hashNuevo.hash}