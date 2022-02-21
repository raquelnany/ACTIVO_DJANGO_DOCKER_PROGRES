from ..serializers import CriticidadSerializer
from ..models import Criticidad


class ControllerCriticidad:
    def crearcriticidad(request):
        datosCriticidad = request.data
        try:
            criticidadNuevo = Criticidad.objects.create(
                criticidad_es = datosCriticidad['criticidad_es'],
                criticidad_en  =datosCriticidad['criticidad_en']     
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_criticidad': criticidadNuevo.criticidad_es}
       
    def listarcriticidad(id_criticidad=None):
        if id_criticidad:
            try:
                queryset = Criticidad.objects.get(id_criticidad=id_criticidad)
            except Criticidad.DoesNotExist:
                return ({'result': 'No se encontró la criticidad deseada'})
            serializer = CriticidadSerializer(queryset)
            return serializer.data
        else:
            queryset = Criticidad.objects.all()
            serializer = CriticidadSerializer(queryset, many=True)
            return serializer.data
