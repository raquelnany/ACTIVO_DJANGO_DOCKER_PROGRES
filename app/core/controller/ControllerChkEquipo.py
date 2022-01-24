from ..serializers import ChkEquipoSerializer
from ..models import Checklist_Equipo, Chk, Chk_Equipo


class ControllerChkEquipo:
    def crearchkequipo(request):
        datosChecklist = request.data
        try:
            chk = Chk.objects.get(id_chk = datosChecklist['chk'])
            checklist_equipo = Checklist_Equipo.objects.get(id_checklist_equipo =  datosChecklist['checklist_equipo'])

            checklistNuevo = Chk_Equipo.objects.create(
                chk = chk,
                checklist_equipo = checklist_equipo
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'chk_equipo': checklistNuevo.id_chk_equipo}
       
    def listarchecklistequipo(id_chk_equipo=None):
        if id_chk_equipo:
            try:
                queryset = Chk_Equipo.objects.get(id_chk_equipo=id_chk_equipo)
            except Chk_Equipo.DoesNotExist:
                return ({'result': 'No se encontró la checklist equipo deseada'})
            serializer = ChkEquipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Chk_Equipo.objects.all()
            serializer = ChkEquipoSerializer(queryset, many=True)
            return serializer.data
