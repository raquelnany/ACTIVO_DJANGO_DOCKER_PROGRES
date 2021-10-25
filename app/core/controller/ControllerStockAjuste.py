from ..serializers import StockAjusteSerializer
from ..models import Proveedor, Stock_Ajuste, Inventario, Stock_Entrada, Usuario


class ControllerStockAjuste:

    def crearstockajuste(request):
        datosStockAjuste = request.data
        try:
           stock_entrada = Stock_Entrada.objects.get(id_stock_entrada = datosStockAjuste['stock_entrada'])
           usuario_ajuste = Usuario.objects.get(id_usuario = datosStockAjuste['usuario_ajuste'])
           proveedor_1 = Proveedor.objects.get(id_proveedor = datosStockAjuste['proveedor_1'])
           proveedor_2 = Proveedor.objects.get(id_proveedor = datosStockAjuste['proveedor_2'])

           stockAjusteNuevo = Stock_Ajuste.objects.create(
            stock_entrada = stock_entrada,
            usuario_ajuste = usuario_ajuste,
            fecha_ajuste = datosStockAjuste['fecha_ajuste'],
            orden_compra_1 = datosStockAjuste['orden_compra_1'],
            orden_compra_2 = datosStockAjuste['orden_compra_2'],
            proveedor_1 = proveedor_1,
            proveedor_2 = proveedor_2,
            cantidad_1 = datosStockAjuste['cantidad_1'],
            cantidad_2 = datosStockAjuste['cantidad_2'],
            cantidad_disponible_1 = datosStockAjuste['cantidad_disponible_1'],
            cantidad_disponible_2 = datosStockAjuste['cantidad_disponible_2'],
            precio_unitario_1 = datosStockAjuste['precio_unitario_1'],
            precio_unitario_2 = datosStockAjuste['precio_unitario_2'],
            moneda_1 = datosStockAjuste['moneda_1'],
            moneda_2 = datosStockAjuste['moneda_2'],
            dolares_1 = datosStockAjuste['dolares_1'],
            dolares_2 = datosStockAjuste['dolares_2'],
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_stock_ajuste': stockAjusteNuevo.stock_entrada}

    def listarstockajuste(id_stock_ajuste=None):
        if id_stock_ajuste:
            try:
                queryset = Stock_Ajuste.objects.get(id_stock_ajuste=id_stock_ajuste)
            except Stock_Ajuste.DoesNotExist:
                return ({'result': 'No se encontró el ajuste de stock deseado'})
            serializer = StockAjusteSerializer(queryset)
            return serializer.data
        else:
            queryset = StockAjusteSerializer.objects.all()
            serializer = StockAjusteSerializer(queryset, many=True)
            return serializer.data