from ..serializers import OrdenSubestatusSerializer
from ..models import Orden_Subestatus

class ControllerOrdenSubestatus:
    serializer_class = OrdenSubestatusSerializer
        
    def crearordensubestatus(request):
        datosOrdenSubestatus = request.data
        ordenSubestatusNuevo = Orden_Subestatus()
        
        try:
            ordenSubestatusNuevo.orden_subestatus_es = datosOrdenSubestatus['orden_subestatus_es']
            ordenSubestatusNuevo.orden_subestatus_en = datosOrdenSubestatus['orden_subestatus_en']
        except Exception:
             return {"estatus":"Error"}
        
        ordenSubestatusNuevo.save()

        return {"estatus":"Ok", 'orden_subestatus': ordenSubestatusNuevo.orden_subestatus_es}

    def listarordensubestatus(id_orden_subestatus=None):
        if id_orden_subestatus:
            try:
                queryset = Orden_Subestatus.objects.get(id_orden_subestatus=id_orden_subestatus)
            except Orden_Subestatus.DoesNotExist:
                return ({'result': 'No se encontró el subestatus estatus de la orden deseada'})
            serializer = OrdenSubestatusSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Subestatus.objects.all()
            serializer = OrdenSubestatusSerializer(queryset, many=True)
            return serializer.data


    def generarordensubestatus(self):
        
        listo = Orden_Subestatus.objects.create(
           orden_subestatus_es='Listo',
           orden_subestatus_en='Ready'
        )
        listo.save()

        programado = Orden_Subestatus.objects.create(
           orden_subestatus_es='Programado',
           orden_subestatus_en='Schedule'
        )
        programado.save()

        libranza = Orden_Subestatus.objects.create(
           orden_subestatus_es='Libranza',
           orden_subestatus_en='Release'
        )
        libranza.save()

        planeado = Orden_Subestatus.objects.create(
           orden_subestatus_es='Planeado',
           orden_subestatus_en='Planned'
        )
        planeado.save()

        aprobado= Orden_Subestatus.objects.create(
           orden_subestatus_es='Aprobado',
           orden_subestatus_en='Approved'
        )
        aprobado.save()

        espera_de_produccion = Orden_Subestatus.objects.create(
           orden_subestatus_es='Espera de Producción',
           orden_subestatus_en='Waiting for Production'
        )
        espera_de_produccion.save()


        espera_de_partes = Orden_Subestatus.objects.create(
           orden_subestatus_es='Espera de Partes',
           orden_subestatus_en='Hold for Parts'
        )
        espera_de_partes.save()

        retrabajo = Orden_Subestatus.objects.create(
           orden_subestatus_es='Retrabajo',
           orden_subestatus_en='Rework'
        )
        retrabajo.save()
