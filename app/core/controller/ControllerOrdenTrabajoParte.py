from ..serializers import OrdenTrabajoParteSerializer
from ..models import OT, Instalacion, Inventario, Orden_Trabajo_Parte, Usuario


class ControllerOrdenTrabajoParte:

    def crearordentrabajoparte(request):
        datosParte = request.data
        try:
           ot = OT.objects.get(id_ot=datosParte['ot']) 
           inventario  = Inventario.objects.get(id_inventario=datosParte['inventario'])
           instalacion = Instalacion.objects.get(id_instalacion=datosParte['instalacion'])
           solicitante = Usuario.objects.get(id_usuario=datosParte['solicitante'])

           parteNuevo = Orden_Trabajo_Parte.objects.create(
            ot = ot,
            inventario  = inventario,
            instalacion = instalacion, 
            solicitante = solicitante, 
            cantidad_solicitada = datosParte['cantidad_solicitada'],
            cantidad_surtida = datosParte['cantidad_surtida'],
            parte_estatus = datosParte['parte_estatus'],
            fecha_surtido = datosParte['fecha_surtido'],
            fecha_solicitud = datosParte['fecha_solicitud']
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'orden_trabajo_parte': Orden_Trabajo_Parte.ot}

    def listarordentrabajoparte(id_orden_trabajo_parte=None):
        if id_orden_trabajo_parte:
            try:
                queryset = Orden_Trabajo_Parte.objects.get(id_orden_trabajo_parte=id_orden_trabajo_parte)
            except Orden_Trabajo_Parte.DoesNotExist:
                return ({'result': 'No se encontró la orden de trabajo parte deseada'})
            serializer = OrdenTrabajoParteSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Trabajo_Parte.objects.all()
            serializer = OrdenTrabajoParteSerializer(queryset, many=True)
            return serializer.data