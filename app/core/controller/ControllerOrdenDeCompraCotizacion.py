from ..serializers import OrdenDeCompraCotizacionSerializer  
from ..models import Orden_De_Compra, Orden_De_Compra_Cotizacion, Orden_De_Compra_Proveedor


class ControllerOrdenDeCompraCotizacion:
    def crearordendecompracotizacion(request):
        datos = request.data
        try:
            oc = Orden_De_Compra.objects.get(id =  datos['oc'])
            proveedor = Orden_De_Compra_Proveedor(id_proveedor = datos['proveedor'])
            
            ordenCompraNuevo = Orden_De_Compra_Cotizacion.objects.create(
                fecha_cotizacion  = datos['fecha_cotizacion'], 
                hora_cotizacion  = datos['hora_cotizacion'], 
                productos = datos['productos'], 
                tipo_de_pago = datos['tipo_de_pago'], 
                porcentaje_descuento = datos['porcentaje_descuento'], 
                descuento = datos['descuento'], 
                porcentaje_iva = datos['porcentaje_iva'], 
                iva = datos['iva'], 
                sub_total = datos['sub_total'], 
                total = datos['total'], 
                observaciones = datos['observaciones'], 
                oc = oc, 
                proveedor = proveedor, 
                accion = datos['accion'], 
                deadline_prov  = datos['deadline_prov'], 
                motivo_elim  = datos['motivo_elim']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_de_compra_cotizacion': ordenCompraNuevo.id}
       
    def listarordendecompracotizacion(id=None):
        if id:
            try:
                queryset = Orden_De_Compra_Cotizacion.objects.get(id=id)
            except Orden_De_Compra_Cotizacion.DoesNotExist:
                return ({'result': 'No se encontró la cotizacion de orde de compra deseada'})
            serializer = OrdenDeCompraCotizacionSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Cotizacion.objects.all()
            serializer = OrdenDeCompraCotizacionSerializer(queryset, many=True)
            return serializer.data
