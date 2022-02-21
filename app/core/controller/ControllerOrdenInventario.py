from ..serializers import OrdenInventarioSerializer
from ..models import Inventario, Orden_Inventario, Usuario


class ControllerOrdenInventario:
    def crearordeninventario(request):
        datosOrdenArchivo = request.data
        try:
            inventario = Inventario.objects.get(id_inventario=datosOrdenArchivo['inventario'])
            usuario = Usuario.objects.get(id_usuario=datosOrdenArchivo['usuario'])

            ordenArchivoNuevo = Orden_Inventario.objects.create(
                nombre_archivo =  datosOrdenArchivo['nombre_archivo'],
                archivo = datosOrdenArchivo['archivo'],
                fecha = datosOrdenArchivo['fecha'],
                comentarios = datosOrdenArchivo['comentarios'],
                inventario = inventario,
                usuario = usuario
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_inventario': ordenArchivoNuevo.nombre_archivo}
       
    def listarordeninventario(id_orden_inventario=None):
        if id_orden_inventario:
            try:
                queryset = Orden_Inventario.objects.get(id_orden_inventario=id_orden_inventario)
            except Orden_Inventario.DoesNotExist:
                return ({'result': 'No se encontró el orden de inventario deseado'})
            serializer = OrdenInventarioSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Inventario.objects.all()
            serializer = OrdenInventarioSerializer(queryset, many=True)
            return serializer.data
