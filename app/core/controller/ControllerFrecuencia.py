from ..serializers import FrecuenciaSerializer
from ..models import Frecuencia


class ControllerFrecuencia:

    def crearfrecuencia(request):
        datosFrecuencia = request.data
        try:
            frecuenciaNueva = Frecuencia.objects.create(
                frecuencia_es = datosFrecuencia['frecuencia_es'],
                frecuencia_en = datosFrecuencia['frecuencia_en'],
                tiempo_es = datosFrecuencia['tiempo_es'],
                tiempo_en = datosFrecuencia['tiempo_en'],

           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'frecuencia': frecuenciaNueva.frecuencia_es}

    def listafrecuencia(id_frecuencia=None):
        if id_frecuencia:
            try:
                queryset = Frecuencia.objects.get(id_frecuencia=id_frecuencia)
            except Frecuencia.DoesNotExist:
                return ({'result': 'No se encontró la frecuencia deseada'})
            serializer = FrecuenciaSerializer(queryset)
            return serializer.data
        else:
            queryset = Frecuencia.objects.all()
            serializer = FrecuenciaSerializer(queryset, many=True)
            return serializer.data