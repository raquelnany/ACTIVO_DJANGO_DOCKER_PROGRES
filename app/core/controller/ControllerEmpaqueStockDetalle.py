from ..serializers import EmpaqueStockDetalleSerializer
from ..models import CentroCosto, Empaque, Empaque_Stock_Detalle, Unidad


class ControllerEmpaqueStockDetalle:
    def crearempaquestockdetalle(request):
        datosEmpaque = request.data
        try:
            empaque = Empaque.objects.get(id_empaque = datosEmpaque['empaque'])
            centro_costo = CentroCosto.objects.get(id_centro_costo = datosEmpaque['centro_costo'])
            unidad = Unidad.objects.get(id_unidad = datosEmpaque['unidad'])

            empaqueNuevo = Empaque_Stock_Detalle.objects.create(
                empaque = empaque,
                cuenta =  datosEmpaque['cuenta'],
                centro_costo = centro_costo,
                modelo = datosEmpaque['modelo'],
                numero_serie = datosEmpaque['numero_serie'],
                notas_detalles = datosEmpaque['notas_detalles'],
                unidad = unidad
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque_stock_detalle': empaqueNuevo.id_empaque_stock_detalle}
       
    def listarempaquestock(id_empaque_stock_detalle = None):
        if id_empaque_stock_detalle:
            try:
                queryset = Empaque_Stock_Detalle.objects.get(id_empaque_stock_detalle = id_empaque_stock_detalle)
            except Empaque_Stock_Detalle.DoesNotExist:
                return ({'result': 'No se encontró el empaque stock detalle deseado'})
            serializer = EmpaqueStockDetalleSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque_Stock_Detalle.objects.all()
            serializer = EmpaqueStockDetalleSerializer(queryset, many=True)
            return serializer.data
