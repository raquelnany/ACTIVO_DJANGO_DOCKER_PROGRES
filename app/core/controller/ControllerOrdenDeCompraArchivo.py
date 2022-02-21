from ..serializers import OrdenDeCompraArchivoSerializer
from ..models import Orden_De_Compra, Orden_De_Compra_Archivo, Orden_De_Compra_Producto, Usuario


class ControllerOrdenDeCompraArchivo:
    def crearordendecompraarchivo(request):
        datos = request.data
        try:
            orden_compra = Orden_De_Compra.objects.get(id = datos['orden_compra'])
            usuario = Usuario.objects.get(id_usuario = datos['usuario'])
            producto_oc = Orden_De_Compra_Producto.objects.get(id = datos['producto_oc'])

            ordenCompraNuevo = Orden_De_Compra_Archivo.objects.create(
                nombre = datos['nombre'],
                archivo = datos['archivo'],
                orden_compra = orden_compra, 
                fecha = datos['fecha'],
                usuario  = usuario,  
                producto_oc = producto_oc  
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_archivo': ordenCompraNuevo.nombre}
       
    def listarordendecompraarchivo(id_orden_compra_archivo=None):
        if id_orden_compra_archivo:
            try:
                queryset = Orden_De_Compra_Archivo.objects.get(id_orden_compra_archivo=id_orden_compra_archivo)
            except Orden_De_Compra_Archivo.DoesNotExist:
                return ({'result': 'No se encontró el archivo de orden de compra deseado'})
            serializer = OrdenDeCompraArchivoSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Archivo.objects.all()
            serializer = OrdenDeCompraArchivoSerializer(queryset, many=True)
            return serializer.data
