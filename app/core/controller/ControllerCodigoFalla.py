from ..serializers import CodigoFallaSerializer
from ..models import Codigo_Falla, Mecanismo_Falla


class ControllerCodigoFalla:

    def crearcodigofalla(request):
        datoscodigofalla = request.data
        try:
            mecanismo_falla = Mecanismo_Falla.objects.get(id_mecanismo_falla = datoscodigofalla['mecanismo_falla'])
            
            codigoFallaNuevo = Mecanismo_Falla.objects.create(
                codigo_falla_en = datoscodigofalla['codigo_falla_en'],
                codigo_falla_es = datoscodigofalla['codigo_falla_es'],
                codigo_falla_code = datoscodigofalla['codigo_falla_code'],
                mecanismo_falla = mecanismo_falla
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'mecanismo_falla': codigoFallaNuevo.codigo_falla_es}

    def listarcodigofalla(id_codigo_falla=None):
        if id_codigo_falla:
            try:
                queryset = Codigo_Falla.objects.get(id_codigo_falla=id_codigo_falla)
            except Codigo_Falla.DoesNotExist:
                return ({'result': 'No se encontró el codigo de falla deseado'})
            serializer = CodigoFallaSerializer(queryset)
            return serializer.data
        else:
            queryset = Codigo_Falla.objects.all()
            serializer = CodigoFallaSerializer(queryset, many=True)
            return serializer.data