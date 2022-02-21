from ..serializers import Usuario_Serializer
from ..models import Cliente, Usuario, Usuario_


class ControllerUsuario_:
    def crearusuario_(request):
        datosUsuario_ = request.data
        try:
            cliente = Cliente.objects.get(id_cliente = datosUsuario_['cliente'])
            usuario = Usuario.objects.get(id_usuario = datosUsuario_['usuario'])
            
            usuario_Nuevo = Usuario_.objects.create(
                cliente = cliente,
                usuario  = usuario,
                fecha =  datosUsuario_['fecha'],
                hora = datosUsuario_['hora'],
                alertas = datosUsuario_['alertas'],
                nota_2 = datosUsuario_['nota_2'], 
                nota_3 = datosUsuario_['nota_3'],   
                nota_4 = datosUsuario_['nota_4'],    
                nota_5 = datosUsuario_['nota_5'], 
                nota_6 = datosUsuario_['nota_6'],    
                nota_7 = datosUsuario_['nota_7']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_usuario_': usuario_Nuevo.id_usuario_}
       
    def listarusuario_(id_usuario_=None):
        if id_usuario_:
            try:
                queryset = Usuario_.objects.get(id_usuario_=id_usuario_)
            except Usuario_.DoesNotExist:
                return ({'result': 'No se encontró el usuario_ deseado'})
            serializer = Usuario_Serializer(queryset)
            return serializer.data
        else:
            queryset = Usuario_.objects.all()
            serializer = Usuario_Serializer(queryset, many=True)
            return serializer.data
