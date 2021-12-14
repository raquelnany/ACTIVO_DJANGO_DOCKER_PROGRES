from ..serializers import OrdenArchivosSerializer
from ..models import Orden_Archivos, Usuario


class ControllerOrdenArchivos:

    def crearordenarchivos(request):
        datosOrdenArchivos = request.data
        try:
           usuario = Usuario.objects.get(id_usuario = datosOrdenArchivos['usuario']) 

           ordenArchivosNuevo = Orden_Archivos.objects.create(
                nombre_archivo = datosOrdenArchivos['nombre_archivo'],
                archivo = datosOrdenArchivos['archivo'],
                fecha = datosOrdenArchivos['fecha'],
                comentarios = datosOrdenArchivos['comentarios'],
                id_orden = datosOrdenArchivos['id_orden'],
                usuario = usuario
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'orden_archivos': ordenArchivosNuevo.nombre_archivo}

    def listarordenarchivos(id_orden_archivos=None):
        if id_orden_archivos:
            try:
                queryset = Orden_Archivos.objects.get(id_orden_archivos=id_orden_archivos)
            except Orden_Archivos.DoesNotExist:
                return ({'result': 'No se encontró el orden de archivos deseado'})
            serializer = OrdenArchivosSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Archivos.objects.all()
            serializer = OrdenArchivosSerializer(queryset, many=True)
            return serializer.data