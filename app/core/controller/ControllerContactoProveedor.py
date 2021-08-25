from ..serializers import  Contacto_ProveedorSerializer
from ..models import Contacto_Proveedor, Proveedor

class ControllerContactoProveedor:
    serializer_class = Contacto_ProveedorSerializer
        
    def crearcontacto_proveedor(request):
        datosContacto_Proveedor = request.data
        try:
            proveedor = Proveedor.objects.get(id_proveedor=datosContacto_Proveedor['proveedor'])
            contactoProveedorNuevo = Contacto_Proveedor.objects.create(
                contacto = datosContacto_Proveedor['contacto'],
                telefono = datosContacto_Proveedor['telefono'],
                email = datosContacto_Proveedor['email'],
                proveedor = proveedor,
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_contacto_para_proveedor: ': contactoProveedorNuevo.proveedor.proveedor}

    def listarcontacto_proveedor(id_contacto_proveedor=None):
        if id_contacto_proveedor:
            try:
                queryset = Contacto_Proveedor.objects.get(id_contacto_proveedor=id_contacto_proveedor)
            except Contacto_Proveedor.DoesNotExist:
                return ({'result': 'No se encontró el contacto del proveedor deseado'})
            serializer = Contacto_ProveedorSerializer(queryset)
            return serializer.data
        else:
            queryset = Contacto_Proveedor.objects.all()
            serializer = Contacto_ProveedorSerializer(queryset, many=True)
            return serializer.data

    def modificarcontacto_proveedor(request,id_contacto_proveedor=None):
        if id_contacto_proveedor:
            datosContactoProveedor = request.data
            try:
                contactoProveedorModificar = Contacto_Proveedor.objects.get(id_contacto_proveedor=id_contacto_proveedor)
            except Proveedor.DoesNotExist:
                return ({'result': 'No se encontró el contacto del proveedor deseado'})
            try:
                
                proveedor = Proveedor.objects.get(id_proveedor=datosContactoProveedor['proveedor'])
                
                contactoProveedorModificar.proveedor = proveedor
                contactoProveedorModificar.contacto = datosContactoProveedor['contacto']
                contactoProveedorModificar.email =  datosContactoProveedor['email']
                contactoProveedorModificar.telefono =  datosContactoProveedor['telefono']
                
                contactoProveedorModificar.save()
                
            except Exception:
                return {"estatus":"Error"}
            return {"estatus":"Ok", 'contacto_modificado_para_proveedor': contactoProveedorModificar.proveedor.proveedor}
        else: 
            return {"result":"Ingrese el Id del contacto del proveedor que desea modificar"}