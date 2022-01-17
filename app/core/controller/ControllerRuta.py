from ..serializers import RutaSerializer
from ..models import Frecuencia, Instalacion, Orden_Trabajo_Tipo, Ruta, Ruta_Estatus, Tipo_Programa, Usuario


class ControllerRuta:

    def crearruta(request):
        datosRuta = request.data
        try:
            user_creador = Usuario.objects.get(id_usuario =  datosRuta['user_creador'])
            user_modifico = Usuario.objects.get(id_usuario =  datosRuta['user_modifico'])
            ruta_estatus = Ruta_Estatus.objects.get(id_ruta_estatus = datosRuta['ruta_estatus'])
            frecuencia = Frecuencia.objects.get(id_frecuencia = datosRuta['frecuencia'])
            instalacion = Instalacion.objects.get(id_instalacion = datosRuta['instalacion'])
            tipo_ot = Orden_Trabajo_Tipo.objects.get(id_orden_trabajo_tipo = datosRuta['tipo_ot'])
            tipo_programa  = Tipo_Programa.objects.get(id_tipo_programa = datosRuta['tipo_programa'])

            rutaNueva = Ruta.objects.create(
                user_creador = user_creador,
                user_modifico = user_modifico,
                ruta_estatus = ruta_estatus,
                frecuencia = frecuencia,
                id_asignado = datosRuta['id_asignado'],
                instalacion = instalacion,
                ruta = datosRuta['tipo_ot'],
                ruta_codigo = datosRuta['ruta_codigo'],
                ruta_cada = datosRuta['ruta_cada'],
                ruta_modificado = datosRuta['ruta_modificado'],
                tipo_ot = tipo_ot,
                tipo_programa  = tipo_programa,
                ruta_alcance = datosRuta['ruta_alcance'],
                ruta_trabajadores = datosRuta['ruta_trabajadores'],
                ruta_realizar_activo = datosRuta['ruta_realizar_activo'],
                tiempo_estimado = datosRuta['tiempo_estimado']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'ruta': rutaNueva.id_ruta}

    def listarruta(id_ruta=None):
        if id_ruta:
            try:
                queryset = Ruta.objects.get(id_ruta=id_ruta)
            except Ruta.DoesNotExist:
                return ({'result': 'No se encontró la ruta deseada'})
            serializer = RutaSerializer(queryset)
            return serializer.data
        else:
            queryset = Ruta.objects.all()
            serializer = RutaSerializer(queryset, many=True)
            return serializer.data