from ..serializers import OrdenDeCompraAccionSerializer
from ..models import Orden_De_Compra_Accion, Orden_De_Compra_Estado


class ControllerOrdenDeCompraAccion:
    def crearordendecompraaccion(request):
        datos = request.data
        try:
            estado = Orden_De_Compra_Estado.objects.get(id = datos['estado'])

            ordenCompraNuevo = Orden_De_Compra_Estado.objects.create(
                nombre_accion = datos['nombre_accion'],  
                clave_accion  = datos['clave_accion'],
                estado = estado     
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_accion': ordenCompraNuevo.nombre_accion}
       
    def listarordendecompraaccion(id=None):
        if id:
            try:
                queryset = Orden_De_Compra_Accion.objects.get(id=id)
            except Orden_De_Compra_Accion.DoesNotExist:
                return ({'result': 'No se encontró la accion de orden de compra deseada'})
            serializer = OrdenDeCompraAccionSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Accion.objects.all()
            serializer = OrdenDeCompraAccionSerializer(queryset, many=True)
            return serializer.data
