from ..serializers import OrdenTrabajoPrioridadSerializer
from ..models import Orden_Trabajo_Prioridad

class ControllerOrdenTrabajoPrioridad:
    serializer_class = OrdenTrabajoPrioridadSerializer
        
    def crearordentrabajoprioridad(request):
        datosOrdenTrabajoPrioridad = request.data
        ordenTrabajoPrioridadNuevo = Orden_Trabajo_Prioridad()
        
        try:
            ordenTrabajoPrioridadNuevo.orden_trabajo_prioridad_es = datosOrdenTrabajoPrioridad['orden_trabajo_prioridad_es']
            ordenTrabajoPrioridadNuevo.orden_trabajo_prioridad_en = datosOrdenTrabajoPrioridad['orden_trabajo_prioridad_en']
        except Exception:
             return {"estatus":"Error"}
        
        ordenTrabajoPrioridadNuevo.save()

        return {"estatus":"Ok", 'orden_trabajo_prioridad': ordenTrabajoPrioridadNuevo.orden_trabajo_prioridad_es}

    def listarordentrabajoprioridad(id_orden_trabajo_prioridad=None):
        if id_orden_trabajo_prioridad:
            try:
                queryset = Orden_Trabajo_Prioridad.objects.get(id_orden_trabajo_prioridad=id_orden_trabajo_prioridad)
            except Orden_Trabajo_Prioridad.DoesNotExist:
                return ({'result': 'No se encontró la prioridad de la orden de trabajo deseada'})
            serializer = OrdenTrabajoPrioridadSerializer(queryset)
            return serializer.data
        else:
            queryset =Orden_Trabajo_Prioridad.objects.all()
            serializer = OrdenTrabajoPrioridadSerializer(queryset, many=True)
            return serializer.data
