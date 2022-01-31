from ..serializers import EmpaqueStockSalidaSerializer
from ..models import Empaque_Stock_Salida, Instalacion, Usuario, Empaque


class ControllerEmpaqueStockSalida:
    def crearempaquestock(request):
        datosEmpaque = request.data
        try:
            instalacion = Instalacion.objects.get(id_instalacion = datosEmpaque['instalacion'])
            empaque = Empaque.objects.get(id_empaque = datosEmpaque['empaque'])
            user_salida = Usuario.objects.get(id_usuario = datosEmpaque['user_stock'])

            empaqueNuevo = Empaque_Stock_Salida.objects.create(
                empaque = empaque,
                instalacion = instalacion,
                fecha_salida = datosEmpaque['fecha_salida'],
                notas =  datosEmpaque['notas'],
                cantidad_salida = datosEmpaque['cantidad_salida'],
                precio_unitario = datosEmpaque['precio_unitario'],
                user_salida = user_salida
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque_stock_salida': empaqueNuevo.id_empaque_stock_salida}
       
    def listarempaquestock(id_empaque_stock_salida = None):
        if id_empaque_stock_salida:
            try:
                queryset = Empaque_Stock_Salida.objects.get(id_empaque_stock_salida = id_empaque_stock_salida)
            except Empaque_Stock_Salida.DoesNotExist:
                return ({'result': 'No se encontró el empaque stock salida deseado'})
            serializer = EmpaqueStockSalidaSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque_Stock_Salida.objects.all()
            serializer = EmpaqueStockSalidaSerializer(queryset, many=True)
            return serializer.data
