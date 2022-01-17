from ..serializers import UsuarioRevisarSerializer
from ..models import Usuario, Usuario_Revisar


class ControllerUsuarioRevisar:

    def crearusuariorevisar(request):
        datosUsuario = request.data
        try:
            usuario = Usuario.objects.get(id_usuario = datosUsuario['usuario'])
            usuarioRevisarNuevo = Usuario_Revisar.objects.create(
                usuario = usuario
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'usuario_revisar': usuarioRevisarNuevo.usuario}

    def listarusuariorevisar(id_usuario_revisar=None):
        if id_usuario_revisar:
            try:
                queryset = Usuario_Revisar.objects.get(id_usuario_revisar=id_usuario_revisar)
            except Usuario_Revisar.DoesNotExist:
                return ({'result': 'No se encontró el usuario a revisar deseado'})
            serializer = UsuarioRevisarSerializer(queryset)
            return serializer.data
        else:
            queryset = Usuario_Revisar.objects.all()
            serializer = UsuarioRevisarSerializer(queryset, many=True)
            return serializer.data