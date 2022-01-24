from ..serializers import ChecklistSerializer  
from ..models import Checklist, EstatusUsuario, Frecuencia, Instalacion, Orden_Trabajo_Tipo, Tipo_Programa, Usuario


class ControllerChecklist:
    def crearchecklist(request):
        datosChecklist = request.data
        try:
            user_creador = Usuario.objects.get(id_usuario = datosChecklist['user_creador'])
            user_modificador = Usuario.objects.get(id_usuario = datosChecklist['user_modificador'])
            checklist_estatus = EstatusUsuario.objects.get(id_estatus = datosChecklist['checklist_estatus'])
            frecuencia = Frecuencia.objects.get(id_frecuencia = datosChecklist['frecuencia'])
            instalacion = Instalacion.objects.get(id_instalacion = datosChecklist['instalacion'])
            tipo_ot = Orden_Trabajo_Tipo.objects.get(id_orden_trabajo_tipo = datosChecklist['tipo_ot'])
            tipo_programa = Tipo_Programa.objects.get(id_tipo_programa =  datosChecklist['tipo_programa'])

            checklistNuevo = Checklist.objects.create(
                user_creador =  user_creador,
                user_modificador = user_modificador,
                checklist_estatus = checklist_estatus,
                frecuencia = frecuencia,
                id_asignado = datosChecklist['id_asignado'],
                instalacion =  instalacion,
                checklist = datosChecklist['checklist'],
                checklist_codigo = datosChecklist['checklist_codigo'],
                checklist_creacion = datosChecklist['checklist_creacion'],
                checklist_cada = datosChecklist['checklist_cada'],
                checklist_modificado = datosChecklist['checklist_modificado'],
                tipo_ot =  tipo_ot,
                tipo_programa = tipo_programa,
                checklist_alcance = datosChecklist['checklist_alcance'],
                checklist_trabajadores = datosChecklist['checklist_trabajadores'],
                checklist_realizar_activo = datosChecklist['checklist_realizar_activo'],
                tiempo_estimado = datosChecklist['tiempo_estimado']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'checklist': checklistNuevo.id_asignado}
       
    def listarchecklist(id_checklist=None):
        if id_checklist:
            try:
                queryset = Checklist.objects.get(id_checklist=id_checklist)
            except Checklist.DoesNotExist:
                return ({'result': 'No se encontró la checklist deseada'})
            serializer = ChecklistSerializer(queryset)
            return serializer.data
        else:
            queryset = Checklist.objects.all()
            serializer = ChecklistSerializer(queryset, many=True)
            return serializer.data
