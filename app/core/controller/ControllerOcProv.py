from ..serializers import  OcProvSerializer
from ..models import  Oc_Prov, Orden_De_Compra, Orden_De_Compra_Proveedor


class ControllerOcProv:
    def creaocprov(request):
        datosOc = request.data
        try:
            prov = Orden_De_Compra_Proveedor.objects.get(id_proveedor = datosOc['prov'])
            oc = Orden_De_Compra.objects.get(id =  datosOc['oc'])

            ocNuevo = Oc_Prov.objects.create(
                prov = prov,
                oc = oc,
                visto = datosOc['visto'],
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'oc_prov_nuevo': ocNuevo.id }
       
    def listarocprov(id=None):
        if id:
            try:
                queryset = Oc_Prov.objects.get(id = id)
            except Oc_Prov.DoesNotExist:
                return ({'result': 'No se encontró el proveedor de la oc deseada'})
            serializer = OcProvSerializer(queryset)
            return serializer.data
        else:
            queryset = Oc_Prov.objects.all()
            serializer = OcProvSerializer(queryset, many=True)
            return serializer.data
