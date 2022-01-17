from ..serializers import RcaStatusSerializer
from ..models import Rca_Status


class ControllerRcaStatus:

    def crearrcastatus(request):
        datosRca = request.data
        RcaNuevo = Rca_Status()
        try:
           RcaNuevo.rca_status_en = datosRca['rca_status_en']
           RcaNuevo.rca_status_es = datosRca['rca_status_es']
           RcaNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'rca_status': RcaNuevo.rca_status_en}

    def listarrcastatus(id_rca_status=None):
        if id_rca_status:
            try:
                queryset = Rca_Status.objects.get(id_rca_status=id_rca_status)
            except Rca_Status.DoesNotExist:
                return ({'result': 'No se encontró el rca status deseado'})
            serializer = RcaStatusSerializer(queryset)
            return serializer.data
        else:
            queryset = Rca_Status.objects.all()
            serializer = RcaStatusSerializer(queryset, many=True)
            return serializer.data

    def generarrcastatus(self):

        CE = Rca_Status.objects.create(
           rca_status_en = "Open",
           rca_status_es = "Abierto",
        )
        CE.save()

        CE = Rca_Status.objects.create(
           rca_status_en = "In Progress",
           rca_status_es = "En Progreso",
        )
        CE.save()

        CE = Rca_Status.objects.create(
           rca_status_en = "Completed",
           rca_status_es = "Completado",
        )
        CE.save()

        CE = Rca_Status.objects.create(
           rca_status_en = "Cancelled",
           rca_status_es = "Cancelado",
        )
        CE.save()