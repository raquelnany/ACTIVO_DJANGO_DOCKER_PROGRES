from ..serializers import RutaEquipoComponenteSerializer
from ..models import Ruta_Condicion, Ruta_Condicion_Unidad, Ruta_Equipo, Ruta_Equipo_Componente


class ControllerRutaEquipoComponente:

    def crearrutaequipocomponente(request):
        datosRutaEquipoComponente = request.data
        try:
            ruta_equipo = Ruta_Equipo.objects.get(id_ruta_equipo = datosRutaEquipoComponente['ruta_equipo'])
            ruta_condicion = Ruta_Condicion.objects.get(id_ruta_condicion = datosRutaEquipoComponente['ruta_condicion'])
            ruta_condicion_unidad = Ruta_Condicion_Unidad.objects.get(id_ruta_condicion_unidad = datosRutaEquipoComponente['ruta_condicion_unidad'])


            rutaEquipoComponenteNuevo = Ruta_Equipo_Componente.objects.create(
                ruta_equipo = ruta_equipo,
                componente = datosRutaEquipoComponente['componente'],
                ruta_condicion =  ruta_condicion,
                ruta_condicion_unidad =  ruta_condicion_unidad,
                puntos_componente = datosRutaEquipoComponente['puntos_componente'],
                fecha_componente = datosRutaEquipoComponente['fecha_componente'],
                ciclo = datosRutaEquipoComponente['ciclo'],
                id_ciclo_condicion = datosRutaEquipoComponente['id_ciclo_condicion'],
                ciclo_cantidad = datosRutaEquipoComponente['ciclo_cantidad']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'ruta_equipo_componente': rutaEquipoComponenteNuevo.id_ruta_equipo_componente}

    def listarrutaequipocomponente(id_ruta_equipo_componente=None):
        if id_ruta_equipo_componente:
            try:
                queryset = Ruta_Equipo_Componente.objects.get(id_ruta_equipo_componente=id_ruta_equipo_componente)
            except Ruta_Equipo_Componente.DoesNotExist:
                return ({'result': 'No se encontróla ruta equipo componente deseada'})
            serializer = RutaEquipoComponenteSerializer(queryset)
            return serializer.data
        else:
            queryset = Ruta_Equipo_Componente.objects.all()
            serializer = RutaEquipoComponenteSerializer(queryset, many=True)
            return serializer.data