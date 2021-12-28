from ..serializers import EquipoTareaSerializer
from ..models import Act_Ot_Tipo, Equipo, Equipo_Tarea, EstatusUsuario, Frecuencia, Instalacion, Orden_Trabajo_Parte, Tarea_Orden_Trabajo, Tipo_Programa, Usuario

class ControllerEquipoTarea:

    def crearequipotarea(request):
        datosEquipoTarea = request.data
        try:
            equipo = Equipo.objects.get(id_equipo = datosEquipoTarea['equipo'])
            tipo = Act_Ot_Tipo.objects.get(id_act_ot_tipo = datosEquipoTarea['tipo'])
            tipo_programa = Tipo_Programa.objects.get(id_tipo_programa = datosEquipoTarea['tipo_programa'])
            frecuencia = Frecuencia.objects.get(id_frecuencia = datosEquipoTarea['frecuencia'])
            estatus = EstatusUsuario.objects.get(id_estatus = datosEquipoTarea['estatus'])
            user = Usuario.objects.get(id_usuario = datosEquipoTarea['user'])
            usuario = Usuario.objects.get(id_usuario = datosEquipoTarea['usuario'])

            equipoTareaNuevo = Equipo_Tarea.objects.create(
                tarea = datosEquipoTarea['tarea'],
                equipo = equipo,
                tipo = tipo,
                descripcion = datosEquipoTarea['descripcion'],
                realizar_activa = datosEquipoTarea['realizar_activa'],
                tipo_programa = tipo_programa,
                fecha_creacion = datosEquipoTarea['fecha_creacion'],
                frecuencia = frecuencia, 
                estatus = estatus,
                cada = datosEquipoTarea['cada'],
                user = user,
                ultima_fecha = datosEquipoTarea['ultima_fecha'],
                numero_trabajadores = datosEquipoTarea['numero_trabajadores'],
                usuario = usuario
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'equipo_tarea': equipoTareaNuevo.tarea}

    def listarequipotarea(id_equipo_tarea=None):
        if id_equipo_tarea:
            try:
                queryset = Equipo_Tarea.objects.get(id_equipo_tarea=id_equipo_tarea)
            except Equipo_Tarea.DoesNotExist:
                return ({'result': 'No se encontró la tarea del equipo deseado'})
            serializer = EquipoTareaSerializer(queryset)
            return serializer.data
        else:
            queryset = Equipo_Tarea.objects.all()
            serializer = EquipoTareaSerializer(queryset, many=True)
            return serializer.data