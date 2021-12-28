from ..serializers import TareaInstruccionSerializer
from ..models import Instruccion, Tarea_Instruccion, Tarea_Orden_Trabajo, Usuario


class ControllerTareaInstruccion:

    def creartareainstruccion(request):
        datosTareaInstruccion = request.data
        try:
            tarea = Tarea_Orden_Trabajo.objects.get(id_tarea_orden_trabajo = datosTareaInstruccion['tarea'])
            instruccion = Instruccion.objects.get(id_instruccion = datosTareaInstruccion['instruccion'])
            user = Usuario.objects.get(id_usuario = datosTareaInstruccion['user'])

            tareaInstruccionNueva = Tarea_Instruccion.objects.create(
                    tarea =  tarea,
                    instruccion =  instruccion,
                    fecha = datosTareaInstruccion['fecha'],
                    hora = datosTareaInstruccion['hora'],
                    user =  user,
                    posicion = datosTareaInstruccion['posicion']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'tarea_instruccion': tareaInstruccionNueva.tarea}

    def listartareainstruccion(id_tarea_instruccion=None):
        if id_tarea_instruccion:
            try:
                queryset = Tarea_Instruccion.objects.get(id_tarea_instruccion=id_tarea_instruccion)
            except Tarea_Instruccion.DoesNotExist:
                return ({'result': 'No se encontró la tarea instruccion deseada'})
            serializer = TareaInstruccionSerializer(queryset)
            return serializer.data
        else:
            queryset = Tarea_Instruccion.objects.all()
            serializer = TareaInstruccionSerializer(queryset, many=True)
            return serializer.data