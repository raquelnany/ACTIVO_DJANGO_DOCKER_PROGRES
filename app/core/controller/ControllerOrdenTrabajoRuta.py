from ..serializers import OrdenTrabajoRutaSerializer
from ..models import OT, Equipo, Orden_Trabajo_Ruta, Ruta, Ruta_Condicion, Ruta_Equipo_Componente, Unidad


class ControllerOrdenTrabajoRuta:

    def crearordentrabajoruta(request):
        datosOrdenTrabajoRuta = request.data
        try:
           orden_trabajo = OT.objects.get(id_ot=datosOrdenTrabajoRuta['orden_trabajo']) 
           ruta  = Ruta.objects.get(id_ruta=datosOrdenTrabajoRuta['ruta'])
           equipo = Equipo.objects.get(id_equipo=datosOrdenTrabajoRuta['equipo'])
           id_componente = Ruta_Equipo_Componente.objects.get(id_ruta_equipo_componente=datosOrdenTrabajoRuta['id_componente'])
           condicion = Ruta_Condicion.objects.get(id_ruta_condicion =  datosOrdenTrabajoRuta['condicion'])
           unidad  = Unidad.objects.get(id_unidad = datosOrdenTrabajoRuta['unidad'])

           ordenTrabajoRutaNuevo = Orden_Trabajo_Ruta.objects.create (
                orden_trabajo =  orden_trabajo,
                ruta = ruta,
                equipo = equipo, 
                id_componente = id_componente,
                componente =  datosOrdenTrabajoRuta['componente'],
                condicion =   condicion,
                unidad = unidad,
                puntos = datosOrdenTrabajoRuta['puntos'],
                ventana =  datosOrdenTrabajoRuta['ventana'],
                realizar_activo =  datosOrdenTrabajoRuta['realizar_activo']
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'orden_trabajo_ruta': ordenTrabajoRutaNuevo.componente}

    def listarordentrabajoruta(id_orden_trabajo_ruta=None):
        if id_orden_trabajo_ruta:
            try:
                queryset = Orden_Trabajo_Ruta.objects.get(id_orden_trabajo_ruta=id_orden_trabajo_ruta)
            except Orden_Trabajo_Ruta.DoesNotExist:
                return ({'result': 'No se encontró la orden de trabajo ruta deseada'})
            serializer = OrdenTrabajoRutaSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Trabajo_Ruta.objects.all()
            serializer = OrdenTrabajoRutaSerializer(queryset, many=True)
            return serializer.data