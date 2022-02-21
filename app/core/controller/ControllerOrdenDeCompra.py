from ..serializers import OrdenDeCompraSerializer
from ..models import Orden_De_Compra, Orden_De_Compra_Proveedor, Usuario


class ControllerOrdenDeCompra:
    def crearordendecompra(request):
        datos = request.data
        try:
            usuario_elabora = Usuario.objects.get(id_usuario = datos['usuario_elabora'])
            proveedor = Orden_De_Compra_Proveedor.objects.get(id_proveedor = datos['proveedor'])
            solicitante = Usuario.objects.get(id_usuario = datos['solicitante'])

            ordenCompraNuevo = Orden_De_Compra.objects.create(
                id_visible_orden_de_compra = datos['id_visible_orden_de_compra'],
                accion = datos['accion'],
                usuario_elabora = usuario_elabora,
                fecha_emitido  = datos['fecha_emitido'],
                hora_emitido  = datos['hora_emitido'],
                fecha_deadline  = datos['fecha_deadline'],
                hora_deadline  =datos['hora_deadline'],
                proveedor = proveedor,
                producto_servicio = datos['producto_servicio'],
                sub_total = datos['sub_total'],
                procentaje_iva =datos['procentaje_iva'],
                iva =datos['iva'],
                gran_total = datos['gran_total'],
                explicativo =datos['explicativo'],
                fecha_salida_por_oc  = datos['fecha_salida_por_oc'],
                hora_salida_por_oc  = datos['hora_salida_por_oc'],
                fecha_ingreso_por_oc  = datos['fecha_ingreso_por_oc'],
                hora_ingreso_por_oc  = datos['hora_ingreso_por_oc'], 
                tipo_cambio = datos['tipo_cambio'],
                comprador_asignado = datos['comprador_asignado'],
                criticidad = datos['criticidad'],
                linea_caida = datos['linea_caida'],
                solicitante = solicitante 
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra': ordenCompraNuevo.id_visible_orden_de_compra}
       
    def listarordendecompra(id=None):
        if id:
            try:
                queryset = Orden_De_Compra.objects.get(id=id)
            except Orden_De_Compra.DoesNotExist:
                return ({'result': 'No se encontró la orden de compra deseada'})
            serializer = OrdenDeCompraSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra.objects.all()
            serializer = OrdenDeCompraSerializer(queryset, many=True)
            return serializer.data
