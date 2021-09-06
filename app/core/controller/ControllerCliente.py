from ..serializers import ClienteSerializer
from ..models import Cliente

class ControllerCliente:
    serializer_class = ClienteSerializer
        
    def crearcliente(request):
        datosCliente= request.data
        try:
            ClienteNuevo = Cliente()
            ClienteNuevo.cliente = datosCliente['cliente']
            ClienteNuevo.calle =  datosCliente['calle']
            ClienteNuevo.colonia =  datosCliente['colonia']
            ClienteNuevo.cp = datosCliente['cp']
            ClienteNuevo.municipio = datosCliente['municipio']
            ClienteNuevo.estado = datosCliente['estado']
            ClienteNuevo.pais = datosCliente['pais']
            ClienteNuevo.razon_social = datosCliente['razon_social']
            ClienteNuevo.rfc = datosCliente['rfc']
            ClienteNuevo.telefono = datosCliente['telefono']
            ClienteNuevo.contacto = datosCliente['contacto']
            ClienteNuevo.email = datosCliente['email']
            ClienteNuevo.pagina_web = datosCliente['pagina_web']
            ClienteNuevo.foto_cliente = datosCliente['foto_cliente']
            ClienteNuevo.id_zona_horaria = datosCliente['id_zona_horaria']
            ClienteNuevo.usar_inventario = datosCliente['usar_inventario']
            ClienteNuevo.alertas_email = datosCliente['alertas_email']
            ClienteNuevo.registro = datosCliente['registro']
            ClienteNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_cliente': ClienteNuevo.cliente}

    def listarcliente(id_cliente=None):
        if id_cliente:
            try:
                queryset = Cliente.objects.get(id_cliente=id_cliente)
            except Cliente.DoesNotExist:
                return ({'result': 'No se encontró el cliente deseado'})
            serializer = ClienteSerializer(queryset)
            return serializer.data
        else:
            queryset = Cliente.objects.all()
            serializer = ClienteSerializer(queryset, many=True)
            return serializer.data

    def modificarcliente(request,id_cliente=None):
        if id_cliente:
            datosCliente = request.data
            try:
                clienteModificar = Cliente.objects.get(id_cliente=id_cliente)
            except Cliente.DoesNotExist:
                return ({'result': 'No se encontró el cliente deseado'})
            try:
                clienteModificar.cliente = datosCliente['cliente']
                clienteModificar.calle =  datosCliente['calle']
                clienteModificar.colonia =  datosCliente['colonia']
                clienteModificar.cp = datosCliente['cp']
                clienteModificar.municipio = datosCliente['municipio']
                clienteModificar.estado = datosCliente['estado']
                clienteModificar.pais = datosCliente['pais']
                clienteModificar.razon_social = datosCliente['razon_social']
                clienteModificar.rfc = datosCliente['rfc']
                clienteModificar.telefono = datosCliente['telefono']
                clienteModificar.contacto = datosCliente['contacto']
                clienteModificar.email = datosCliente['email']
                clienteModificar.pagina_web = datosCliente['pagina_web']
                clienteModificar.foto_cliente = datosCliente['foto_cliente']
                clienteModificar.id_zona_horaria = datosCliente['id_zona_horaria']
                clienteModificar.usar_inventario = datosCliente['usar_inventario']
                clienteModificar.alertas_email = datosCliente['alertas_email']
                clienteModificar.registro = datosCliente['registro']
                clienteModificar.save()
                
                clienteModificar.save()
                
            except Exception:
                return {"estatus":"Error"}
            return {"estatus":"Ok", 'cliente_modificado': clienteModificar.cliente}
        else: 
            return {"result":"Ingrese el Id del cliente que desea modificar"}