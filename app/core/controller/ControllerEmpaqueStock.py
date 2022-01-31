from ..serializers import EmpaqueStockSerializer
from ..models import Empaque_Stock, Instalacion, Empaque, Usuario


class ControllerEmpaqueStock:
    def crearempaquestock(request):
        datosEmpaque = request.data
        try:
            instalacion = Instalacion.objects.get(id_instalacion = datosEmpaque['instalacion'])
            empaque = Empaque.objects.get(id_empaque = datosEmpaque['empaque'])
            user_stock = Usuario.objects.get(id_usuario = datosEmpaque['user_stock'])

            empaqueNuevo = Empaque_Stock.objects.create(
                instalacion = instalacion,
                empaque = empaque,
                cantidad_actual = datosEmpaque['cantidad_actual'],
                punto_reorden = datosEmpaque['punto_reorden'],
                pasillo =  datosEmpaque['pasillo'],
                columna = datosEmpaque['columna'],
                contenedor = datosEmpaque['contenedor'],
                user_stock = user_stock,
                img_empaque = datosEmpaque['img_empaque'],
                maxima = datosEmpaque['maxima']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque_stock': empaqueNuevo.id_empaque_stock}
       
    def listarempaquestock(id_empaque_stock = None):
        if id_empaque_stock:
            try:
                queryset = Empaque_Stock.objects.get(id_empaque_stock = id_empaque_stock)
            except Empaque_Stock.DoesNotExist:
                return ({'result': 'No se encontró el empaque stock deseado'})
            serializer = EmpaqueStockSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque_Stock.objects.all()
            serializer = EmpaqueStockSerializer(queryset, many=True)
            return serializer.data
