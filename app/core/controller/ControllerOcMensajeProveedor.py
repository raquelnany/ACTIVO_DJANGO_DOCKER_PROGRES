from ..serializers import OcMensajeProveedorSerializer
from ..models import Oc_Mensaje_Proveedor, Orden_De_Compra, Orden_De_Compra_Proveedor 


class ControllerOcMensajeProveedor:
    def creaocmensajeproveedor(request):
        datosOc = request.data
        try:
            oc = Orden_De_Compra.objects.get(id = datosOc['oc'])
            proveedor = Orden_De_Compra_Proveedor.objects.get(id_proveedor = datosOc['proveedor'])

            ocNuevo = Oc_Mensaje_Proveedor.objects.create(
                oc = oc,
                proveedor = proveedor,  
                fk_mensaje = datosOc['fk_mensaje']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'oc_mensaje_proveedor': ocNuevo.id }
       
    def listarocmensajeproveedor(id=None):
        if id:
            try:
                queryset = Oc_Mensaje_Proveedor.objects.get(id = id)
            except Oc_Mensaje_Proveedor.DoesNotExist:
                return ({'result': 'No se encontró el mensaje a proveedor de oc equipo deseada'})
            serializer = OcMensajeProveedorSerializer(queryset)
            return serializer.data
        else:
            queryset = Oc_Mensaje_Proveedor.objects.all()
            serializer = OcMensajeProveedorSerializer(queryset, many=True)
            return serializer.data
