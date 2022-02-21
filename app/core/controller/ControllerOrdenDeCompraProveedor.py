from ..serializers import OrdenDeCompraProveedorSerializer
from ..models import EstatusUsuario, Orden_De_Compra_Proveedor


class ControllerOrdenDeCompraProveedor:
    def crearordendecompraproveedor(request):
        datos = request.data
        try:
            estatus_proveedor =EstatusUsuario.objects.get(id_estatus = datos['estatus_proveedor'])

            ordenCompraNuevo = Orden_De_Compra_Proveedor.objects.create(
                proveedor = datos['proveedor'], 
                calle  =  datos['calle'], 
                colonia  =  datos['colonia'], 
                cp  =  datos['cp'], 
                municipio  = datos['municipio'], 
                estado  = datos['estado'], 
                pais  = datos['pais'], 
                razon_social  = datos['razon_social'], 
                rfc  = datos['rfc'], 
                telefono  = datos['telefono'], 
                contacto  = datos['contacto'], 
                email  = datos['email'], 
                pagina_web  = datos['pagina_web'], 
                foto_proveedor  = datos['foto_proveedor'], 
                estatus_proveedor =  estatus_proveedor,   
                numero_proveedor  = datos['numero_proveedor'], 
                moneda =  datos['moneda']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_orden_compra_proveedor': ordenCompraNuevo.proveedor}
       
    def listarordendecompraproveedor(id_proveedor=None):
        if id_proveedor:
            try:
                queryset = Orden_De_Compra_Proveedor.objects.get(id_proveedor=id_proveedor)
            except Orden_De_Compra_Proveedor.DoesNotExist:
                return ({'result': 'No se encontró el proveedor de orden de compra deseado'})
            serializer = OrdenDeCompraProveedorSerializer(queryset)
            return serializer.data
        else:
            queryset = Orden_De_Compra_Proveedor.objects.all()
            serializer = OrdenDeCompraProveedorSerializer(queryset, many=True)
            return serializer.data
