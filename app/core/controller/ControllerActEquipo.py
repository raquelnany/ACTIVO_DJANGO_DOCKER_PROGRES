from ..serializers import ActEquipoSerializer  
from ..models import Act_Equipo, Equipo


class ControllerActEquipo:
    def crearactequipo(request):
        datosActEquipo = request.data
        try:
            equipo = Equipo.objects.get(id_equipo = datosActEquipo['equipo'])

            actEquipoNuevo = Act_Equipo.objects.create(
                equipo = equipo, 
                descr_act = datosActEquipo['descr_act']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'act_equipo_nuevo': actEquipoNuevo.id_act_equipo }
       
    def listaractequipo(id_act_equipo=None):
        if id_act_equipo:
            try:
                queryset = Act_Equipo.objects.get(id_act_equipo = id_act_equipo)
            except Act_Equipo.DoesNotExist:
                return ({'result': 'No se encontró la act equipo deseada'})
            serializer = ActEquipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Act_Equipo.objects.all()
            serializer = ActEquipoSerializer(queryset, many=True)
            return serializer.data
