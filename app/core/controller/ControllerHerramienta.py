from ..serializers import HerramientaSerializer
from ..models import Herramienta, Herramienta_Movimiento, Usuario, EstatusUsuario, Proveedor


class ControllerHerramienta:

    def crearherramienta(request):
        datosHerramienta = request.data
        try:
            herramienta_proveedor = Proveedor.objects.get(id_proveedor = datosHerramienta['herramienta_proveedor'])
            herramienta_usuario = Usuario.objects.get(id_usuario = datosHerramienta['herramienta_usuario'])
            herramienta_estatus = EstatusUsuario.objects.get(id_estatus = datosHerramienta['herramienta_estatus'])
            herramienta_movimiento = Herramienta_Movimiento.objects.get(id_herramienta_movimiento = datosHerramienta['herramienta_movimiento'])

            herramientaNueva = Herramienta.objects.create(
                herramienta= datosHerramienta['herramienta'],
                herramienta_codigo =  datosHerramienta['herramienta_codigo'],
                herramienta_descripcion =  datosHerramienta['herramienta_descripcion'],
                herramienta_marca = datosHerramienta['herramienta_marca'],
                herramienta_modelo =  datosHerramienta['herramienta_modelo'],
                herramienta_num_serie =  datosHerramienta['herramienta_num_serie'],
                herramienta_departamento = datosHerramienta['herramienta_departamento'],
                herramienta_proveedor = herramienta_proveedor,
                herramienta_usuario = herramienta_usuario,
                herramienta_registro = datosHerramienta['herrameinta_registro'],
                herramienta_estatus =herramienta_estatus,
                herramienta_foto = datosHerramienta['herramienta_foto'],
                herramienta_movimiento = herramienta_movimiento,
                herramienta_costo =datosHerramienta['herramienta_costo'],
            )

        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'herramienta_nueva': herramientaNueva.herramienta}

    def listarherramienta(id_herramienta=None):
        if id_herramienta:
            try:
                queryset = Herramienta.objects.get(id_herramienta=id_herramienta)
            except Herramienta.DoesNotExist:
                return ({'result': 'No se encontró la herramienta deseada'})
            serializer = HerramientaSerializer(queryset)
            return serializer.data
        else:
            queryset = Herramienta.objects.all()
            serializer = HerramientaSerializer(queryset, many=True)
            return serializer.data

    def modificarherramienta(request,id_herramienta=None):
        if id_herramienta:
            datosHerramienta = request.data
            try:
                herramientaModificar = Herramienta.objects.get(id_herramienta=id_herramienta)
            except Herramienta.DoesNotExist:
                return ({'result': 'No se encontró la herramienta deseada'})
            try:
               
                herramienta_proveedor = Proveedor.objects.get(id_proveedor = datosHerramienta['herramienta_proveedor'])
                herramienta_usuario = Usuario.objects.get(id_usuario = datosHerramienta['herramienta_usuario'])
                herramienta_estatus = EstatusUsuario.objects.get(id_estatus = datosHerramienta['herramienta_estatus'])
                herramienta_movimiento = Herramienta_Movimiento.objects.get(id_herramienta_movimiento = datosHerramienta['herramienta_movimiento'])

                herramientaModificar.herramienta= datosHerramienta['herramienta']
                herramientaModificar.herramienta_codigo =  datosHerramienta['herramienta_codigo']
                herramientaModificar.herramienta_descripcion =  datosHerramienta['herramienta_descripcion']
                herramientaModificar.herramienta_marca = datosHerramienta['herramienta_marca']
                herramientaModificar.herramienta_modelo =  datosHerramienta['herramienta_modelo']
                herramientaModificar.herramienta_num_serie =  datosHerramienta['herramienta_num_serie']
                herramientaModificar.herramienta_departamento = datosHerramienta['herramienta_departamento']
                herramientaModificar.herramienta_proveedor = herramienta_proveedor
                herramientaModificar.herramienta_usuario = herramienta_usuario
                herramientaModificar.herramienta_registro = datosHerramienta['herrameinta_registro']
                herramientaModificar.herramienta_estatus =herramienta_estatus
                herramientaModificar.herramienta_foto = datosHerramienta['herramienta_foto']
                herramientaModificar.herramienta_movimiento = herramienta_movimiento
                herramientaModificar.herramienta_costo =datosHerramienta['herramienta_costo']
                herramientaModificar.save()
              
            except Exception:
                return {"estatus":"Error"}

            return {"estatus":"Ok", 'herramienta_modificada': herramientaModificar.herramienta}
        else: 
            return {"result":"Ingrese el Id de la herramienta que desea modificar"}