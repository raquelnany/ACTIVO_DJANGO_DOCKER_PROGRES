from ..serializers import EmpaqueCategoriaSerializer
from ..models import Empaque_Categoria, EstatusUsuario


class ControllerEmpaqueCategoria:
    def crearempaquecategoria(request):
        datosEmpaque = request.data
        try:
            empaque_categoria_estatus = EstatusUsuario.objects.get(id_estatus = datosEmpaque['estatus_empaque'])

            empaqueNuevo = Empaque_Categoria.objects.create(
                empaque_categoria = datosEmpaque['empaque_categoria'],
                empaque_categoria_estatus = empaque_categoria_estatus,
                empaque_categoria_notas = datosEmpaque['empaque_categoria_notas']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque_categoria': empaqueNuevo.empaque_categoria}
       
    def listarempaquecategoria(id_empaque_categoria = None):
        if id_empaque_categoria:
            try:
                queryset = Empaque_Categoria.objects.get(id_empaque_categoria = id_empaque_categoria)
            except Empaque_Categoria.DoesNotExist:
                return ({'result': 'No se encontró el empaque deseado'})
            serializer = EmpaqueCategoriaSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque_Categoria.objects.all()
            serializer = EmpaqueCategoriaSerializer(queryset, many=True)
            return serializer.data
