from ..serializers import ParteDetalleSerializer
from ..models import Inventario_Vale, Parte_Detalle, Stock, Stock_Entrada

class ControllerParteDetalle:
    serializer_class = ParteDetalleSerializer
        
    def crearpartedetalle(request):
        datosParteDetalle = request.data
        try:
            stock = Stock.objects.get(id_stock = datosParteDetalle['stock'])
            stock_entrada = Stock_Entrada.objects.get(id_stock_entrada = datosParteDetalle['stock_entrada'])
            inventario_vale = Inventario_Vale.objects.get(id_inventario_vale = datosParteDetalle['inventario_vale'])

            parteDetalleNuevo = Parte_Detalle.objects.create(
                orden_trabajo_parte  = datosParteDetalle['orden_trabajo_parte'],
                stock = stock,
                stock_entrada = stock_entrada,
                cantidad = datosParteDetalle['cantidad'],
                inventario_vale = inventario_vale,
            )            
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'parte_detalle': parteDetalleNuevo.cantidad}

    def listarpartedetalle(id_partedetalle=None):
        if id_partedetalle:
            try:
                queryset = Parte_Detalle.objects.get(id_partedetalle=id_partedetalle)
            except Parte_Detalle.DoesNotExist:
                return ({'result': 'No se encontró el detalle de parte deseado'})
            serializer = ParteDetalleSerializer(queryset)
            return serializer.data
        else:
            queryset = Parte_Detalle.objects.all()
            serializer = ParteDetalleSerializer(queryset, many=True)
            return serializer.data
