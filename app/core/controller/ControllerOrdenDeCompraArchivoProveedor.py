from ..serializers import OrdenDeCompraArchivoProveedorSerializer
from ..models import Orden_De_Compra, Orden_De_Compra_Archivo_Proveedor, Orden_De_Compra_Proveedor, Usuario


class ControllerOrdenDeCompraArchivoProveedor:
    def crearordendecompraarchivoproveedor(request):
        datos = request.data
        try:
            orden_compra = Orden_De_Compra.objects.get(id = datos['orden_compra'])
            usuario = Usuario.objects.get(id_usuario = datos['usuario'])
            proveedor_oc = Orden_De_Compra_Proveedor.objects.get(id_proveedor = datos['proveedor_oc'])

            ordenCompraNuevo = Orden_De_Compra_Archivo_Proveedor.objects.create(
                nombre = datos['nombre'],
                archivo = datos['archivo'],
                orden_compra = orden_compra, 
                fecha = datos['fecha'],
                usuario  = usuario,  
                proveedor_oc = proveedor_oc  
   
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_archivo_proveedor': ordenCompraNuevo.nombre}
       
    def listarordendecompraarchivo(id_orden_compra_archivo_proveedor=None):
        if id_orden_compra_archivo_proveedor:
            try:
                queryset = Orden_De_Compra_Archivo_Proveedor.objects.get(id_orden_compra_archivo_proveedor=id_orden_compra_archivo_proveedor)
            except Orden_De_Compra_Archivo_Proveedor.DoesNotExist:
                return ({'result': 'No se encontró el archivo de orden de compra deseado'})
            serializer = OrdenDeCompraArchivoProveedorSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Archivo_Proveedor.objects.all()
            serializer = OrdenDeCompraArchivoProveedorSerializer(queryset, many=True)
            return serializer.data
