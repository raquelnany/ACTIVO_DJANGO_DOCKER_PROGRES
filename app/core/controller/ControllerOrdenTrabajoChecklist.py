from ..serializers import OrdenTrabajoChecklistSerializer
from ..models import OT, Chk, Orden_Trabajo_Checklist, Usuario


class ControllerOrdenTrabajoChecklist:
    def crearordentrabajochecklist(request):
        datosChecklist = request.data
        try:
            ot = OT.objects.get(id_ot = datosChecklist['ot'])
            chk = Chk.objects.get(id_chk = datosChecklist['chk'])
            usuario = Usuario.objects.get(id_usaurio = datosChecklist['usuario'])

            checklistNuevo = Orden_Trabajo_Checklist.objects.create(
                ot = ot,
                chk = chk,
                fecha = datosChecklist['fecha'],
                usuario = usuario
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'orden_trabajo_checklist': checklistNuevo.chk_instruccion}
       
    def listarcheckinstruccion(id_orden_trabajo_checklist=None):
        if id_orden_trabajo_checklist:
            try:
                queryset = Orden_Trabajo_Checklist.objects.get(id_orden_trabajo_checklist=id_orden_trabajo_checklist)
            except Orden_Trabajo_Checklist.DoesNotExist:
                return ({'result': 'No se encontró la instruccion chk deseada'})
            serializer = OrdenTrabajoChecklistSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Trabajo_Checklist.objects.all()
            serializer = OrdenTrabajoChecklistSerializer(queryset, many=True)
            return serializer.data
