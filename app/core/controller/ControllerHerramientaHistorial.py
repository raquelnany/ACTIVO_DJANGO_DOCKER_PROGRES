from ..serializers import HerramientaHistorialSerializer
from ..models import Herramienta, Herramienta_Historial, Herramienta_Movimiento, Usuario


class ControllerHerramientaHistorial:

    def crearherramientahistorial(request):
        datosHerramientahistorial = request.data
        try:
            herramienta = Herramienta.objects.get(id_herramienta = datosHerramientahistorial['herramienta'])
            herramienta_movimiento = Herramienta_Movimiento.objects.get(id_herramienta_moviento=datosHerramientahistorial['id_herramienta_moviente'])
            solicitante = Usuario.objects.get(id_usuario=datosHerramientahistorial['solicitante'])
            usuario = Usuario.objects.get(id_usuario=datosHerramientahistorial['usuario'])

            herramientaHistorialNuevo = Herramienta_Historial.objects.create(
                herramienta= herramienta,
                herramienta_movimiento = herramienta_movimiento,
                fecha_movimiento = datosHerramientahistorial['fecha_movimiento'],
                notas_herramienta = datosHerramientahistorial['notas_herramienta'],
                solicitante = solicitante,
                usuario = usuario,
                prestamo = datosHerramientahistorial['prestamo']

            )

        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'herramienta_historial_nuevo': herramientaHistorialNuevo.herramienta}

    def listarherramientahistorial(id_herramienta_historial=None):
        if id_herramienta_historial:
            try:
                queryset = Herramienta_Historial.objects.get(id_herramienta_historial=id_herramienta_historial)
            except Herramienta_Historial.DoesNotExist:
                return ({'result': 'No se encontró el historial de herramienta deseado'})
            serializer = HerramientaHistorialSerializer(queryset)
            return serializer.data
        else:
            queryset = Herramienta_Historial.objects.all()
            serializer = HerramientaHistorialSerializer(queryset, many=True)
            return serializer.data

