from ..serializers import RequisicionEstatusSerializer
from ..models import Requisicion_Estatus


class ControllerRequisicionEstatus:
    def crearrequisicionestatus(request):
        datosRequisicionEstatus = request.data
        try:
           requisicionEstatusNuevo = Requisicion_Estatus.objects.create(
                requisicion_estatus_es = datosRequisicionEstatus['requisicion_estatus_es'],
                requisicion_estatus_en = datosRequisicionEstatus['requisicion_estatus_en']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_requisicion_estatus': requisicionEstatusNuevo.requisicion_estatus_es}
       
    def listarrequisicionestatus(id_requisicion_estatus=None):
        if id_requisicion_estatus:
            try:
                queryset = Requisicion_Estatus.objects.get(id_requisicion_estatus=id_requisicion_estatus)
            except Requisicion_Estatus.DoesNotExist:
                return ({'result': 'No se encontró el estatus de requisicion deseado'})
            serializer = RequisicionEstatusSerializer(queryset)
            return serializer.data
        else:
            queryset = Requisicion_Estatus.objects.all()
            serializer = RequisicionEstatusSerializer(queryset, many=True)
            return serializer.data
