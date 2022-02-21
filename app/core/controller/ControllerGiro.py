from ..serializers import GiroSerializer
from ..models import Giro


class ControllerGiro:
    def creargiro(request):
        datos = request.data
        try:
            giroNuevo = Giro.objects.create(
                giro = datos['giro'],
                codigo_giro  = datos['codigo_giro']  
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_giro': giroNuevo.giro}
       
    def listarestadopaquete(id_giro=None):
        if id_giro:
            try:
                queryset = Giro.objects.get(id_giro=id_giro)
            except Giro.DoesNotExist:
                return ({'result': 'No se encontró el giro deseado'})
            serializer = GiroSerializer(queryset)
            return serializer.data
        else:
            queryset = Giro.objects.all()
            serializer = GiroSerializer(queryset, many=True)
            return serializer.data
