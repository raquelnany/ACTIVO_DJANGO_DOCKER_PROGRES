from ..serializers import ChecklistInstruccionSerializer
from ..models import Checklist_Aspecto, Checklist_Instruccion


class ControllerChecklistInstruccion:
    def crearchecklistInstruccion(request):
        datosChecklist = request.data
        try:
            checklist_aspecto = Checklist_Aspecto.objects.get(id_checklist_aspecto = datosChecklist['checklist_aspecto'] )

            checklistNuevo = Checklist_Instruccion.objects.create(
                checklist_instruccion = datosChecklist['checklist_instruccion'],
                checklist_aspecto =  checklist_aspecto
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'checklist_instruccion': checklistNuevo.checklist_instruccion}
       
    def listarchecklistinstruccion(id_checklist_instruccion=None):
        if id_checklist_instruccion:
            try:
                queryset = Checklist_Instruccion.objects.get(id_checklist_instruccion=id_checklist_instruccion)
            except Checklist_Instruccion.DoesNotExist:
                return ({'result': 'No se encontró la checklist instruccion deseada'})
            serializer = ChecklistInstruccionSerializer(queryset)
            return serializer.data
        else:
            queryset = Checklist_Instruccion.objects.all()
            serializer = ChecklistInstruccionSerializer(queryset, many=True)
            return serializer.data
