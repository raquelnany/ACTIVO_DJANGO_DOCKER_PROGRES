from ..serializers import OrdenDeCompraPresupuestoSerializer
from ..models import Orden_De_Compra_Presupuesto, Usuario


class ControllerOrdenDeCompraPresupuesto:
    def crearordendecomprapresupuesto(request):
        datos = request.data
        try:
            usuario_autoriza_presupuesto = Usuario.objects.get(id_usuario =  datos['usuario_autoriza_presupuesto'])
            usuario_solicita_presupuesto = Usuario.objects.get(id_usuario =  datos['usuario_solicita_presupuesto'])

            ordenCompraNuevo = Orden_De_Compra_Presupuesto.objects.create(
                id_fiscal = datos['id_fiscal'],
                usuario_autoriza_presupuesto = usuario_autoriza_presupuesto,
                usuario_solicita_presupuesto = usuario_solicita_presupuesto,
                fecha_presupuesto = datos['fecha_presupuesto'],
                plazo_presupuesto = datos['plazo_presupuesto'],
                importe = datos['importe']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_presupuesto': ordenCompraNuevo.id}
       
    def listarordendecomprapresupuesto(id=None):
        if id:
            try:
                queryset = Orden_De_Compra_Presupuesto.objects.get(id=id)
            except Orden_De_Compra_Presupuesto.DoesNotExist:
                return ({'result': 'No se encontró el presupuesto de orden de compra deseado'})
            serializer = OrdenDeCompraPresupuestoSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Presupuesto.objects.all()
            serializer = OrdenDeCompraPresupuestoSerializer(queryset, many=True)
            return serializer.data
