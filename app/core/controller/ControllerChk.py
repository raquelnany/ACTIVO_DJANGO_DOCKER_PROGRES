from ..serializers import ChkSerializer
from ..models import Chk, Checklist, EstatusUsuario, Instalacion, Orden_Trabajo_Tipo, Tipo_Programa, Usuario


class ControllerChk:
    def crearchk(request):
        datosChecklist = request.data
        try:
            checklist = Checklist.objects.get(id_checklist = datosChecklist['checklist'])
            chk_estatus = EstatusUsuario.objects.get(id_estatus = datosChecklist['chk_estatus'])
            chk_modificado_por = Usuario.objects.get(id_usuario = datosChecklist['usuario'])
            instalacion = Instalacion.objects.get(id_instalacion = datosChecklist['instalacion'])
            tipo_ot = Orden_Trabajo_Tipo.objects.get(id_orden_trabajo_tipo = datosChecklist['tipo_ot'])
            tipo_programa = Tipo_Programa.objects.get(id_tipo_programa = datosChecklist['tipo_programa'])

            checklistNuevo = Chk.objects.create(
                checklist = checklist,
                chk_codigo = datosChecklist['chk_codigo'],
                checklist = datosChecklist['checklist'],
                chk_fecha_creacion = datosChecklist['chk_fecha_creacion'],
                chk_hora_creacion = datosChecklist['chk_hora_creacion'],
                chk_estatus = chk_estatus,
                chk_fecha_modificado = datosChecklist['chk_fecha_modificado'],
                chk_hora_modificado = datosChecklist['chk_hora_modificado'],
                chk_modificado_por = chk_modificado_por,
                id_asignado = datosChecklist['id_asignado'],
                instalacion = instalacion,
                tipo_ot = tipo_ot,
                tipo_programa = tipo_programa,
                num_trabajadores = datosChecklist['num_trabajadores'],
                realizar_activo = datosChecklist['realizar_activo'],
                tiempo_estimado = datosChecklist['tiempo_estimado']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'Chk': checklistNuevo.chk_codigo}
       
    def listarchecklistchk(id_chk=None):
        if id_chk:
            try:
                queryset = Chk.objects.get(id_chk=id_chk)
            except Chk.DoesNotExist:
                return ({'result': 'No se encontró el chk deseado'})
            serializer = ChkSerializer(queryset)
            return serializer.data
        else:
            queryset = Chk.objects.all()
            serializer = ChkSerializer(queryset, many=True)
            return serializer.data
