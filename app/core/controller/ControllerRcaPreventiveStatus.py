from ..serializers import RcaPreventiveStatusSerializer
from ..models import Rca_Preventive_Status


class ControllerRcaPreventiveStatus:

    def crearrcapreventivestatus(request):
        datosRca = request.data
        RcaNuevo = Rca_Preventive_Status()
        try:
           RcaNuevo.rca_preventive_status_en = datosRca['rca_preventive_status_en']
           RcaNuevo.rca_preventive_status_es = datosRca['rca_preventive_status_es']
           RcaNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'rca_preventive_status': RcaNuevo.rca_preventive_status_en}

    def listarrcapreventivestatus(id_rca_preventive_status=None):
        if id_rca_preventive_status:
            try:
                queryset = Rca_Preventive_Status.objects.get(id_rca_preventive_status=id_rca_preventive_status)
            except Rca_Preventive_Status.DoesNotExist:
                return ({'result': 'No se encontró el rca preventive status deseado'})
            serializer = RcaPreventiveStatusSerializer(queryset)
            return serializer.data
        else:
            queryset = Rca_Preventive_Status.objects.all()
            serializer = RcaPreventiveStatusSerializer(queryset, many=True)
            return serializer.data

    def generarrcapreventivestatus(self):

        CE = Rca_Preventive_Status.objects.create(
           rca_preventive_status_en = "Open",
           rca_preventive_status_es = "Abierto",
        )
        CE.save()

        CE = Rca_Preventive_Status.objects.create(
           rca_preventive_status_en = "In Progress",
           rca_preventive_status_es = "En Progreso",
        )
        CE.save()

        CE = Rca_Preventive_Status.objects.create(
           rca_preventive_status_en = "Completed",
           rca_preventive_status_es = "Completado",
        )
        CE.save()

        CE = Rca_Preventive_Status.objects.create(
           rca_preventive_status_en = "Cancelled",
           rca_preventive_status_es = "Cancelado",
        )
        CE.save()