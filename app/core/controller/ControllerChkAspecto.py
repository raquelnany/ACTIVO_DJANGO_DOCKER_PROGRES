from ..serializers import ChkAspectoSerializer
from ..models import Checklist_Aspecto, Chk_Aspecto, Chk_Equipo


class ControllerChkAspecto:
    def crearchkaspecto(request):
        datosChecklist = request.data
        try:
            chk_equipo = Chk_Equipo.objects.get(id_chk_equipo = datosChecklist['chk_equipo'])
            checklist_aspecto = Checklist_Aspecto.objects.get(id_checklist_aspecto =  datosChecklist['checklist_aspecto'])

            checklistNuevo = Chk_Aspecto.objects.create(
                chk_equipo = chk_equipo,
                checklist_aspecto =  checklist_aspecto
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'chk_aspecto': checklistNuevo.id_chk_aspecto}
       
    def listarchecklistaspecto(id_chk_aspecto=None):
        if id_chk_aspecto:
            try:
                queryset = Chk_Aspecto.objects.get(id_chk_aspecto=id_chk_aspecto)
            except Chk_Aspecto.DoesNotExist:
                return ({'result': 'No se encontró la checklist equipo deseada'})
            serializer = ChkAspectoSerializer(queryset)
            return serializer.data
        else:
            queryset = Chk_Aspecto.objects.all()
            serializer = ChkAspectoSerializer(queryset, many=True)
            return serializer.data
