from ..serializers import UsuarioEventoSerializer
from ..models import Usuario, Usuario_Evento

class ControllerUsuarioEvento:
    def crearusuarioevento(request):
        datosusuario = request.data
        try:
            usuario_modifica = Usuario.objects.get(id_usuario = datosusuario['usuario_modifica'])
            usaurio_modificado = Usuario.objects.get(id_usuario = datosusuario['usaurio_modificado'])

            usuarioNuevo = Usuario_Evento.objects.create(
                usuario_modifica = usuario_modifica,
                movimiento = datosusuario['movimiento'],
                elemento = datosusuario['elemento'],
                anterior = datosusuario['anterior'],
                nuevo = datosusuario['nuevo'],
                fecha = datosusuario['fecha'],
                hora = datosusuario['hora'],
                usaurio_modificado =  usaurio_modificado
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'usuario_evento_nuevo': usuarioNuevo.id_usuario_evento}
       
    def listarusuarioevento(id_usuario_evento=None):
        if id_usuario_evento:
            try:
                queryset = Usuario_Evento.objects.get(id_usuario_evento = id_usuario_evento)
            except Usuario_Evento.DoesNotExist:
                return ({'result': 'No se encontró el evento de usuario deseado'})
            serializer = UsuarioEventoSerializer(queryset)
            return serializer.data
        else:
            queryset = Usuario_Evento.objects.all()
            serializer = UsuarioEventoSerializer(queryset, many=True)
            return serializer.data
