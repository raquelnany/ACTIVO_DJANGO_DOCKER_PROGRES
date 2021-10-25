from ..serializers import StockSerializer
from ..models import Stock, Instalacion, Inventario


class ControllerStock:

    def crearstock(request):
        datosStock = request.data
        try:
           instalacion = Instalacion.objects.get(id_instalacion = datosStock['instalacion'])
           inventario = Inventario.objects.get(id_inventario = datosStock['inventario'])
           stockNuevo = Stock.objects.create(
            instalacion = instalacion,
            inventario = inventario,
            cantidad_actual = datosStock['cantaidad_actual'],
            punto_reorden = datosStock['punto_reorden'],
            pasillo = datosStock['pasillo'],
            columna = datosStock['columna'],
            contenedor = datosStock['contenedor'],
            user_stock = datosStock['user_stock'],
            img_inventario = datosStock['img_inventario'],
            maxima = datosStock['maxima'],
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_stock': stockNuevo.cantidad_actual}

    def listarstock(id_stock=None):
        if id_stock:
            try:
                queryset = Stock.objects.get(id_stock=id_stock)
            except Stock.DoesNotExist:
                return ({'result': 'No se encontró el stock deseado'})
            serializer = StockSerializer(queryset)
            return serializer.data
        else:
            queryset = Stock.objects.all()
            serializer = StockSerializer(queryset, many=True)
            return serializer.data