from ..serializers import EmpaqueStockOrdenCompraSerializer
from ..models import Empaque_Stock_Orden_Compra, Empaque, EstatusUsuario, Proveedor, Usuario


class ControllerEmpaqueStockOrdenCompra:
    def crearempaquestockordencompra(request):
        datosEmpaque = request.data
        try:
            empaque = Empaque.objects.get(id_empaque = datosEmpaque['empaque'])
            user_entrada = Usuario.objects.get(id_usuario = datosEmpaque['user_stock'])
            proveedor = Proveedor.objects.get(id_proveedor = datosEmpaque['proveedor'])
            estatus = EstatusUsuario.objects.get(id_estatus = datosEmpaque['estatus'])

            empaqueNuevo = Empaque_Stock_Orden_Compra.objects.create(
                empaque = empaque,
                proveedor = proveedor,
                fecha_orden = datosEmpaque['fecha_orden'],
                fecha_recibido = datosEmpaque['fecha_recibido'],
                orden_compra =  datosEmpaque['orden_compra'],
                cantidad_recibida = datosEmpaque['cantidad_recibida'],
                precio_unitario = datosEmpaque['precio_unitario'],
                embargado_a = datosEmpaque['embargado_a'],
                user_entrada = user_entrada,
                cantidad_disponible = datosEmpaque['cantidad_disponible'],
                moneda = datosEmpaque['moneda'],
                dolares = datosEmpaque['dolares'],
                estatus = estatus
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque_stock_orden_compra': empaqueNuevo.id_empaque_stock_orden_compra}
       
    def listarempaquestockordencompra(id_empaque_stock_orden_compra = None):
        if id_empaque_stock_orden_compra:
            try:
                queryset = Empaque_Stock_Orden_Compra.objects.get(id_empaque_stock_orden_compra = id_empaque_stock_orden_compra)
            except Empaque_Stock_Orden_Compra.DoesNotExist:
                return ({'result': 'No se encontró el empaque stock orden compra deseado'})
            serializer = EmpaqueStockOrdenCompraSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque_Stock_Orden_Compra.objects.all()
            serializer = EmpaqueStockOrdenCompraSerializer(queryset, many=True)
            return serializer.data
