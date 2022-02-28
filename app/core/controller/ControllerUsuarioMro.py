from ..serializers import UsuarioMroSerializer
from ..models import Nivel_Gastos, Nivel_Mro, Usuario, Usuario_Mro    

class ControllerUsuarioMro:
    def crearusuariomro(request):
        datosusuario = request.data
        try:
            usuario = Usuario.objects.get(id_usuario = datosusuario['usuario'])
            nivel = Nivel_Mro.objects.get(id_nivel_mro = datosusuario['nivel'])
            gastos = Nivel_Gastos.objects.get(id_nivel_gastos = datosusuario['gastos'])

            usuarioNuevo = Usuario_Mro.objects.create(
                usuario = usuario,
                nivel = nivel,
                gastos = gastos
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'usuario_mro_nuevo': usuarioNuevo.id_usuario_mro}
       
    def listarusuariomro(id_usuario_mro=None):
        if id_usuario_mro:
            try:
                queryset = Usuario_Mro.objects.get(id_usuario_mro = id_usuario_mro)
            except Usuario_Mro.DoesNotExist:
                return ({'result': 'No se encontró el mro de usuario deseado'})
            serializer = UsuarioMroSerializer(queryset)
            return serializer.data
        else:
            queryset = Usuario_Mro.objects.all()
            serializer = UsuarioMroSerializer(queryset, many=True)
            return serializer.data
