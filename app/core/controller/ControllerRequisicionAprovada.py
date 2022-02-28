from ..serializers import RequisiconAprovadaSerializer  
from ..models import Requisicion, Requisicion_Aprovada


class ControllerRequisicionAprovada:
    def crearrequisicionaprovada(request):
        datosRequisiconAprovada = request.data
        try:
            requisicion = Requisicion.objects.get(id_requiscion = datosRequisiconAprovada['requisicion'])

            requisicionAprovadaNuevo = Requisicion_Aprovada.objects.create(
                requisicion = requisicion,
                id_aprovacion_1 = datosRequisiconAprovada['id_aprovacion_1'],
                id_aprovacion_2 = datosRequisiconAprovada['id_aprovacion_2'],
                id_aprovacion_3 = datosRequisiconAprovada['id_aprovacion_3']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'requisicion_aprovada_nueva': requisicionAprovadaNuevo.id_requisicion_aprovada }
       
    def listarrequisicionaprovada(id_requisicion_aprovada=None):
        if id_requisicion_aprovada:
            try:
                queryset = Requisicion_Aprovada.objects.get(id_requisicion_aprovada = id_requisicion_aprovada)
            except Requisicion_Aprovada.DoesNotExist:
                return ({'result': 'No se encontró la requisicion aprovada deseada'})
            serializer = RequisiconAprovadaSerializer(queryset)
            return serializer.data
        else:
            queryset = Requisicion_Aprovada.objects.all()
            serializer = RequisiconAprovadaSerializer(queryset, many=True)
            return serializer.data
