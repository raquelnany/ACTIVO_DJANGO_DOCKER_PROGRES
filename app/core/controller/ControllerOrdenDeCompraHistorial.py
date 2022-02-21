from ..serializers import OrdenDeCompraHistorialSerializer
from ..models import Orden_De_Compra, Orden_De_Compra_Accion, Orden_De_Compra_Estado, Orden_De_Compra_Historial, Usuario


class ControllerOrdenDeCompraHistorial:
    def crearordendecomprahistorial(request):
        datos = request.data
        try:
            oc = Orden_De_Compra.objects.get(id = datos['oc'])
            usuario = Usuario.objects.get(id_usuario = datos['usuario'])
            estado = Orden_De_Compra_Estado.objects.get(id = datos['estado'])
            accion = Orden_De_Compra_Accion.objects.get(id =  datos['accion'] )
           
            ordenCompraNuevo = Orden_De_Compra_Historial.objects.create(
                usuario  = usuario,
                estado = estado,   
                oc = oc,   
                accion = accion, 
                fecha = datos['fecha'],
                hora = datos['hora'],
                timestamp = datos['timestamp']   
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_historial': ordenCompraNuevo.id}
       
    def listarordendecompraemailvisto(id=None):
        if id:
            try:
                queryset = Orden_De_Compra_Historial.objects.get(id=id)
            except Orden_De_Compra_Historial.DoesNotExist:
                return ({'result': 'No se encontró el historial de orden de compra deseado'})
            serializer = OrdenDeCompraHistorialSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Historial.objects.all()
            serializer = OrdenDeCompraHistorialSerializer(queryset, many=True)
            return serializer.data
