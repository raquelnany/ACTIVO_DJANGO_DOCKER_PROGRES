from ..serializers import EmpaqueSerializer
from ..models import Empaque, Empaque_Categoria, Empaque_Tipo, EstatusUsuario, Orden_Trabajo_Prioridad


class ControllerEmpaque:
    def crearempaque(request):
        datosEmpaque = request.data
        try:
            estatus_empaque = EstatusUsuario.objects.get(id_estatus = datosEmpaque['estatus_empaque'])
            prioridad_empaque = Orden_Trabajo_Prioridad.objects.get(id_orden_trabajo_prioridad = datosEmpaque['prioridad_empaque'])
            empaque_categoria = Empaque_Categoria.objects.get(id_empaque_categoria = datosEmpaque['empaque_categoria'])
            empaque_tipo = Empaque_Tipo.objects.get(id_empaque_tipo = datosEmpaque['empaque_tipo'])

            empaqueNuevo = Empaque.objects.create(
                empaque = datosEmpaque['empaque'],
                descripcion_empaque = datosEmpaque['descripcion_empaque'],
                codigo_empaque = datosEmpaque['codigo_empaque'],
                estatus_empaque= estatus_empaque,
                prioridad_empaque= prioridad_empaque,
                foto_empaque = datosEmpaque['foto_empaque'],
                empaque_categoria = empaque_categoria,
                empaque_tipo = empaque_tipo
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque': empaqueNuevo.empaque}
       
    def listarempaque(id_empaque = None):
        if id_empaque:
            try:
                queryset = Empaque.objects.get(id_empaque = id_empaque)
            except Empaque.DoesNotExist:
                return ({'result': 'No se encontró el empaque deseado'})
            serializer = EmpaqueSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque.objects.all()
            serializer = EmpaqueSerializer(queryset, many=True)
            return serializer.data
