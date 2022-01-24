from ..serializers import OrdenTrabajoRutaSetPointSerializer
from ..models import Orden_Trabajo_Ruta, Orden_Trabajo_Ruta_Set_Point, Ruta_Set_Point_Operador


class ControllerOrdenTrabajoRutaSetPoint:
    def crearordentrabajorutasetpoint(request):
        datosOT = request.data
        try:
            orden_trabajo_ruta = Orden_Trabajo_Ruta.objects.get(id_orden_trabajo_ruta = datosOT['orden_trabajo_ruta'])
            operador = Ruta_Set_Point_Operador.objects.get(id_ruta_set_point_operador = datosOT['operador'])

            ordenTrabajoNuevo = Orden_Trabajo_Ruta_Set_Point.objects.create(
                orden_trabajo_ruta = orden_trabajo_ruta,
                operador =  operador,
                punto_a_base =  datosOT['punto_a_base'],
                lectura = datosOT['lectura'],
                punto_b_base =  datosOT['punto_b_base'],
                modifico = datosOT['modifico']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'orden_trabajo_ruta_set_point': ordenTrabajoNuevo.id_orden_trabajo_ruta_set_point}
       
    def listarordentrabajorutasetpoint(id_orden_trabajo_ruta_set_point=None):
        if id_orden_trabajo_ruta_set_point:
            try:
                queryset = Orden_Trabajo_Ruta_Set_Point.objects.get(id_orden_trabajo_ruta_set_point=id_orden_trabajo_ruta_set_point)
            except Orden_Trabajo_Ruta_Set_Point.DoesNotExist:
                return ({'result': 'No se encontró la orden trabajo ruta set point deseada'})
            serializer = OrdenTrabajoRutaSetPointSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Trabajo_Ruta_Set_Point.objects.all()
            serializer = OrdenTrabajoRutaSetPointSerializer(queryset, many=True)
            return serializer.data
