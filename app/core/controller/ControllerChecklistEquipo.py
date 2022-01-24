from ..serializers import ChecklistEquipoSerializer 
from ..models import Checklist, Checklist_Equipo, Equipo, Equipo_Estatus


class ControllerChecklistEquipo:
    def crearchecklistequipo(request):
        datosChecklist = request.data
        try:
            checklist = Checklist.objects.get(id_checklist = datosChecklist['checklist'])
            equipo = Equipo.objects.get(id_equipo = datosChecklist['equipo'])
            estatus_equipo = Equipo_Estatus.objects.get(id_equipo_estatus = datosChecklist['estatus_equipo'])

            checklistNuevo = Checklist.objects.create(
                checklist = checklist,
                equipo = equipo, 
                estatus_equipo = estatus_equipo
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'checklist_equipo': checklistNuevo.id_checklist_equipo}
       
    def listarchecklistequipo(id_checklist_equipo=None):
        if id_checklist_equipo:
            try:
                queryset = Checklist_Equipo.objects.get(id_checklist_equipo=id_checklist_equipo)
            except Checklist_Equipo.DoesNotExist:
                return ({'result': 'No se encontró la checklist equipo deseada'})
            serializer = ChecklistEquipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Checklist_Equipo.objects.all()
            serializer = ChecklistEquipoSerializer(queryset, many=True)
            return serializer.data
