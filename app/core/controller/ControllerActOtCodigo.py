from ..serializers import AtcOtCodigoSerializer
from ..models import Act_Ot_Codigo


class ControllerActOtCodigo:
    def crearactotcodigo(request):
        datosCodigo = request.data
        codigoNuevo = Act_Ot_Codigo()
        try:
            codigoNuevo.act_ot_codigo_en = datosCodigo['act_ot_codigo_en']
            codigoNuevo.act_ot_codigo_es = datosCodigo['act_ot_codigo_es']
            codigoNuevo.act_clave = datosCodigo['act_clave']
        except Exception:
             return {"estatus":"Error"}
        
        codigoNuevo.save()
        return {"estatus":"Ok", 'codigo': codigoNuevo.act_ot_codigo_es}

    def listaractotcodigo(id_act_ot_codigo=None):
        if id_act_ot_codigo:
            try:
                queryset = Act_Ot_Codigo.objects.get(id_act_ot_codigo=id_act_ot_codigo)
            except Act_Ot_Codigo.DoesNotExist:
                return ({'result': 'No se encontró el act ot codigo deseado'})
            serializer = AtcOtCodigoSerializer(queryset)
            return serializer.data
        else:
            queryset = Act_Ot_Codigo.objects.all()
            serializer = AtcOtCodigoSerializer(queryset, many=True)
            return serializer.data