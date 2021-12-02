from ..serializers import OrdenTrabajoEstatusSerializer
from ..models import Orden_Trabajo_Estatus

class ControllerOrdenTrabajoEstatus:
    serializer_class = OrdenTrabajoEstatusSerializer
        
    def crearordentrabajoestatus(request):
        datosOrdenTrabajoEstatus = request.data
        ordenTrabajoEstatusNuevo = Orden_Trabajo_Estatus()
        
        try:
            ordenTrabajoEstatusNuevo.orden_trabajo_estatus_es = datosOrdenTrabajoEstatus['orden_trabajo_estatus_es']
            ordenTrabajoEstatusNuevo.orden_trabajo_estatus_en = datosOrdenTrabajoEstatus['orden_trabajo_estatus_en']
        except Exception:
             return {"estatus":"Error"}
        
        ordenTrabajoEstatusNuevo.save()

        return {"estatus":"Ok", 'orden_trabajo_estatus': ordenTrabajoEstatusNuevo.orden_trabajo_estatus_en}

    def listarordentrabajoestatus(id_orden_trabajo_estatus=None):
        if id_orden_trabajo_estatus:
            try:
                queryset = Orden_Trabajo_Estatus.objects.get(id_orden_trabajo_estatus=id_orden_trabajo_estatus)
            except Orden_Trabajo_Estatus.DoesNotExist:
                return ({'result': 'No se encontró el estatus de la orden de trabajo deseada'})
            serializer = OrdenTrabajoEstatusSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Trabajo_Estatus.objects.all()
            serializer = OrdenTrabajoEstatusSerializer(queryset, many=True)
            return serializer.data

    def generarordentrabajoestatus(self):
        
        notificada = Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Notificada',
           orden_trabajo_estatus_en='Notified'
        )
        notificada.save()

        abierta = Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Abierta',
           orden_trabajo_estatus_en='Open'
        )
        abierta.save()

        asignada = Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Asignada',
           orden_trabajo_estatus_en='Assigned'
        )
        asignada.save()

        activa = Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Activa',
           orden_trabajo_estatus_en='Active'
        )
        activa.save()

        completa= Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Completa',
           orden_trabajo_estatus_en='Completed'
        )
        completa.save()

        revisada = Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Revisada',
           orden_trabajo_estatus_en='Reviewed'
        )
        revisada.save()


        cancelada = Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Cancelada',
           orden_trabajo_estatus_en='Canceled'
        )
        cancelada.save()

        programada = Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Programada',
           orden_trabajo_estatus_en='Schenduled'
        )
        programada.save()

        programada_sin_asignar = Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Programada Sin Asignar',
           orden_trabajo_estatus_en='Schenduled Unasigned'
        )
        programada_sin_asignar.save()

        re_abierta = Orden_Trabajo_Estatus.objects.create(
           orden_trabajo_estatus_es='Re-Abierta',
           orden_trabajo_estatus_en='Re-Open'
        )
        re_abierta.save()


      