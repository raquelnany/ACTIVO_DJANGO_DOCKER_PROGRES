from ..serializers import TareaOrdenTrabajoSerializer
from ..models import OT, Tarea_Orden_Trabajo

class ControllerTareaOrdenTrabajo:
    def creartareaordentrabajo(request):
        datosTarea = request.data
        try:
            orden_trabajo = OT.objects.get(id_ot=datosTarea['orden_trabajo'])
                    
            tareaNueva = Tarea_Orden_Trabajo.objects.create(
                id_tarea = datosTarea['orden_trabajo'],
                orden_trabajo = orden_trabajo,
                fecha  = datosTarea['fecha'],
                hora =datosTarea['hora'],
                instrucciones = datosTarea['instrucciones'],
                fecha_base = datosTarea['fecha_base'],
                tiempo_estimado = datosTarea['tiempo_estimado'],
                ventana_cumplimiento = datosTarea['ventana_cumplimiento'],
                bloque_en = datosTarea['bloque_en'],
            )
                
        except Exception:
            return {"estatus":"Error"}

        return {"estatus":"Ok", 'nueva_tarea': tareaNueva.id_tarea}
       
    def listartareaordentrabajo(id_tarea_orden_trabajo=None):
        if id_tarea_orden_trabajo:
            try:
                queryset = Tarea_Orden_Trabajo.objects.get(id_tarea_orden_trabajo=id_tarea_orden_trabajo)
            except Tarea_Orden_Trabajo.DoesNotExist:
                return ({'result': 'No se encontró la tarea de la orden de trabajo deseada'})
            serializer = TareaOrdenTrabajoSerializer(queryset)
            return serializer.data
        else:
            queryset = Tarea_Orden_Trabajo.objects.all()
            serializer = TareaOrdenTrabajoSerializer(queryset, many=True)
            return serializer.data

  