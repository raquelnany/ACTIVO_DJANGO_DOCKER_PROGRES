from ..serializers import InstruccionSerializer
from ..models import Instruccion, Tiempo_Unidad, Tipo_Instruccion


class ControllerInstruccion:

    def crearainstruccion(request):
        datosInstruccion = request.data
        try:
            
            tipo = Tipo_Instruccion.objects.get(id_instruccion = datosInstruccion['tipo'])
            unidad = Tiempo_Unidad.objects.get(id_tiempo_unidad = datosInstruccion['unidad'])

            instruccionNueva = Instruccion.objects.create(
                instruccion = datosInstruccion['instruccion'],
                codigo = datosInstruccion['codigo'],
                tipo = tipo,
                tiempo =datosInstruccion['tiempo'],
                unidad = unidad,  
                descripcion = datosInstruccion['descripcion']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'instruccion': instruccionNueva.instruccion}

    def listarinstruccion(id_instruccion=None):
        if id_instruccion:
            try:
                queryset = Instruccion.objects.get(id_instruccion=id_instruccion)
            except Instruccion.DoesNotExist:
                return ({'result': 'No se encontró la instruccion deseada'})
            serializer = InstruccionSerializer(queryset)
            return serializer.data
        else:
            queryset = Instruccion.objects.all()
            serializer = InstruccionSerializer(queryset, many=True)
            return serializer.data