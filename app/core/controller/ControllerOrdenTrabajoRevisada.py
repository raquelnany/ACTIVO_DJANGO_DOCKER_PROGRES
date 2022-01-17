from ..serializers import OrdenTrabajoRevisadaSerializer
from ..models import OT, Orden_trabajo_Revisada, Usuario


class ControllerOrdenTrabajoRevisada:

    def crearordentrabajorevisada(request):
        datosOTR = request.data
        try:
            ot = OT.objects.get(id_ot = datosOTR['ot'])
            reviso = Usuario.objects.get(id_usuario = datosOTR['reviso'])

            oTRNuevo = Orden_trabajo_Revisada.objects.create(
                ot = ot,
                calificacion_revisada = datosOTR['calificacion_revisada'],
                comentarios_revisada = datosOTR['comentarios_revisada'],
                fecha_revisada = datosOTR['fecha_revisada'],
                hora_revisada = datosOTR['hora_revisada'],
                reviso = reviso
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'orden_trabajo_revisada': oTRNuevo.id_orden_trabajo_revisada}

    def listarordentrabajorevisada(id_orden_trabajo_revisada=None):
        if id_orden_trabajo_revisada:
            try:
                queryset = Orden_trabajo_Revisada.objects.get(id_orden_trabajo_revisada=id_orden_trabajo_revisada)
            except Orden_trabajo_Revisada.DoesNotExist:
                return ({'result': 'No se encontró la orden de trabajo deseada'})
            serializer = OrdenTrabajoRevisadaSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_trabajo_Revisada.objects.all()
            serializer = OrdenTrabajoRevisadaSerializer(queryset, many=True)
            return serializer.data