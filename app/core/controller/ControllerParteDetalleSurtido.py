from ..serializers import  ParteDetalleSurtidoSerializer
from ..models import  Parte_Detalle_Surtido, Inventario_Vale


class ControllerParteDetalleSurtido:

    def crearpartedetallesurtido(request):
        datosParteDetallesurtido = request.data
        try:
            inventario_vale = Inventario_Vale.objects.get(id_inventario_vale = datosParteDetallesurtido['inventario_vale'])

            parteDetallesurtidoNuevo = Parte_Detalle_Surtido.objects.create(
                id_surtido_por  = datosParteDetallesurtido['id_surtido_por'],
                id_orden_trabajo_parte = datosParteDetallesurtido['id_orden_trabajo_parte'],
                inventario_vale = inventario_vale,
                fecha_surtido = datosParteDetallesurtido['fecha_surtido'],
                hora_surtido  = datosParteDetallesurtido['hora_surtido']
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'parte_detalle_surtido': parteDetallesurtidoNuevo.id_orden_trabajo_parte}

    def listarpartedetallesurtido(id_parte_detalle_surtido=None):
        if id_parte_detalle_surtido:
            try:
                queryset = Parte_Detalle_Surtido.objects.get(id_parte_detalle_surtido=id_parte_detalle_surtido)
            except Parte_Detalle_Surtido.DoesNotExist:
                return ({'result': 'No se encontró el detalle de parte surtido deseado'})
            serializer = ParteDetalleSurtidoSerializer(queryset)
            return serializer.data
        else:
            queryset = Parte_Detalle_Surtido.objects.all()
            serializer = ParteDetalleSurtidoSerializer(queryset, many=True)
            return serializer.data