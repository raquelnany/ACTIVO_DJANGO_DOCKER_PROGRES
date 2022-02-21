from ..serializers import MesSerializer  
from ..models import Mes


class ControllerMes:
    def crearmes(request):
        datosMes = request.data
        try:
            mesNuevo = Mes.objects.create(
                mes_es =  datosMes['mes_es'],
                mes_en = datosMes['mes_en'],
                mes_c_es =  datosMes['mes_c_es'],   
                mes_c_en = datosMes['mes_c_en']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_mes': Mes.mes_es}
       
    def listarmes(id_mes=None):
        if id_mes:
            try:
                queryset = Mes.objects.get(id_mes=id_mes)
            except Mes.DoesNotExist:
                return ({'result': 'No se encontró el mes deseado'})
            serializer = MesSerializer(queryset)
            return serializer.data
        else:
            queryset = Mes.objects.all()
            serializer = MesSerializer(queryset, many=True)
            return serializer.data
