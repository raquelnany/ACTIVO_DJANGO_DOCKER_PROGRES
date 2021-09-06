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
                hora=datosJornadaHoras['hora'],)

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

    def modificarjornadahoras(request,id_jornada_horas=None):
        if id_jornada_horas:
            datosJornadaHoras = request.data
            try:
                jornadahorasmodificar = JornadaHoras.objects.get(id_jornada_horas=id_jornada_horas)
            except JornadaHoras.DoesNotExist:
                return ({'result': 'No se encontró la jornada horas deseada'})
            try:
                
                jornada = Jornada.objects.get(id_jornada=datosJornadaHoras['jornada'])
                usuario = Usuario.objects.get(id_usuario=datosJornadaHoras['usuario'])
                
                jornadahorasmodificar.jornada=jornada
                jornadahorasmodificar.usuario=usuario
                jornadahorasmodificar.dia=datosJornadaHoras['dia']
                jornadahorasmodificar.hora=datosJornadaHoras['hora']             
                
                jornadahorasmodificar.save()
                
            except Exception:
                return {"estatus":"Error"}
            return {"estatus":"Ok", 'Jjornada_horas_modificada': jornadahorasmodificar.id_jornada_horas}
        else: 
            return {"result":"Ingrese el Id de la jornada horas que desea modificar"}