from ..serializers import TipoProgramaSerializer
from ..models import Tipo_Programa


class ControllerTipoPrograma:

    def creartipoprograma(request):
        datosTipoPrograma = request.data
        try:
            tipoProgramaNuevo = Tipo_Programa.objects.create(
                tipo_programa_es = datosTipoPrograma['tipo_programa_es'],
                tipo_programa_en = datosTipoPrograma['tipo_programa_en']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'tipo_programa': tipoProgramaNuevo.tipo_programa_es}

    def listartipoprograma(id_tipo_programa=None):
        if id_tipo_programa:
            try:
                queryset = Tipo_Programa.objects.get(id_tipo_programa=id_tipo_programa)
            except Tipo_Programa.DoesNotExist:
                return ({'result': 'No se encontró el tipo de programa deseado'})
            serializer = TipoProgramaSerializer(queryset)
            return serializer.data
        else:
            queryset = Tipo_Programa.objects.all()
            serializer = TipoProgramaSerializer(queryset, many=True)
            return serializer.data