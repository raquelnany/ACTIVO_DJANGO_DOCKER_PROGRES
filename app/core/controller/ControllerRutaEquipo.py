from ..serializers import RutaEquipoSerializer
from ..models import Ruta_Equipo, Ruta, Equipo


class ControllerRutaEquipo:

    def crearrutaequipo(request):
        datosRutaEquipo = request.data
        try:
            ruta = Ruta.objects.get(id_ruta = datosRutaEquipo['ruta'])
            equipo = Equipo.objects.get(id_equipo = datosRutaEquipo['equipo'])
            rutaEquipoNueva = Ruta_Equipo.objects.create(
                ruta = ruta,
                equipo = equipo
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'ruta_equipo': rutaEquipoNueva.id_ruta_equipo}

    def listarusuariorevisar(id_ruta_equipo=None):
        if id_ruta_equipo:
            try:
                queryset = Ruta_Equipo.objects.get(id_ruta_equipo=id_ruta_equipo)
            except Ruta_Equipo.DoesNotExist:
                return ({'result': 'No se encontró la ruta de equipo deseada'})
            serializer = RutaEquipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Ruta_Equipo.objects.all()
            serializer = RutaEquipoSerializer(queryset, many=True)
            return serializer.data