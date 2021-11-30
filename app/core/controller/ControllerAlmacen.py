from ..serializers import AlmacenSerializer
from ..models import Almacen, EstatusUsuario


class ControllerAlmacen:

    def crearalmacen(request):
        datosAlmacen = request.data
        try:
            estatus_almacen = EstatusUsuario.objects.get(id_usuario = datosAlmacen['estatus_almacen'])
            AlmacenNuevo = Almacen.objects.create(
                descripcion_almacen = datosAlmacen['descripcion_almacen'],
                jerarquia_almacen = datosAlmacen['jerarquia_almacen'],
                padre_almacen = datosAlmacen['padre_almacen'],
                foto_almacen = datosAlmacen['foto_almacen'],
                lugar_almacen  = datosAlmacen['lugar_almacen'],
                icono = datosAlmacen['icono'],
                color = datosAlmacen['color'],
                estatus_almacen = estatus_almacen
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'almacen': AlmacenNuevo.descripcion_almacen}

    def listaralmacen(id_almacen=None):
        if id_almacen:
            try:
                queryset = Almacen.objects.get(id_almacen=id_almacen)
            except Almacen.DoesNotExist:
                return ({'result': 'No se encontró el almacen de equipo deseado'})
            serializer = AlmacenSerializer(queryset)
            return serializer.data
        else:
            queryset = Almacen.objects.all()
            serializer = AlmacenSerializer(queryset, many=True)
            return serializer.data