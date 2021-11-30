from ..serializers import OrdenTrabajoTipoSerializer
from ..models import  Orden_Trabajo_Tipo

class ControllerOrdenTrabajoTipo:
    serializer_class = OrdenTrabajoTipoSerializer
        
    def crearordentrabajotipo(request):
        datosOrdenTrabajoTipo= request.data
        ordenTrabajoTipoNuevo = Orden_Trabajo_Tipo()
        try:
            ordenTrabajoTipoNuevo.siglas_es = datosOrdenTrabajoTipo['siglas_es']
            ordenTrabajoTipoNuevo.sigles_en = datosOrdenTrabajoTipo['sigles_en']
            ordenTrabajoTipoNuevo.orden_trabajo_tipo_es = datosOrdenTrabajoTipo['orden_trabajo_tipo_es']
            ordenTrabajoTipoNuevo.orden_trabajo_tipo_en = datosOrdenTrabajoTipo['orden_trabajo_tipo_en']
        except Exception:
             return {"estatus":"Error"}
        
        ordenTrabajoTipoNuevo.save()
        return {"estatus":"Ok", 'orden_trabajo_tipo': ordenTrabajoTipoNuevo.siglas_es}

    def listarordentrabajotipo(id_orden_trabajo_tipo=None):
        if id_orden_trabajo_tipo:
            try:
                queryset = Orden_Trabajo_Tipo.objects.get(id_orden_trabajo_tipo=id_orden_trabajo_tipo)
            except Orden_Trabajo_Tipo.DoesNotExist:
                return ({'result': 'No se encontró el tipo de orden de trabajo deseado'})
            serializer = OrdenTrabajoTipoSerializer(queryset)
            return serializer.data
        else:
            queryset =Orden_Trabajo_Tipo.objects.all()
            serializer = OrdenTrabajoTipoSerializer(queryset, many=True)
            return serializer.data