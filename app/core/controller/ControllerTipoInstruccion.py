from ..serializers import TipoInstruccionSerializer
from ..models import Tipo_Instruccion


class ControllerTipoInstruccion:

    def creartipoinstruccion(request):
        datosTipoInstruccion = request.data
        try:
            tipoInstruccionNueva = Tipo_Instruccion.objects.create(                
            tipo_instruccion_es = datosTipoInstruccion['tipo_instruccion_es'],
            tipo_instruccion_en = datosTipoInstruccion['tipo_instruccion_en']

           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'tipo_instruccion': tipoInstruccionNueva.tipo_instruccion_es}

    def listartipoinstruccion(id_tipo_instruccion=None):
        if id_tipo_instruccion:
            try:
                queryset = Tipo_Instruccion.objects.get(id_tipo_instruccion=id_tipo_instruccion)
            except Tipo_Instruccion.DoesNotExist:
                return ({'result': 'No se encontró el tipo de instruccion deseado'})
            serializer = TipoInstruccionSerializer(queryset)
            return serializer.data
        else:
            queryset = Tipo_Instruccion.objects.all()
            serializer = TipoInstruccionSerializer(queryset, many=True)
            return serializer.data