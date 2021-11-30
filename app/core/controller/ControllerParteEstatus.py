from ..serializers import ParteEstatusSerializer
from ..models import Parte_Estatus

class ControllerParteEstatus:
    serializer_class = ParteEstatusSerializer
        
    def crearparteestatus(request):
        datosParteEstatus = request.data
        parteEstatusNuevo = Parte_Estatus()
        
        try:
            parteEstatusNuevo.parte_estatus_en = datosParteEstatus['parte_estatus_en']
            parteEstatusNuevo.parte_estatus_es = datosParteEstatus['parte_estatus_es']
        except Exception:
             return {"estatus":"Error"}
        
        parteEstatusNuevo.save()

        return {"estatus":"Ok", 'parte_estatus': parteEstatusNuevo.parte_estatus_es}

    def listarparteestatus(id_parte_estatus=None):
        if id_parte_estatus:
            try:
                queryset = Parte_Estatus.objects.get(id_parte_estatus=id_parte_estatus)
            except Parte_Estatus.DoesNotExist:
                return ({'result': 'No se encontró el estatus de parte deseado'})
            serializer = ParteEstatusSerializer(queryset)
            return serializer.data
        else:
            queryset = Parte_Estatus.objects.all()
            serializer = ParteEstatusSerializer(queryset, many=True)
            return serializer.data
