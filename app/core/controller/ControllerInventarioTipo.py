from ..serializers import InventarioTipoSerializer
from ..models import Inventario_Tipo

class ControllerInventarioTipo:
    serializer_class = InventarioTipoSerializer
        
    def crearinventarioTipo(request):
        datosInventarioTipo = request.data
        inventarioTipoNuevo = Inventario_Tipo()
        try:
           inventarioTipoNuevo.inventario_tipo_en= datosInventarioTipo['inventario_tipo_en']
           inventarioTipoNuevo.inventario_tipo_es= datosInventarioTipo['inventario_tipo_es']
        except Exception:
             return {"estatus":"Error"}

        inventarioTipoNuevo.save()
        return {"estatus":"Ok", 'nuevo_inventario_tipo': inventarioTipoNuevo.inventario_tipo_es}

    def listarinventariotipo(id_inventario_tipo=None):
        if id_inventario_tipo:
            try:
                queryset = Inventario_Tipo.objects.get(id_inventario_tipo=id_inventario_tipo)
            except Inventario_Tipo.DoesNotExist:
                return ({'result': 'No se encontró el tipo del inventario deseado'})
            serializer = InventarioTipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Inventario_Tipo.objects.all()
            serializer = InventarioTipoSerializer(queryset, many=True)
            return serializer.data

    def generarinventariotipo(self):

        Cons=Inventario_Tipo.objects.create(
           inventario_tipo_en='Consumable',
           inventario_tipo_es='Consumible'
        )
        Cons.save()

        Rep=Inventario_Tipo.objects.create(
           inventario_tipo_en='Repair',
           inventario_tipo_es='Refaccion'
        )
        Rep.save()

        Dir=Inventario_Tipo.objects.create(
           inventario_tipo_en='Direct',
           inventario_tipo_es='Directo'
        )
        Dir.save()

       