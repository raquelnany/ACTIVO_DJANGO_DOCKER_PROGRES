from ..serializers import UsuarioControsenaSerializer
from ..models import Usuario, Usuario_Contrasena

class ControllerUsuarioContrasena:
    def crearusuariocontrasena(request):
        datosusuario = request.data
        try:
            usuario = Usuario.objects.get(id_usuario = datosusuario['usuario'])

            usuarioNuevo = Usuario_Contrasena.objects.create(
                usuario = usuario, 
                contrasena = datosusuario['contrasena'],
                fecha = datosusuario['fecha'],
                hora = datosusuario['hora']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'usuario_contrasena_nuevo': usuarioNuevo.id_usuario_contrasena }
       
    def listarusuariocontrasena(id_usuario_contrasena=None):
        if id_usuario_contrasena:
            try:
                queryset = Usuario_Contrasena.objects.get(id_usuario_contrasena = id_usuario_contrasena)
            except Usuario_Contrasena.DoesNotExist:
                return ({'result': 'No se encontró la contrasena de usuario deseada'})
            serializer = UsuarioControsenaSerializer(queryset)
            return serializer.data
        else:
            queryset = Usuario_Contrasena.objects.all()
            serializer = UsuarioControsenaSerializer(queryset, many=True)
            return serializer.data
