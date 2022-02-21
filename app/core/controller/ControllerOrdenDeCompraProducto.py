from ..serializers import OrdenDeCompraProductoSerializer
from ..models import Orden_De_Compra, Orden_De_Compra_Producto, Unidad


class ControllerOrdenDeCompraProducto:
    def crearordendecompraproducto(request):
        datos = request.data
        try:
            unidad = Unidad.objects.get(id_unidad = datos['unidad'])
            compra = Orden_De_Compra.objects.get(id = datos['compra'])

            ordenCompraNuevo = Orden_De_Compra_Producto.objects.create(
                nombre = datos['nombre'],
                cantidad = datos['cantidad'],
                cantidad_recibida = datos['cantidad_recibida'],
                unidad = unidad, 
                precio  = datos['precio'],
                oc_moneda = datos['oc_moneda'],
                total = datos['total'],
                compra =  compra
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_producto': ordenCompraNuevo.nombre}
       
    def listarordendecompraproducto(id=None):
        if id:
            try:
                queryset = Orden_De_Compra_Producto.objects.get(id=id)
            except Orden_De_Compra_Producto.DoesNotExist:
                return ({'result': 'No se encontró el producto de orden de compra deseado'})
            serializer = OrdenDeCompraProductoSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Producto.objects.all()
            serializer = OrdenDeCompraProductoSerializer(queryset, many=True)
            return serializer.data
