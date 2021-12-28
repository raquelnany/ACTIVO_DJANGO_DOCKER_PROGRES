from ..serializers import M4Serializer
from ..models import M4


class ControllerM4:

    def crearm4(request):
        datosm4 = request.data
        try:
            m4Nuevo = M4.objects.create(
                es_4m = datosm4['es_4m'],
                en_4m = datosm4['en_4m'],
   
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", '4M': m4Nuevo.es_4m}

    def listarm4(id_4m=None):
        if id_4m:
            try:
                queryset = M4.objects.get(id_4m=id_4m)
            except M4.DoesNotExist:
                return ({'result': 'No se encontró el 4M de equipo deseado'})
            serializer = M4Serializer(queryset)
            return serializer.data
        else:
            queryset = M4.objects.all()
            serializer = M4Serializer(queryset, many=True)
            return serializer.data