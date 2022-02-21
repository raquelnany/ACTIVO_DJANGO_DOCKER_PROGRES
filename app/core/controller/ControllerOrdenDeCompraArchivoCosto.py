from ..serializers import OrdenDeCompraArchivoCostoSerializer
from ..models import Orden_De_Compra, Orden_De_Compra_Archivo_Costo, Orden_De_Compra_Cotizacion


class ControllerOrdenDeCompraArchivoCosto:
    def crearordendecompraarchivocosto(request):
        datos = request.data
        try:
            oc = Orden_De_Compra.objects.get(id = datos['oc'])
            oc_cot = Orden_De_Compra_Cotizacion.objects.get(id = datos['oc_cot'])
           
            ordenCompraNuevo = Orden_De_Compra_Archivo_Costo.objects.create(
                importe = datos['importe'],
                realizado_por = datos['realizado_por'],
                fecha_realizado = datos['fecha_realizado'],
                hora_realizado = datos['hora_realizado'],
                oc  = oc, 
                oc_cot = oc_cot   
   
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_archivo_costo': ordenCompraNuevo.id}
       
    def listarordendecompraarchivocosto(id=None):
        if id:
            try:
                queryset = Orden_De_Compra_Archivo_Costo.objects.get(id=id)
            except Orden_De_Compra_Archivo_Costo.DoesNotExist:
                return ({'result': 'No se encontró el archivo de costo de orden de compra deseado'})
            serializer = OrdenDeCompraArchivoCostoSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Archivo_Costo.objects.all()
            serializer = OrdenDeCompraArchivoCostoSerializer(queryset, many=True)
            return serializer.data
