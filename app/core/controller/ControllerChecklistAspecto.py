from ..serializers import ChecklistAspectoSerializer 
from ..models import Checklist_Aspecto, Checklist_Equipo


class ControllerChecklistAspecto:
    def crearchecklistaspecto(request):
        datosChecklist = request.data
        try:
            checklist_equipo = Checklist_Equipo.objects.get(id_checklist_equipo = datosChecklist['checklist_equipo'] )

            checklistNuevo = Checklist_Aspecto.objects.create(
                checklist_aspecto = datosChecklist['checklist_aspecto'],
                checklist_equipo =  checklist_equipo
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'checklist_aspecto': checklistNuevo.checklist_aspecto}
       
    def listarchecklistaspecto(id_checklist_aspecto=None):
        if id_checklist_aspecto:
            try:
                queryset = Checklist_Aspecto.objects.get(id_checklist_aspecto=id_checklist_aspecto)
            except Checklist_Aspecto.DoesNotExist:
                return ({'result': 'No se encontró la checklist aspecto deseada'})
            serializer = ChecklistAspectoSerializer(queryset)
            return serializer.data
        else:
            queryset = Checklist_Aspecto.objects.all()
            serializer = ChecklistAspectoSerializer(queryset, many=True)
            return serializer.data
