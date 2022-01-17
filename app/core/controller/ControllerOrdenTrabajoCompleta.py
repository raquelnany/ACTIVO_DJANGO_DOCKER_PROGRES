from ..serializers import OrdenTrabajoCompletaSerializer
from ..models import M4, OT, Codigo_Falla, Mecanismo_Falla, Orden_Trabajo_Completa


class ControllerOrdenTrabajoCompleta:

    def crearordentrabajocompleta(request):
        datosOTC = request.data
        try:
            orden_trabajo  = OT.objects.get(id_ot = datosOTC['orden_trabajo'])
            mecanismo_falla = Mecanismo_Falla.objects.get(id_mecanismo_falla = datosOTC['mecanismo_falla'])
            codigo_falla = Codigo_Falla.objects.get(id_codigo_falla = datosOTC['codigo_falla'])
            m4 = M4.objects.get(id_4m = datosOTC['m4'])

            otcNuevo = Orden_Trabajo_Completa.objects.create(
                orden_trabajo = orden_trabajo,
                cuenta_cc = datosOTC['cuenta_cc'],
                mecanismo_falla =  mecanismo_falla,
                codigo_falla = codigo_falla,
                id_modo_deteccion =  datosOTC['id_modo_deteccion'],
                id_actividad_mantenimiento =  datosOTC['id_actividad_mantenimiento'],
                modo_falla = datosOTC['modo_falla'],
                notas = datosOTC['notas'],
                trabajadores_reales = datosOTC['trabajadores_reales'],
                tiempo_real =  datosOTC['tiempo_real'],
                m4 =  m4
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'orden_trabajo_completa': otcNuevo.cuenta_cc}

    def listarordentrabajocompleta(id_orden_trabajo_completa=None):
        if id_orden_trabajo_completa:
            try:
                queryset = Orden_Trabajo_Completa.objects.get(id_orden_trabajo_completa=id_orden_trabajo_completa)
            except Orden_Trabajo_Completa.DoesNotExist:
                return ({'result': 'No se encontró el almacen de equipo deseado'})
            serializer = OrdenTrabajoCompletaSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Trabajo_Completa.objects.all()
            serializer = OrdenTrabajoCompletaSerializer(queryset, many=True)
            return serializer.data