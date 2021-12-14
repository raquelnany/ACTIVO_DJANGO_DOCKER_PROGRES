from ..serializers import TipoCambioSerializer
from ..models import Tipo_Cambio, Tipo_Rol


class ControllerTipoCambio:
    def creartipocambio(request):
        datosTipoCambio = request.data
        tipoCambioNuevo = Tipo_Cambio()
        try:
            tipoCambioNuevo.tipo_cambio = datosTipoCambio['tipo_cambio']
            tipoCambioNuevo.tipo_cambio_en = datosTipoCambio['tipo_cambio_en']
            tipoCambioNuevo.tipo_cambio_es = datosTipoCambio['tipo_cambio_es']
        except Exception:
             return {"estatus":"Error"}
        
        tipoCambioNuevo.save()
        return {"estatus":"Ok", 'tipo_cambio': tipoCambioNuevo.tipo_cambio}

    def listartipocambio(id_tipo_cambio=None):
        if id_tipo_cambio:
            try:
                queryset = Tipo_Cambio.objects.get(id_tipo_cambio=id_tipo_cambio)
            except Tipo_Cambio.DoesNotExist:
                return ({'result': 'No se encontró el tipo de cambio deseado'})
            serializer = TipoCambioSerializer(queryset)
            return serializer.data
        else:
            queryset = Tipo_Cambio.objects.all()
            serializer = TipoCambioSerializer(queryset, many=True)
            return serializer.data