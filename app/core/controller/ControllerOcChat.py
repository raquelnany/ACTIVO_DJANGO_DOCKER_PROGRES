from ..serializers import OcChatSerializer
from ..models import Oc_Chat, Orden_De_Compra_Cotizacion, Orden_De_Compra_Proveedor, Usuario


class ControllerOcChat:
    def crearocchat(request):
        datosOcChat = request.data
        try:
            usuario = Usuario.objects.get(id_usuario = datosOcChat['usuario'])
            prov = Orden_De_Compra_Proveedor.objects.get(id_proveedor = datosOcChat['prov'])
            cotizacion = Orden_De_Compra_Cotizacion.objects.get(id = datosOcChat['cotizacion'])

            ocChatNuevo = Oc_Chat.objects.create(
                usuario = usuario,
                fecha = datosOcChat['fecha'],
                hora = datosOcChat['hora'],
                timestamp = datosOcChat['timestamp'],
                prov = prov,
                mensaje = datosOcChat['mensaje'],
                cotizacion = cotizacion,
                envia = datosOcChat['envia']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'oc_chat_nuevo': ocChatNuevo.id_oc_chat }
       
    def listarocchat(id_oc_chat=None):
        if id_oc_chat:
            try:
                queryset = Oc_Chat.objects.get(id_oc_chat = id_oc_chat)
            except Oc_Chat.DoesNotExist:
                return ({'result': 'No se encontró el chat de oc deseado'})
            serializer = OcChatSerializer(queryset)
            return serializer.data
        else:
            queryset = Oc_Chat.objects.all()
            serializer = OcChatSerializer(queryset, many=True)
            return serializer.data
