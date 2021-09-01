from ..serializers import JornadaSerializer
from ..models import Jornada

class ControllerJornada:
    serializer_class = JornadaSerializer
        
    def crearjornada(request):
        datosJornada = request.data
        JornadaNuevo = Jornada()
        
        try:
            JornadaNuevo.anio = datosJornada['anio']
            JornadaNuevo.mes =  datosJornada['mes']
            JornadaNuevo.horaInicio =  datosJornada['horaInicio']
            JornadaNuevo.horaFinal = datosJornada['horaFinal']
        except Exception:
             return {"estatus":"Error"}
        
        JornadaNuevo.save()
        return {"estatus":"Ok", 'nuevo_jornada': JornadaNuevo.anio}

    def listarjornada(id_jornada=None):
        if id_jornada:
            try:
                queryset = Jornada.objects.get(id_jornada=id_jornada)
            except Jornada.DoesNotExist:
                return ({'result': 'No se encontró jornada deada'})
            serializer = JornadaSerializer(queryset)
            return serializer.data
        else:
            queryset =Jornada.objects.all()
            serializer = JornadaSerializer(queryset, many=True)
            return serializer.data

    
