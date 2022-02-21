from ..serializers import OrdenDeCompraMensajeSerializer
from ..models import Orden_De_Compra, Orden_De_Compra_Mensaje, Orden_De_Compra_Proveedor


class ControllerOrdenDeCompraMensaje:
    def crearordendecompramensaje(request):
        datos = request.data
        try:
            oc = Orden_De_Compra.objects.get(id = datos['oc'])
            oc_prov = Orden_De_Compra_Proveedor.objects.get(id_proveedor = datos['oc_prov'])
           
            ordenCompraNuevo = Orden_De_Compra_Mensaje.objects.create(
                oc = oc, 
                oc_prov = oc_prov, 
                mensaje = datos['mensaje'],
                timestamp = datos['timestamp']
   
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_mensaje': ordenCompraNuevo.id}
       
    def listarordendecompramensaje(id=None):
        if id:
            try:
                queryset = Orden_De_Compra_Mensaje.objects.get(id=id)
            except Orden_De_Compra_Mensaje.DoesNotExist:
                return ({'result': 'No se encontró el mensaje de costo de orden de compra deseado'})
            serializer = OrdenDeCompraMensajeSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Mensaje.objects.all()
            serializer = OrdenDeCompraMensajeSerializer(queryset, many=True)
            return serializer.data
