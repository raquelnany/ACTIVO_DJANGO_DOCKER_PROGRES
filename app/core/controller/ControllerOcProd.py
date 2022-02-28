from ..serializers import  OcProdSerializer
from ..models import  Oc_Prod, Orden_De_Compra, Orden_De_Compra_Producto


class ControllerOcProd:
    def creaocprod(request):
        datosOc = request.data
        try:
            producto = Orden_De_Compra_Producto.objects.get(id = datosOc['producto'])
            oc = Orden_De_Compra.objects.get(id =  datosOc['oc'])

            ocNuevo = Oc_Prod.objects.create(
                producto = producto,
                oc = oc
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'oc_prod_nuevo': ocNuevo.id }
       
    def listarocprod(id=None):
        if id:
            try:
                queryset = Oc_Prod.objects.get(id = id)
            except Oc_Prod.DoesNotExist:
                return ({'result': 'No se encontró el producto de la oc equipo deseada'})
            serializer = OcProdSerializer(queryset)
            return serializer.data
        else:
            queryset = Oc_Prod.objects.all()
            serializer = OcProdSerializer(queryset, many=True)
            return serializer.data
