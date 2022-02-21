from ..serializers import ProbEquipoSerializer  
from ..models import Equipo, Prob_Equipo


class ControllerProbEquipo:
    def crearprobequipo(request):
        datosProbEquipo = request.data
        try:
            equipo = Equipo.objects.get(id_equipo=datosProbEquipo['equipo'])

            probEquipoNuevo = Prob_Equipo.objects.create(
                equipo = equipo, 
                codigo_prob_equipo = datosProbEquipo['codigo_prob_equipo'],
                descripcion_prob_equipo = datosProbEquipo['descripcion_prob_equipo']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_prob_equipo': probEquipoNuevo.codigo_prob_equipo}
       
    def listarprobequipo(id_prob_equipo=None):
        if id_prob_equipo:
            try:
                queryset = Prob_Equipo.objects.get(id_prob_equipo=id_prob_equipo)
            except Prob_Equipo.DoesNotExist:
                return ({'result': 'No se encontró la prob equipo deseada'})
            serializer = ProbEquipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Prob_Equipo.objects.all()
            serializer = ProbEquipoSerializer(queryset, many=True)
            return serializer.data
