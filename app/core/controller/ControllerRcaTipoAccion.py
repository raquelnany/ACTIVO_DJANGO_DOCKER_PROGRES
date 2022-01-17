from ..serializers import RcaTipoAccionSerializer
from ..models import Rca_Tipo_Accion


class ControllerRcaTipoAccion:

    def crearrcatipoacion(request):
        datosRca = request.data
        RcaNuevo = Rca_Tipo_Accion()
        try:
           RcaNuevo.rca_tipo_accion_en = datosRca['rca_tipo_accion_en']
           RcaNuevo.rca_tipo_accion_es = datosRca['rca_tipo_accion_es']
           RcaNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'rca_tipo_accion': RcaNuevo.rca_tipo_accion_en}

    def listarrcatipoaccion(id_rca_tipo_accion=None):
        if id_rca_tipo_accion:
            try:
                queryset = Rca_Tipo_Accion.objects.get(id_rca_tipo_accion=id_rca_tipo_accion)
            except Rca_Tipo_Accion.DoesNotExist:
                return ({'result': 'No se encontró el rca tipo accion deseado'})
            serializer = RcaTipoAccionSerializer(queryset)
            return serializer.data
        else:
            queryset = Rca_Tipo_Accion.objects.all()
            serializer = RcaTipoAccionSerializer(queryset, many=True)
            return serializer.data

    def generarrcatipoaccion(self):

        CE = Rca_Tipo_Accion.objects.create(
           rca_tipo_accion_en = "Interim",
           rca_tipo_accion_es = "Interina",
        )
        CE.save()

        CE = Rca_Tipo_Accion.objects.create(
           rca_tipo_accion_en = "Adaptive",
           rca_tipo_accion_es = "Adoptiva",
        )
        CE.save()

        CE = Rca_Tipo_Accion.objects.create(
           rca_tipo_accion_en = "Temporal",
           rca_tipo_accion_es = "Temporal",
        )
        CE.save()

        CE = Rca_Tipo_Accion.objects.create(
           rca_tipo_accion_en = "Partia",
           rca_tipo_accion_es = "Parcial",
        )
        CE.save()

        CE = Rca_Tipo_Accion.objects.create(
           rca_tipo_accion_es = "Corrective",
           rca_tipo_accion_en = "Correctiva",
        )
        CE.save()
