from ..serializers import EmpaqueStockAjusteSerializer
from ..models import Empaque_Stock_Ajuste, Empaque_Stock_Entrada, Proveedor, Usuario


class ControllerEmpaqueStockAjuste:
    def crearempaquestockajuste(request):
        datosEmpaque = request.data
        try:
            empaque_stock_entrada = Empaque_Stock_Entrada.objects.get(id_empaque_stock_entrada = datosEmpaque['empaque_stock_entrada'])
            usuario_ajuste = Usuario.objects.get(id_usuario = datosEmpaque['usuario_ajuste'])
            proveedor_1 = Proveedor.objects.get(id_proveedor = datosEmpaque['proveedor_1'])
            proveedor_2 = Proveedor.objects.get(id_proveedor = datosEmpaque['proveedor_2'])

            empaqueNuevo = Empaque_Stock_Ajuste.objects.create(
                empaque_stock_entrada = empaque_stock_entrada,
                usuario_ajuste = usuario_ajuste,
                fecha_ajuste = datosEmpaque['fecha_ajuste'],
                orden_compra_1 =   datosEmpaque['orden_compra_1'],
                orden_compra_2 =   datosEmpaque['orden_compra_2'],
                proveedor_1 = proveedor_1,
                proveedor_2 = proveedor_2, 
                cantidad_disponible_1 = datosEmpaque['cantidad_disponible_1'],
                cantidad_disponible_2 = datosEmpaque['cantidad_disponible_2'],
                precio_unitario_1 = datosEmpaque['precio_unitario_1'],
                precio_unitario_2 = datosEmpaque['precio_unitario_2'],
                moneda_1 = datosEmpaque['moneda_1'],
                moneda_2 = datosEmpaque['moneda_2'],
                dolares_1 = datosEmpaque['dolares_1'],
                dolares_2 = datosEmpaque['dolares_2']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque_stock_ajuste': empaqueNuevo.id_empaque_stock_ajuste}
       
    def listarempaquestock(id_empaque_stock_ajuste = None):
        if id_empaque_stock_ajuste:
            try:
                queryset = Empaque_Stock_Ajuste.objects.get(id_empaque_stock_ajuste = id_empaque_stock_ajuste)
            except Empaque_Stock_Ajuste.DoesNotExist:
                return ({'result': 'No se encontró el empaque stock ajuste deseado'})
            serializer = EmpaqueStockAjusteSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque_Stock_Ajuste.objects.all()
            serializer = EmpaqueStockAjusteSerializer(queryset, many=True)
            return serializer.data
