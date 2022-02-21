from ..serializers import OrdenDeCompraEmailVistoSerializer
from ..models import Orden_De_Compra, Orden_De_Compra_Email_Visto, Orden_De_Compra_Proveedor


class ControllerOrdenDeCompraEmailVisto:
    def crearordendecompraemailvisto(request):
        datos = request.data
        try:
            oc = Orden_De_Compra.objects.get(id = datos['oc'])
            prov = Orden_De_Compra_Proveedor.objects.get(id_proveedor = datos['prov'])
           
            ordenCompraNuevo = Orden_De_Compra_Email_Visto.objects.create(
                oc  = oc, 
                prov = prov, 
                estado = datos['estado']  
   
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_email_visto': ordenCompraNuevo.orden_de_compra_email_visto}
       
    def listarordendecompraemailvisto(orden_de_compra_email_visto=None):
        if orden_de_compra_email_visto:
            try:
                queryset = Orden_De_Compra_Email_Visto.objects.get(orden_de_compra_email_visto=orden_de_compra_email_visto)
            except Orden_De_Compra_Email_Visto.DoesNotExist:
                return ({'result': 'No se encontró el archivo de costo de orden de compra deseado'})
            serializer = OrdenDeCompraEmailVistoSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Email_Visto.objects.all()
            serializer = OrdenDeCompraEmailVistoSerializer(queryset, many=True)
            return serializer.data
