from ..serializers import OrdenArchivoSerializer
from ..models import Equipo, Orden_Archivo, Usuario


class ControllerOrdenArchivo:
    def crearordenarchivo(request):
        datosOrdenArchivo = request.data
        try:
            equipo = Equipo.objects.get(id_equipo=datosOrdenArchivo['equipo'])
            usuario = Usuario.objects.get(id_usuario=datosOrdenArchivo['usuario'])

            ordenArchivoNuevo = Orden_Archivo.objects.create(
                nombre_archivo =  datosOrdenArchivo['nombre_archivo'],
                archivo = datosOrdenArchivo['archivo'],
                fecha = datosOrdenArchivo['fecha'],
                comentarios = datosOrdenArchivo['comentarios'],
                equipo = equipo,
                usuario = usuario
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_archivo': ordenArchivoNuevo.nombre_archivo}
       
    def listarordenarchivo(id_orden_archivo=None):
        if id_orden_archivo:
            try:
                queryset = Orden_Archivo.objects.get(id_orden_archivo=id_orden_archivo)
            except Orden_Archivo.DoesNotExist:
                return ({'result': 'No se encontró el orden de archivo deseado'})
            serializer = OrdenArchivoSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_Archivo.objects.all()
            serializer = OrdenArchivoSerializer(queryset, many=True)
            return serializer.data
