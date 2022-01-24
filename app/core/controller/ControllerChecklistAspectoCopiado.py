from ..serializers import ChecklistAspectoCopiadoSerializer 
from ..models import Checklist_Aspecto_Copiado, Equipo, Usuario


class ControllerChecklistAspectoCopiado:
    def crearchecklistaspectocopiado(request):
        datosChecklist = request.data
        try:
            equipo_base = Equipo.objects.get(id_equipo = datosChecklist['equipo_base'])
            equipo_copia = Equipo.objects.get(id_equipo = datosChecklist['equipo_copia'])
            usuario = Usuario.objects.get(id_usuario = datosChecklist['usuario'] )

            checklistNuevo = Checklist_Aspecto_Copiado.objects.create(
                equipo_base = equipo_base,
                equipo_copia = equipo_copia,
                usuario =  usuario, 
                fecha =datosChecklist['fecha'],
                hora = datosChecklist['hora'],
                notas = datosChecklist['notas']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'checklist_aspecto_copiado': checklistNuevo.checklist_aspecto}
       
    def listarchecklistaspectocopiado(id_checklist_aspecto_copiado=None):
        if id_checklist_aspecto_copiado:
            try:
                queryset = Checklist_Aspecto_Copiado.objects.get(id_checklist_aspecto_copiado=id_checklist_aspecto_copiado)
            except Checklist_Aspecto_Copiado.DoesNotExist:
                return ({'result': 'No se encontró la checklist aspecto copiado deseado'})
            serializer = ChecklistAspectoCopiadoSerializer(queryset)
            return serializer.data
        else:
            queryset = Checklist_Aspecto_Copiado.objects.all()
            serializer = ChecklistAspectoCopiadoSerializer(queryset, many=True)
            return serializer.data
