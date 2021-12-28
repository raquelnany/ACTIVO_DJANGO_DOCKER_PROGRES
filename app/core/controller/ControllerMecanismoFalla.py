from ..serializers import MecanismoFallaSerializer
from ..models import Mecanismo_Falla


class ControllerMecanismoFalla:

    def crearmecanismofalla(request):
        datoMecanismoFalla = request.data
        try:
            mecanismoFallaNueva = Mecanismo_Falla.objects.create(
                mecanismo_falla_en = datoMecanismoFalla['mecanismo_falla_en'],
                mecanismo_falla_es = datoMecanismoFalla['mecanismo_falla_es'],
                mecanismo_falla_code = datoMecanismoFalla['mecanismo_falla_code']

           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'mecanismo_falla': mecanismoFallaNueva.mecanismo_falla_es}

    def listarmecanismofalla(id_mecanismo_falla=None):
        if id_mecanismo_falla:
            try:
                queryset = Mecanismo_Falla.objects.get(id_mecanismo_falla=id_mecanismo_falla)
            except Mecanismo_Falla.DoesNotExist:
                return ({'result': 'No se encontró la falla del mecanismo deseado'})
            serializer = MecanismoFallaSerializer(queryset)
            return serializer.data
        else:
            queryset = Mecanismo_Falla.objects.all()
            serializer = MecanismoFallaSerializer(queryset, many=True)
            return serializer.data