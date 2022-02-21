from ..serializers import EstadoPaqueteSerializer
from ..models import Estado_Paquete


class ControllerEstadoPaquete:
    def crearestadopaquete(request):
        datos = request.data
        try:
            estadoPaqueteNuevo = Estado_Paquete.objects.create(
                estado_paquete_es = datos['estado_paquete_es'],  
                estado_paquete_en  = datos['estado_paquete_en']        
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_estado_paquete': estadoPaqueteNuevo.estado_paquete_es}
       
    def listarestadopaquete(id_estado_paquete=None):
        if id_estado_paquete:
            try:
                queryset = Estado_Paquete.objects.get(id_estado_paquete=id_estado_paquete)
            except Estado_Paquete.DoesNotExist:
                return ({'result': 'No se encontró el estado del paquete deseado'})
            serializer = EstadoPaqueteSerializer(queryset)
            return serializer.data
        else:
            queryset = Estado_Paquete.objects.all()
            serializer = EstadoPaqueteSerializer(queryset, many=True)
            return serializer.data
