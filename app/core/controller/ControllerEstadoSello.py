from ..serializers import EstadoSelloSerializer
from ..models import Estado_Sello


class ControllerEstadoSello:
    def crearestadosello(request):
        datos = request.data
        try:
            estadoSelloNuevo = Estado_Sello.objects.create(
                estado_sello_es = datos['estado_sello_es'],  
                estado_sello_en = datos['estado_sello_en']        
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_estado_sello': estadoSelloNuevo.estado_paquete_es}
       
    def listarestadosello(id_estado_sello=None):
        if id_estado_sello:
            try:
                queryset = Estado_Sello.objects.get(id_estado_sello=id_estado_sello)
            except Estado_Sello.DoesNotExist:
                return ({'result': 'No se encontró el estado del sello deseado'})
            serializer = EstadoSelloSerializer(queryset)
            return serializer.data
        else:
            queryset = Estado_Sello.objects.all()
            serializer = EstadoSelloSerializer(queryset, many=True)
            return serializer.data