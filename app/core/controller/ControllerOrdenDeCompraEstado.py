from ..serializers import OrdenDeCompraEstadoSerializer
from ..models import Orden_De_Compra_Estado


class ControllerOrdenDeCompraEstado:
    def crearordendecompraestado(request):
        datos = request.data
        try:
            ordenCompraNuevo = Orden_De_Compra_Estado.objects.create(
                estado = datos['estado'],  
                clave  = datos['clave']        
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_estado': ordenCompraNuevo.estado}
       
    def listarordendecompraestado(id=None):
        if id:
            try:
                queryset = Orden_De_Compra_Estado.objects.get(id=id)
            except Orden_De_Compra_Estado.DoesNotExist:
                return ({'result': 'No se encontró el estado de orden de compra deseado'})
            serializer = OrdenDeCompraEstadoSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Estado.objects.all()
            serializer = OrdenDeCompraEstadoSerializer(queryset, many=True)
            return serializer.data
