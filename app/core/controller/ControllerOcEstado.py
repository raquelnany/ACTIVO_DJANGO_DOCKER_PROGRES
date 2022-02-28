from ..serializers import OcEstadoSerializer  
from ..models import Oc_Estado, Orden_De_Compra, Usuario


class ControllerOcEstado:
    def creaocestado(request):
        datosOc = request.data
        try:
            usuario = Usuario.objects.get(id_usuario = datosOc['usuario'])
            oc = Orden_De_Compra.objects.get(id = datosOc['oc'])

            ocNuevo = Oc_Estado.objects.create(
                usuario = usuario,  
                oc = oc
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'oc_estado': ocNuevo.id }
       
    def listarocestado(id=None):
        if id:
            try:
                queryset = Oc_Estado.objects.get(id = id)
            except Oc_Estado.DoesNotExist:
                return ({'result': 'No se encontró el estado de oc equipo deseada'})
            serializer = OcEstadoSerializer(queryset)
            return serializer.data
        else:
            queryset = Oc_Estado.objects.all()
            serializer = OcEstadoSerializer(queryset, many=True)
            return serializer.data
