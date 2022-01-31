from ..serializers import CausaRaizSerializer  
from ..models import Causa_Raiz, Equipo


class ControllerCausaRaiz:
    def crearcausaraiz(request):
        datosCausaRaiz = request.data
        try:
            equipo = Equipo.objects.get(id_equipo = datosCausaRaiz['equipo'])
           
            causaRaizNueva = Causa_Raiz.objects.create(
                equipo = equipo,
                descripcion_causa_raiz = datosCausaRaiz['descripcion_causa_raiz']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'causa_raiz_nueva': causaRaizNueva.id_causa_raiz}
       
    def listarcausaraiz(id_causa_raiz=None):
        if id_causa_raiz:
            try:
                queryset = Causa_Raiz.objects.get(id_causa_raiz=id_causa_raiz)
            except Causa_Raiz.DoesNotExist:
                return ({'result': 'No se encontró la causa raiz deseada'})
            serializer = CausaRaizSerializer(queryset)
            return serializer.data
        else:
            queryset = Causa_Raiz.objects.all()
            serializer = CausaRaizSerializer(queryset, many=True)
            return serializer.data
