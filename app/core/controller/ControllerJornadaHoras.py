from ..serializers import JornadaHorasSerializer
from ..models import JornadaHoras, Jornada, Usuario

class ControllerJornadaHoras:
    def crearjornadahoras(request):
        datosJornadaHoras = request.data
        try:
            jornada = Jornada.objects.get(id_jornada=datosJornadaHoras['jornada'])
            usuario = Usuario.objects.get(id_usuario=datosJornadaHoras['usuario'])
            jornadaHorasNuevo= JornadaHoras.objects.create(
                jornada=jornada,
                usuario=usuario,
                dia=datosJornadaHoras['dia'],
                horas=datosJornadaHoras['horas'],
               
            )

        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_jornadahoras': jornadaHorasNuevo.dia}

    def listarjornadahoras(id_jornada_horas=None):
        if id_jornada_horas:
            try:
                queryset = JornadaHoras.objects.get(id_jornada_horas=id_jornada_horas)
            except JornadaHoras.DoesNotExist:
                return ({'result': 'No se encontró jornada horas deseada'})
            serializer = JornadaHorasSerializer(queryset)
            return serializer.data
        else:
            queryset =JornadaHoras.objects.all()
            serializer = JornadaHorasSerializer(queryset, many=True)
            return serializer.data