from ..serializers import StockDetalleSerializer
from ..models import CentroCosto, Stock_Detalle, Inventario, Unidad


class ControllerStockDetalle:

    def crearstockdetalle(request):
        datosStockDetalle = request.data
        try:
           inventario = Inventario.objects.get(id_inventario = datosStockDetalle['inventario'])
           centro_costos = CentroCosto.objects.get(id_centro_costos = datosStockDetalle['centro_costos'])
           unidad = Unidad.objects.get(id_unidad = datosStockDetalle['unidad'])
           
           stockDetalleNuevo = Stock_Detalle.objects.create(
            inventario = inventario,
            cuenta = datosStockDetalle['cuenta'],
            centro_costos = centro_costos,
            modelo = datosStockDetalle['modelo'],
            numero_serie = datosStockDetalle['numero_serie'],
            notas_detalles = datosStockDetalle['notas_detalle'],
            unidad = unidad,
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_stock_detalle': stockDetalleNuevo.cuenta}

    def listarstockdetalle(id_stock_detalle=None):
        if id_stock_detalle:
            try:
                queryset = Stock_Detalle.objects.get(id_stock_detalle=id_stock_detalle)
            except Stock_Detalle.DoesNotExist:
                return ({'result': 'No se encontró el detalle stock deseado'})
            serializer = StockDetalleSerializer(queryset)
            return serializer.data
        else:
            queryset = Stock_Detalle.objects.all()
            serializer = StockDetalleSerializer(queryset, many=True)
            return serializer.data