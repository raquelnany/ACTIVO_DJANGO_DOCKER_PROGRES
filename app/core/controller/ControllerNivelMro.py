from ..serializers import NivelMroSerializer
from ..models import Nivel_Mro


class ControllerNivelMro:
    def crearnivelmro(request):
        datos = request.data
        try:
            nivelMroNuevo = Nivel_Mro.objects.create(
                nivel_es = datos['nivel_es'],
                nivel_en  = datos['nivel_en']        
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_nivel_mro': nivelMroNuevo.nivel_es}
       
    def listarnivelmro(id_nivel_mro=None):
        if id_nivel_mro:
            try:
                queryset = Nivel_Mro.objects.get(id_nivel_mro=id_nivel_mro)
            except Nivel_Mro.DoesNotExist:
                return ({'result': 'No se encontró el nivel mro deseado'})
            serializer = NivelMroSerializer(queryset)
            return serializer.data
        else:
            queryset = Nivel_Mro.objects.all()
            serializer = NivelMroSerializer(queryset, many=True)
            return serializer.data
