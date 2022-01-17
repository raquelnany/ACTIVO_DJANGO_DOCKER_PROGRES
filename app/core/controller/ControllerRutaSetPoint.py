from ..serializers import RutaSetPointSerializer
from ..models import Ruta_Equipo_Componente, Ruta_Set_Point, Ruta_Set_Point_Operador


class ControllerRutaSetPoint:

    def crearrutasetpoint(request):
        datosRuta = request.data
        try:
            ruta_equipo_componente = Ruta_Equipo_Componente.objects.get(id_ruta_equipo_componente = datosRuta['ruta_equipo_componente'])
            ruta_set_point_operador = Ruta_Set_Point_Operador.objects.get(id_ruta_set_point_operador = datosRuta['ruta_set_point_operador'])

            rutaSetPointNuevo = Ruta_Set_Point.objects.create(
                ruta_equipo_componente =  ruta_equipo_componente,
                ruta_set_point_operador =  ruta_set_point_operador,
                ruta_set_point_1 = datosRuta['ruta_set_point_1'],
                ruta_set_point_2 = datosRuta['ruta_set_point_2']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'ruta_set_point': rutaSetPointNuevo.id_ruta_set_point}

    def listarrutasetpoint(id_ruta_set_point=None):
        if id_ruta_set_point:
            try:
                queryset = Ruta_Set_Point.objects.get(id_ruta_set_point=id_ruta_set_point)
            except Ruta_Set_Point.DoesNotExist:
                return ({'result': 'No se encontró la ruta set point deseada'})
            serializer = RutaSetPointSerializer(queryset)
            return serializer.data
        else:
            queryset = Ruta_Set_Point.objects.all()
            serializer = RutaSetPointSerializer(queryset, many=True)
            return serializer.data