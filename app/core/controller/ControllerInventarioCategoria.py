from ..serializers import Inventario_CategoriaSerializer
from ..models import Inventario_Categoria, EstatusUsuario

class ControllerInventarioCategoria:
    serializer_class = Inventario_CategoriaSerializer
        
    def crearinventariocategoria(request):
        datosInventarioCategoria = request.data
        try:
            estatus = EstatusUsuario.objects.get(id_estatus=datosInventarioCategoria['inventario_categoria_estatus'])
            InventarioCategoriaNuevo = Inventario_Categoria.objects.create(
                inventario_categoria = datosInventarioCategoria['inventario_categoria'],
                inventario_categoria_notas  = datosInventarioCategoria['inventario_categoria_notas'],
                inventario_categoria_estatus = estatus, 
                
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_inventario_categoria': InventarioCategoriaNuevo.inventario_categoria}

    def listarinventariocategoria(id_inventario_categoria=None):
        if id_inventario_categoria:
            try:
                queryset = Inventario_Categoria.objects.get(id_inventario_categoria=id_inventario_categoria)
            except Inventario_Categoria.DoesNotExist:
                return ({'result': 'No se encontró la categoría del inventario deseada'})
            serializer = Inventario_CategoriaSerializer(queryset)
            return serializer.data
        else:
            queryset = Inventario_Categoria.objects.all()
            serializer = Inventario_CategoriaSerializer(queryset, many=True)
            return serializer.data

    def modificarinventariocategoria(request,id_inventario_categoria=None):
        if id_inventario_categoria:
            datosInventarioCategoria = request.data
            try:
                InventarioCategoriaModificar = Inventario_Categoria.objects.get(id_inventario_categoria=id_inventario_categoria)
            except Inventario_Categoria.DoesNotExist:
                return ({'result': 'No se encontró la categoría del inventario deseada'})
            try:
                
                estatus = EstatusUsuario.objects.get(id_estatus=datosInventarioCategoria['inventario_categoria_estatus'])
                InventarioCategoriaModificar.inventario_categoria = datosInventarioCategoria['inventario_categoria']
                InventarioCategoriaModificar.inventario_categoria_notas = datosInventarioCategoria['inventario_categoria_notas']
                InventarioCategoriaModificar.estatus  = estatus          
                InventarioCategoriaModificar.save()
                
            except Exception:
                return {"estatus":"Error"}
            return {"estatus":"Ok", 'inventario_categoria_modificada': InventarioCategoriaModificar.inventario_categoria}
        else: 
            return {"result":"Ingrese el Id del proveedor que desea modificar"}