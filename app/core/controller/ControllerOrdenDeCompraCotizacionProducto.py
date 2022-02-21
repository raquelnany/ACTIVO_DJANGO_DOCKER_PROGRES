from ..serializers import OrdenDeCompraCotizacionProductoSerializer
from ..models import Orden_De_Compra_Cotizacion_Producto


class ControllerOrdenDeCompraCotizacionProducto:
    def crearordendecompracotizacionproducto(request):
        datos = request.data
        try:
           ordenCompraNuevo = Orden_De_Compra_Cotizacion_Producto.objects.create(
                producto = datos['producto'],  
                precio = datos['precio'],
                moneda = datos['moneda'],
                precio_divisa =  datos['precio_divisa'],
                total  = datos['total'],
                fk_oc_cotizacion = datos['fk_oc_cotizacion']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_producto': ordenCompraNuevo.nombre}
       
    def listarordendecompracotizacionproducto(id=None):
        if id:
            try:
                queryset = Orden_De_Compra_Cotizacion_Producto.objects.get(id=id)
            except Orden_De_Compra_Cotizacion_Producto.DoesNotExist:
                return ({'result': 'No se encontró la cotizacion de producto de orden de compra deseada'})
            serializer = OrdenDeCompraCotizacionProductoSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Cotizacion_Producto.objects.all()
            serializer = OrdenDeCompraCotizacionProductoSerializer(queryset, many=True)
            return serializer.data
