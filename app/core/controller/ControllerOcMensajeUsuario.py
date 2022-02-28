from ..serializers import  OcMensajeUsuarioSerializer
from ..models import  Oc_Mensaje_Usuario, Orden_De_Compra, Usuario 


class ControllerOcMensajeUsuario:
    def creaocmensajeusuario(request):
        datosOc = request.data
        try:
            oc = Orden_De_Compra.objects.get(id = datosOc['oc'])
            usuario = Usuario.objects.get(id_usuario = datosOc['usuario'])

            ocNuevo = Oc_Mensaje_Usuario.objects.create(
                oc = oc,
                usuario = usuario,  
                fk_mensaje = datosOc['fk_mensaje']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'oc_mensaje_usuario': ocNuevo.id }
       
    def listarocmensajeusuario(id=None):
        if id:
            try:
                queryset = Oc_Mensaje_Usuario.objects.get(id = id)
            except Oc_Mensaje_Usuario.DoesNotExist:
                return ({'result': 'No se encontró el mensaje a usuario de oc equipo deseada'})
            serializer = OcMensajeUsuarioSerializer(queryset)
            return serializer.data
        else:
            queryset = Oc_Mensaje_Usuario.objects.all()
            serializer = OcMensajeUsuarioSerializer(queryset, many=True)
            return serializer.data
