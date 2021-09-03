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

    def modificarjornada(request,id_jornada=None):
        if id_jornada:
            datosJornada = request.data
            try:
                JornadaModificar = Jornada.objects.get(id_jornada=id_jornada)
            except Jornada.DoesNotExist:
                return ({'result': 'No se encontró jornada deseada'})
            try: 
              
                JornadaModificar.anio = datosJornada['anio']
                JornadaModificar.mes =  datosJornada['mes']
                JornadaModificar.horaInicio =  datosJornada['horaInicio']
                JornadaModificar.horaFinal = datosJornada['horaFinal']
              
            except Exception:
                return {"estatus":"Error"}

            return {"estatus":"Ok", 'jornada_modificado': JornadaModificar.mes}
        else: 
            return {"result":"Ingrese el Id de la jornada a modificar"}

    
