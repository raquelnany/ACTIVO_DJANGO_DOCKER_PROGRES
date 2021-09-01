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