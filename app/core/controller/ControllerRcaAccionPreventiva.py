from ..serializers import RcaAccionPreventivaSerializer
from ..models import Rca_Accion_Preventiva, OT, Rca, Rca_Preventive_Status


class ControllerRcaAccionPreventiva:

    def crearrcaaccionpreventiva(request):
        datosRCA = request.data
        try:
            rca = Rca.objects.get(id_rca = datosRCA['rca'])
            ot  = OT.objects.get(id_ot = datosRCA['ot'])
            rca_preventive_status = Rca_Preventive_Status.objects.get(id_rca_preventive_status = datosRCA['rca_preventive_status'])
            
            rcaNuevo = Rca.objects.create(
                rca = rca,
                ot = ot,
                rca_accion_preventiva = datosRCA['rca_accion_preventiva'],
                fecha_cumpliento = datosRCA['fecha_cumpliento'],
                duenio = datosRCA['duenio'],
                rca_preventive_status = rca_preventive_status,
                fecha_apertura = datosRCA['fecha_apertura']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'rca': rcaNuevo.rca_accion_preventiva}

    def listarrcaaccionpreventiva(id_rca_accion_preventiva=None):
        if id_rca_accion_preventiva:
            try:
                queryset = Rca_Accion_Preventiva.objects.get(id_rca_accion_preventiva=id_rca_accion_preventiva)
            except Rca_Accion_Preventiva.DoesNotExist:
                return ({'result': 'No se encontró el RCA deseado'})
            serializer = RcaAccionPreventivaSerializer(queryset)
            return serializer.data
        else:
            queryset = Rca_Accion_Preventiva.objects.all()
            serializer = RcaAccionPreventivaSerializer(queryset, many=True)
            return serializer.data