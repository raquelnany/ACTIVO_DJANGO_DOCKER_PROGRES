from ..serializers import EstadoProductoRecibidoSerializer  
from ..models import Estado_Material, Estado_Paquete, Estado_Producto_Recibido, Estado_Sello, Orden_De_Compra, Orden_De_Compra_Producto

class ControllerEstadoProductoRecibido:
    def crearestadoproductorecibido(request):
        datos = request.data
        try:
            producto = Orden_De_Compra_Producto.objects.get(id = datos['producto'])
            oc = Orden_De_Compra.objects.get(id = datos['oc'])
            estado_paquete = Estado_Paquete.objects.get(id_estado_paquete = datos['estado_paquete'])
            estado_material = Estado_Material.objects.get(id_estado_material =  datos['estado_material'])
            estado_sello = Estado_Sello.objects.get(id_estado_sello = datos['estado_sello'])

            estadoProductoRecibidoNuevo = Estado_Producto_Recibido.objects.create(
                producto = producto,  
                oc = oc,
                estado_paquete = estado_paquete,
                estado_material = estado_material,
                estado_sello = estado_sello,
                fecha = datos['fecha'],
                hora = datos['hora']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_Estado_producto_recibido': estadoProductoRecibidoNuevo.id_estado_producto_recibido }
       
    def listarestadoproductorecibido(id_estado_producto_recibido=None):
        if id_estado_producto_recibido:
            try:
                queryset = Estado_Producto_Recibido.objects.get(id_estado_producto_recibido = id_estado_producto_recibido)
            except Estado_Producto_Recibido.DoesNotExist:
                return ({'result': 'No se encontró el estado de producto recibido deseado'})
            serializer = EstadoProductoRecibidoSerializer(queryset)
            return serializer.data
        else:
            queryset = Estado_Producto_Recibido.objects.all()
            serializer = EstadoProductoRecibidoSerializer(queryset, many=True)
            return serializer.data
