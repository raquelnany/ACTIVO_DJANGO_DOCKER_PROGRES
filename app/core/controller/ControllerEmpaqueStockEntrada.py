from ..serializers import EmpaqueStockEntradaSerializer
from ..models import Empaque_Stock_Entrada, Empaque, Proveedor, Usuario


class ControllerEmpaqueStockEntrada:
    def crearempaquestockentrada(request):
        datosEmpaque = request.data
        try:
            empaque = Empaque.objects.get(id_empaque = datosEmpaque['empaque'])
            proveedor = Proveedor.objects.get(id_proveedor = datosEmpaque['proveedor'])
            user_entrada = Usuario.objects.get(id_usuario = datosEmpaque['user_entrada'])

            empaqueNuevo = Empaque_Stock_Entrada.objects.create(
                empaque = empaque,
                proveedor = proveedor,
                fecha_orden = datosEmpaque['fecha_orden'],
                fecha_recibido = datosEmpaque['fecha_recibido'],
                orden_compra =  datosEmpaque['orden_compra'],
                cantidad_recibida = datosEmpaque['cantidad_recibida'],
                precio_unitario = datosEmpaque['precio_unitario'],
                embargado_a = datosEmpaque['embargado_a'],
                user_entrada = user_entrada,
                cantidad_disponible = datosEmpaque['cantidad_disponible'],
                moneda = datosEmpaque['moneda'],
                dolares = datosEmpaque['dolares']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque_stock_entrada': empaqueNuevo.id_empaque_stock_entrada}
       
    def listarempaquestockentrada(id_empaque_stock_entrada = None):
        if id_empaque_stock_entrada:
            try:
                queryset = Empaque_Stock_Entrada.objects.get(id_empaque_stock_entrada = id_empaque_stock_entrada)
            except Empaque_Stock_Entrada.DoesNotExist:
                return ({'result': 'No se encontró el empaque stock entrada deseado'})
            serializer = EmpaqueStockEntradaSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque_Stock_Entrada.objects.all()
            serializer = EmpaqueStockEntradaSerializer(queryset, many=True)
            return serializer.data
