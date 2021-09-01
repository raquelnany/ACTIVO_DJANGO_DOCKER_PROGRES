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



    def generarcategorias(self):
        estatus=EstatusUsuario.objects.get(id_estatus=1)
        GENE=Inventario_Categoria.objects.create(
           inventario_categoria='General',
           inventario_categoria_notas='',
           inventario_categoria_estatus= estatus
        )
        GENE.save()

        GRAS=Inventario_Categoria.objects.create(
           inventario_categoria='Grasas',
           inventario_categoria_notas='',
           inventario_categoria_estatus= estatus
        )
        GRAS.save()

        SEGU=Inventario_Categoria.objects.create(
           inventario_categoria='Seguridad',
           inventario_categoria_notas='',
           inventario_categoria_estatus= estatus
        )
        SEGU.save()

        MAQU=Inventario_Categoria.objects.create(
           inventario_categoria='Maquinado',
           inventario_categoria_notas='',
           inventario_categoria_estatus= estatus
        )
        MAQU.save()

        HERR=Inventario_Categoria.objects.create(
           inventario_categoria='Herramienta',
           inventario_categoria_notas='',
           inventario_categoria_estatus= estatus
        )
        HERR.save()

        ACEI=Inventario_Categoria.objects.create(
           inventario_categoria='Aceite',
           inventario_categoria_notas='Notas de las categorias',
           inventario_categoria_estatus= estatus
        )
        ACEI.save()

        DIEL=Inventario_Categoria.objects.create(
           inventario_categoria='Dielectrico',
           inventario_categoria_notas='',
           inventario_categoria_estatus= estatus
        )
        DIEL.save()

        PEGA=Inventario_Categoria.objects.create(
           inventario_categoria='Pegamentos',
           inventario_categoria_notas='',
           inventario_categoria_estatus= estatus
        )
        PEGA.save()

        BURI=Inventario_Categoria.objects.create(
           inventario_categoria='Buriles',
           inventario_categoria_notas='',
           inventario_categoria_estatus= estatus
        )
        BURI.save()

        INSE=Inventario_Categoria.objects.create(
           inventario_categoria='Insertos',
           inventario_categoria_notas='',
           inventario_categoria_estatus= estatus
        )
        INSE.save()

        PAPE=Inventario_Categoria.objects.create(
           inventario_categoria='Papeleria',
           inventario_categoria_notas='Papeleria para produccion',
           inventario_categoria_estatus= estatus
        )
        PAPE.save()

        FERRE=Inventario_Categoria.objects.create(
           inventario_categoria='Ferreteria',
           inventario_categoria_notas='Articulos de ferreteria',
           inventario_categoria_estatus= estatus
        )
        FERRE.save()

        PINT=Inventario_Categoria.objects.create(
           inventario_categoria='Pinturas',
           inventario_categoria_notas='Pinturas en general',
           inventario_categoria_estatus=estatus
        )
        PINT.save()

        ALCO=Inventario_Categoria.objects.create(
           inventario_categoria='Alcohol',
           inventario_categoria_notas='Alcohol isopropilico',
           inventario_categoria_estatus= estatus
        )
        ALCO.save()

        JABO=Inventario_Categoria.objects.create(
           inventario_categoria='Jabon shampoo',
           inventario_categoria_notas='Jabon shampoo',
           inventario_categoria_estatus= estatus
        )
        JABO.save()

        BATE=Inventario_Categoria.objects.create(
           inventario_categoria='Baterias_Pilas',
           inventario_categoria_notas='Baterias',
           inventario_categoria_estatus= estatus
        )
        BATE.save()

        LIMP=Inventario_Categoria.objects.create(
           inventario_categoria='Limpieza',
           inventario_categoria_notas='Todos los articulos relacionados con la limpieza',
           inventario_categoria_estatus= estatus
        )
        LIMP.save()

        SOLV=Inventario_Categoria.objects.create(
           inventario_categoria='Solventes',
           inventario_categoria_notas='Solventes dielectricos',
           inventario_categoria_estatus= estatus
        )
        SOLV.save()