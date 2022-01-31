from ..serializers import EmpaqueValeSerializer
from ..models import Empaque_Vale, Empaque, Instalacion, Usuario, Parte_Estatus


class ControllerEmpaqueVale:
    def crearempaquevale(request):
        datosEmpaque = request.data
        try:
            empaque = Empaque.objects.get(id_empaque = datosEmpaque['empaque'])
            instalacion = Instalacion.objects.get(id_instalacion = datosEmpaque['instalacion'])
            solicitante = Usuario.objects.get(id_usuario = datosEmpaque['solicitante'])
            parte_estatus = Parte_Estatus.objects.get(id_parte_estatus = datosEmpaque['parte_estatus'])

            empaqueNuevo = Empaque_Vale.objects.create(
                nombre_empaque =  datosEmpaque['nombre_empaque'],
                empaque = empaque,
                instalacion = instalacion,
                solicitante = solicitante,
                cantidad_solicitada = datosEmpaque['cantidad_solicitada'],
                cantidad_surtida = datosEmpaque['cantidad_surtida'],
                parte_estatus = parte_estatus,
                fecha_surtido = datosEmpaque['fecha_surtido'],
                fecha_solicitado = datosEmpaque['fecha_solicitado']
                
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque_vale': empaqueNuevo.nombre_empaque}
       
    def listarempaquevale(id_empaque_vale = None):
        if id_empaque_vale:
            try:
                queryset = Empaque_Vale.objects.get(id_empaque_vale = id_empaque_vale)
            except Empaque_Vale.DoesNotExist:
                return ({'result': 'No se encontró el empaque vale deseado'})
            serializer = EmpaqueValeSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque_Vale.objects.all()
            serializer = EmpaqueValeSerializer(queryset, many=True)
            return serializer.data
