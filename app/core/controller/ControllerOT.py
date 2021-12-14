from ..serializers import OTSerializer
from ..models import OT, Equipo, Orden_Subestatus, Orden_Trabajo_Estatus, Orden_Trabajo_Prioridad, Usuario

class ControllerOT:
    def crearot(request):
        datosOT = request.data
        try:
                   
            equipo_ot = Equipo.objects.get(id_equipo=datosOT['id_visible_ot'])
            id_requisitor_ot = Usuario.objects.get(id_usuario=datosOT['id_requisitor_ot'])
            prioridad_ot = Orden_Trabajo_Prioridad.objects.get(id_orden_trabajo_prioridad=datosOT['prioridad_ot'])
            estatus_ot = Orden_Trabajo_Estatus.objects.get(id_orden_trabajo_estatus=datosOT['estatus_ot'])
            subestatus_ot = Orden_Subestatus.objects.get(id_orden_subestatus=datosOT['subestatus_ot'])
            responsable_ot = Usuario.objects.get(id_usuario=datosOT['responsable_ot'])
            tecnico_asignado = Usuario.objects.get(id_usuario=datosOT['tecnico_asignado'])

            oTNuevo = OT.objects.create(
                id_visible_ot = datosOT['id_visible_ot'],
                descipcion_ot =  datosOT['descipcion_ot'],
                equipo_ot = equipo_ot,
                id_requisitor_ot =id_requisitor_ot,
                id_cuenta = datosOT['id_cuenta'],
                id_problema = datosOT['id_problema'],
                id_causa = datosOT['id_causa'],
                id_actividad = datosOT['id_actividad'],
                caido_ot = datosOT['caido_ot'],
                prioridad_ot = prioridad_ot,
                tipo_de_trabajo_ot = datosOT['tipo_de_trabajo_ot'],
                estatus_ot = estatus_ot,
                subestatus_ot = subestatus_ot,
                responsable_ot = responsable_ot,
                fecha_inicio_ot = datosOT['fecha_inicio_ot'],
                fecha_estimada = datosOT['fecha_estimada'],
                fecha_fin_ot = datosOT['fecha_fin_ot'],
                tecnico_asignado = tecnico_asignado,
                instr_trab_ot = datosOT['instr_trab_ot'],
                notas_ot = datosOT['notas_ot'],
                trab_estimados = datosOT['trab_estimados']
            )
                
        except Exception:
            return {"estatus":"Error"}

        return {"estatus":"Ok", 'ot_nueva': oTNuevo.id_visible_ot}
       
    def listarot(id_ot=None):
        if id_ot:
            try:
                queryset = OT.objects.get(id_ot=id_ot)
            except OT.DoesNotExist:
                return ({'result': 'No se encontró la OT deseada'})
            serializer = OTSerializer(queryset)
            return serializer.data
        else:
            queryset = OT.objects.all()
            serializer = OTSerializer(queryset, many=True)
            return serializer.data