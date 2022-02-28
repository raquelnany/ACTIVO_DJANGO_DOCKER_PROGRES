from ..serializers import UsuarioActivoeamSerializer  
from ..models import Usuario, Usuario_Activoeam


class ControllerUsuarioActivoeam:
    def crearusuarioactivoeam(request):
        datosusuario = request.data
        try:
            usuario = Usuario.objects.get(id_usuario = datosusuario['usuario'])

            usuarioNuevo = Usuario_Activoeam.objects.create(
                usuario = usuario
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'usuario_activoeam_nuevo': usuarioNuevo.id_usuario_activoeam }
       
    def listarusuarioactivoeam(id_usuario_activoeam=None):
        if id_usuario_activoeam:
            try:
                queryset = Usuario_Activoeam.objects.get(id_usuario_activoeam = id_usuario_activoeam)
            except Usuario_Activoeam.DoesNotExist:
                return ({'result': 'No se encontró el usuario activoeam deseado'})
            serializer = UsuarioActivoeamSerializer(queryset)
            return serializer.data
        else:
            queryset = Usuario_Activoeam.objects.all()
            serializer = UsuarioActivoeamSerializer(queryset, many=True)
            return serializer.data
