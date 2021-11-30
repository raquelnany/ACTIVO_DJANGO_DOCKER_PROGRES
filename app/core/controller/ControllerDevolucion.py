from ..serializers import DevolucionSerializer
from ..models import Devolucion, Inventario_Vale


class ControllerDevolucion:

    def creardevolucion(request):
        datosDevolucion = request.data
        try:
            inventario_vale = Inventario_Vale.objects.get(id_inventario_vale = datosDevolucion['inventario_vale'])

            devolucionNueva = Devolucion.objects.create(   
                id_devuelto_por  = datosDevolucion['id_devuelto_por'],
                id_orden_trabajo_parte = datosDevolucion['id_orden_trabajo_parte'],
                inventario_vale = inventario_vale,
                fecha_devuelto = datosDevolucion['fecha_devuelto'],
                hora_devuelto  = datosDevolucion['hora_devuelto'],
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'devolucion': devolucionNueva.id_orden_trabajo_parte}

    def listardevolcion(id_devolucion=None):
        if id_devolucion:
            try:
                queryset = Devolucion.objects.get(id_devolucion=id_devolucion)
            except Devolucion.DoesNotExist:
                return ({'result': 'No se encontró la devolución deseadas'})
            serializer = DevolucionSerializer(queryset)
            return serializer.data
        else:
            queryset = Devolucion.objects.all()
            serializer = DevolucionSerializer(queryset, many=True)
            return serializer.data