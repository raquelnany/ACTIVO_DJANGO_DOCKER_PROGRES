from ..serializers import EquipoTareaParteSerializer
from ..models import Equipo, Equipo_Tarea, Equipo_Tarea_Parte, Instalacion, Orden_Trabajo_Parte, Tarea_Orden_Trabajo, Usuario

class ControllerEquipoTareaParte:

    def crearequipotareaparte(request):
        datosEquipoTarea = request.data
        try:
            parte = Orden_Trabajo_Parte.objects.get(id_orden_trabajo_parte = datosEquipoTarea['parte'])
            tarea = Tarea_Orden_Trabajo.objects.get(id_tarea_orden_trabajo = datosEquipoTarea['tarea'])
            equipo = Equipo.objects.get(id_equipo = datosEquipoTarea['equipo'])
            usuario = Usuario.objects.get(id_usuario = datosEquipoTarea['usuario'])
            instalacion = Instalacion.objects.get(id_instalacion = datosEquipoTarea['instalacion'])

            equipoTareaNuevo = Equipo_Tarea_Parte.objects.create(
                parte =  parte, 
                cantidad_solicitada =  datosEquipoTarea['cantidad_solicitada'],
                tarea = tarea,
                equipo = equipo,
                user =  usuario,
                instalacion =  instalacion, 
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'equipo_tarea': equipoTareaNuevo.parte}

    def listarequipotareaparte(id_equipo_tarea_parte=None):
        if id_equipo_tarea_parte:
            try:
                queryset = Equipo_Tarea_Parte.objects.get(id_equipo_tarea_parte=id_equipo_tarea_parte)
            except Equipo_Tarea_Parte.DoesNotExist:
                return ({'result': 'No se encontró la tarea del equipo deseado'})
            serializer = EquipoTareaParteSerializer(queryset)
            return serializer.data
        else:
            queryset = Equipo_Tarea_Parte.objects.all()
            serializer = EquipoTareaParteSerializer(queryset, many=True)
            return serializer.data