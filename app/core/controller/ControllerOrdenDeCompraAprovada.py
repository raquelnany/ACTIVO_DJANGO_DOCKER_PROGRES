from ..serializers import  OrdenDeCompraAprovadaSerializer
from ..models import Orden_De_Compra, Orden_De_Compra_Aprovada


class ControllerOrdenDeCompraAprovada:
    def creaocaprovada(request):
        datosOc = request.data
        try:
            orden_compra = Orden_De_Compra.objects.get(id =  datosOc['orden_compra'])

            ocNuevo = Orden_De_Compra_Aprovada.objects.create(
                orden_compra = orden_compra,
                id_aprovacion_1 = datosOc['id_aprovacion_1'],
                id_aprovacion_2 = datosOc['id_aprovacion_2'],
                id_aprovacion_3 = datosOc['id_aprovacion_3']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'orden_de_compra_aprovada': ocNuevo.id_orden_compra_aprovada }
       
    def listarocaprovada(id_orden_compra_aprovada=None):
        if id_orden_compra_aprovada:
            try:
                queryset = Orden_De_Compra_Aprovada.objects.get(id_orden_compra_aprovada = id_orden_compra_aprovada)
            except Orden_De_Compra_Aprovada.DoesNotExist:
                return ({'result': 'No se encontró el orden de compra aprovada deseada'})
            serializer = OrdenDeCompraAprovadaSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Aprovada.objects.all()
            serializer = OrdenDeCompraAprovadaSerializer(queryset, many=True)
            return serializer.data
