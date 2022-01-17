from ..serializers import RCASerializer
from ..models import Rca, OT, Rca_Status, Rca_Tipo_Accion


class ControllerRca:

    def crearrca(request):
        datosRCA = request.data
        try:
            ot  = OT.objects.get(id_ot = datosRCA['ot'])
            rca_tipo_accion = Rca_Tipo_Accion.objects.get(id_rca_tipo_accion = datosRCA['rca_tipo_accion'])
            rca_status = Rca_Status.objects.get(id_rca_status = datosRCA['rca_status'])

            rcaNuevo = Rca.objects.create(
                ot = ot,
                rca_causa = datosRCA['rca_causa'],
                rca_tipo_accion = rca_tipo_accion,
                rca_status = rca_status,
                rca_causa_raiz = datosRCA['rca_causa_raiz']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'rca': rcaNuevo.rca_causa}

    def listarrca(id_rca=None):
        if id_rca:
            try:
                queryset = Rca.objects.get(id_rca=id_rca)
            except Rca.DoesNotExist:
                return ({'result': 'No se encontró el RCA deseado'})
            serializer = RCASerializer(queryset)
            return serializer.data
        else:
            queryset = Rca.objects.all()
            serializer = RCASerializer(queryset, many=True)
            return serializer.data