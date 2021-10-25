from ..serializers import StockEntradaSerializer
from ..models import Proveedor, Stock_Entrada, Inventario, Usuario


class ControllerStockEntrada:

    def crearstockentrada(request):
        datosStockEntrada = request.data
        try:
           inventario = Inventario.objects.get(id_inventario = datosStockEntrada['inventario'])
           proveedor = Proveedor.objects.get (id_proveedor = datosStockEntrada['proveedor'])
           user_entrada = Usuario.objects.get(id_usuario = datosStockEntrada['user_entrada'])

           stockEntradaNuevo = Stock_Entrada.objects.create(
            inventario = inventario,
            proveedor = proveedor,
            fecha_orden = datosStockEntrada['fecha_orden'],
            fecha_recibido = datosStockEntrada['fecha_recibido'],
            orden_compra = datosStockEntrada['orden_compra'],
            cantidad_recibida = datosStockEntrada['cantidad_recibida'],
            precio_unitario = datosStockEntrada['precio_unitario'],
            embargado_a = datosStockEntrada['embargado_a'],
            user_entrada =  user_entrada,
            cantidad_disponible = datosStockEntrada['cantidad_disponible'],
            moneda = datosStockEntrada['moneda'],
            dolares = datosStockEntrada['dolares'],
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_stock_entrada': stockEntradaNuevo.cantidad_disponible}

    def listarstockentrada(id_stock_entrada=None):
        if id_stock_entrada:
            try:
                queryset = Stock_Entrada.objects.get(id_stock_entrada=id_stock_entrada)
            except Stock_Entrada.DoesNotExist:
                return ({'result': 'No se encontró la entraada de stock deseada'})
            serializer = StockEntradaSerializer(queryset)
            return serializer.data
        else:
            queryset = Stock_Entrada.objects.all()
            serializer = StockEntradaSerializer(queryset, many=True)
            return serializer.data