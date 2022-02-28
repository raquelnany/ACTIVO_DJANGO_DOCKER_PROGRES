from ..serializers import UsuarioSesionSerializer
from ..models import Usuario, Usuario_Sesion 

class ControllerUsuarioSesion:
    def crearusuariosesion(request):
        datosusuario = request.data
        try:
            usuario = Usuario.objects.get(id_usuario = datosusuario['usuario'])

            usuarioNuevo = Usuario_Sesion.objects.create(
                usuario = usuario,
                fecha_inicio = datosusuario['fecha_inicio'],
                hora_inicio = datosusuario['hora_inicio'],
                fecha_cierre = datosusuario['fecha_cierre'],
                hora_cierre = datosusuario['hora_cierre']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'usuario_sesion_nuevo': usuarioNuevo.id_usuario_sesion}
       
    def listarusuariosesion(id_usuario_sesion=None):
        if id_usuario_sesion:
            try:
                queryset = Usuario_Sesion.objects.get(id_usuario_sesion = id_usuario_sesion)
            except Usuario_Sesion.DoesNotExist:
                return ({'result': 'No se encontró la sesion de usuario deseada'})
            serializer = UsuarioSesionSerializer(queryset)
            return serializer.data
        else:
            queryset = Usuario_Sesion.objects.all()
            serializer = UsuarioSesionSerializer(queryset, many=True)
            return serializer.data
