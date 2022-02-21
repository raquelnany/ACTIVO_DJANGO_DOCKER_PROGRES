from ..serializers import NivelGastosSerializer
from ..models import Nivel_Gastos


class ControllerNivelGastos:
    def crearnivelgastos(request):
        datos = request.data
        try:
            nivelGastosNuevo = Nivel_Gastos.objects.create(
                gastos_es = datos['gastos_es'],
                gastos_en = datos['gastos_en']        
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_nivel_gastos': nivelGastosNuevo.gastos_es}
       
    def listarnivelgastos(id_nivel_gastos=None):
        if id_nivel_gastos:
            try:
                queryset = Nivel_Gastos.objects.get(id_nivel_gastos=id_nivel_gastos)
            except Nivel_Gastos.DoesNotExist:
                return ({'result': 'No se encontró el nivel de gastos deseado'})
            serializer = NivelGastosSerializer(queryset)
            return serializer.data
        else:
            queryset = Nivel_Gastos.objects.all()
            serializer = NivelGastosSerializer(queryset, many=True)
            return serializer.data
