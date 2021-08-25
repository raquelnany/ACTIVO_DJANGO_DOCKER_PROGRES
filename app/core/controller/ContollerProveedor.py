from ..serializers import ProveedorSerializer
from ..models import Proveedor, EstatusUsuario

class ControllerProveedor:
    serializer_class = ProveedorSerializer
        
    def crearproveedor(request):
        datosProveedor = request.data
        try:
            estatus = EstatusUsuario.objects.get(id_estatus=datosProveedor['id_estatus_proveedor'])
            print(estatus)
            ProveedorNuevo = Proveedor.objects.create(
                proveedor = datosProveedor['proveedor'],
                calle =  datosProveedor['calle'],
                colonia =  datosProveedor['colonia'],
                cp = datosProveedor['cp'],
                municipio = datosProveedor['municipio'],
                estado = datosProveedor['estado'],
                pais = datosProveedor['pais'],
                razon_social = datosProveedor['razon_social'],
                rfc = datosProveedor['rfc'],
                pagina_web = datosProveedor['pagina_web'],
                foto_proveedor = datosProveedor['foto_proveedor'],
                id_estatus_proveedor = estatus,
                numero_proveedor = datosProveedor['numero_proveedor'],
                moneda = datosProveedor['moneda'],
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_proveedor': ProveedorNuevo.proveedor}

    def listarproveedor(id_proveedor=None):
        if id_proveedor:
            try:
                queryset = Proveedor.objects.get(id_proveedor=id_proveedor)
            except Proveedor.DoesNotExist:
                return ({'result': 'No se encontró el proveedor deseado'})
            serializer = ProveedorSerializer(queryset)
            return serializer.data
        else:
            queryset = Proveedor.objects.all()
            serializer = ProveedorSerializer(queryset, many=True)
            return serializer.data

    def modificarProveedor(request,id_proveedor=None):
        if id_proveedor:
            datosProveedor = request.data
            try:
                proveedorModificar = Proveedor.objects.get(id_proveedor=id_proveedor)
            except Proveedor.DoesNotExist:
                return ({'result': 'No se encontró el proveedor deseado'})
            try:
                
                estatus = EstatusUsuario.objects.get(id_estatus=datosProveedor['id_estatus_proveedor'])
                
                proveedorModificar.proveedor = datosProveedor['proveedor']
                proveedorModificar.calle =  datosProveedor['calle']
                proveedorModificar.colonia =  datosProveedor['colonia']
                proveedorModificar.cp = datosProveedor['cp']
                proveedorModificar.municipio = datosProveedor['municipio']
                proveedorModificar.estado = datosProveedor['estado']
                proveedorModificar.pais = datosProveedor['pais']
                proveedorModificar.razon_social = datosProveedor['razon_social']
                proveedorModificar.rfc = datosProveedor['rfc']
                proveedorModificar.pagina_web = datosProveedor['pagina_web']
                proveedorModificar.foto_proveedor = datosProveedor['foto_proveedor']
                proveedorModificar.id_estatus_proveedor = estatus
                proveedorModificar.numero_proveedor = datosProveedor['numero_proveedor']
                proveedorModificar.moneda = datosProveedor['moneda']
                
                proveedorModificar.save()
                
            except Exception:
                return {"estatus":"Error"}
            return {"estatus":"Ok", 'Proveedor_modificado': proveedorModificar.proveedor}
        else: 
            return {"result":"Ingrese el Id del proveedor que desea modificar"}