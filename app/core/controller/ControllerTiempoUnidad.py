from ..serializers import TiempoUnidadSerializer
from ..models import Tiempo_Unidad


class ControllerTiempoUnidad:

    def creartiempounidad(request):
        datostimpounidad = request.data
        try:
            tiempoUnidadNuevo = Tiempo_Unidad.objects.create(
                unidad_es = datostimpounidad['unidad_es'],
                unidad_en = datostimpounidad['unidad_en']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'tiempo_unidad': tiempoUnidadNuevo.unidad_es}

    def listartiempounidad(id_tiempo_unidad=None):
        if id_tiempo_unidad:
            try:
                queryset = Tiempo_Unidad.objects.get(id_tiempo_unidad=id_tiempo_unidad)
            except Tiempo_Unidad.DoesNotExist:
                return ({'result': 'No se encontró el tiempo de unidad deseado'})
            serializer = TiempoUnidadSerializer(queryset)
            return serializer.data
        else:
            queryset = Tiempo_Unidad.objects.all()
            serializer = TiempoUnidadSerializer(queryset, many=True)
            return serializer.data