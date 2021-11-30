from ..serializers import InventarioAjusteSerializer    
from ..models import Inventario_Ajuste, Inventario, Parte_Estatus, Stock_Entrada, Usuario


class ControllerInventarioAjuste:

    def crearinventarioajuste(request):
        datosinventarioajuste = request.data
        try:
           inventario = Inventario.objects.get(id_inventario = datosinventarioajuste['inventario'])
           stock_entrada = Stock_Entrada.objects.get(id_stock_entrada = datosinventarioajuste['stock_entrada'])
           solicitante = Usuario.objects.get(id_usuario = datosinventarioajuste['solicitante'])
           parte_estatus = Parte_Estatus.objects.get(id_parte_estatus = datosinventarioajuste['parte_estatus'])
           aprobador = Usuario.objects.get(id_usuario = datosinventarioajuste['aprobador'])
           
           InventarioAjusteNuevo = Inventario_Ajuste.objects.create(
                id_inventario_ajuste = datosinventarioajuste['id_inventario_ajuste'],
                nombre_ajuste  = datosinventarioajuste['nombre_ajuste'],
                inventario = inventario,
                stock_entrada = stock_entrada,
                solicitante = solicitante,
                fecha_solicitud  = datosinventarioajuste['fecha_solicitud'],
                fecha_aceptado = datosinventarioajuste['fecha_aceptado'],
                parte_estatus = parte_estatus,
                aprobador = aprobador
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'inventario_ajuste': InventarioAjusteNuevo.nombre_ajuste}

    def listarinventarioajuste(id_inventario_ajuste=None):
        if id_inventario_ajuste:
            try:
                queryset = Inventario_Ajuste.objects.get(id_inventario_ajuste = id_inventario_ajuste)
            except Inventario_Ajuste.DoesNotExist:
                return ({'result': 'No se encontró la ajuste de inventario deseado'})
            serializer = InventarioAjusteSerializer(queryset)
            return serializer.data
        else:
            queryset = Inventario_Ajuste.objects.all()
            serializer = InventarioAjusteSerializer(queryset, many=True)
            return serializer.data