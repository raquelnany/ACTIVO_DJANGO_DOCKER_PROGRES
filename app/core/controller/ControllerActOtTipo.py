from ..serializers import AtcOtTipoSerializer
from ..models import Act_Ot_Tipo

class ControllerActOtTipo:
    def crearactottipo(request):
        datostipo = request.data
        tipoNuevo = Act_Ot_Tipo()
        try:
            tipoNuevo.act_ot_tipo_en = datostipo['act_ot_tipo_en']
            tipoNuevo.act_ot_tipo_es = datostipo['act_ot_tipo_es']
        except Exception:
             return {"estatus":"Error"}
        
        tipoNuevo.save()
        return {"estatus":"Ok", 'codigo': tipoNuevo.act_ot_tipo_es}

    def listaractottipo(id_act_ot_tipo=None):
        if id_act_ot_tipo:
            try:
                queryset = Act_Ot_Tipo.objects.get(id_act_ot_tipo=id_act_ot_tipo)
            except Act_Ot_Tipo.DoesNotExist:
                return ({'result': 'No se encontró el act ot tipo deseado'})
            serializer = AtcOtTipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Act_Ot_Tipo.objects.all()
            serializer = AtcOtTipoSerializer(queryset, many=True)
            return serializer.data