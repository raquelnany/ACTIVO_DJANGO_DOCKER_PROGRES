from ..serializers import InventarioValeSerializer  
from ..models import Equipo, Instalacion, Inventario_Vale, Inventario, Parte_Estatus, Usuario


class ControllerInventarioVale:
    def crearinventariovale(request):
        datosInventarioVale= request.data
        try:
        
            inventario = Inventario.objects.get(id_inventario =  datosInventarioVale['inventario'])
            instalacion = Instalacion.objects.get(id_instalacion =  datosInventarioVale['instalacion'])
            solicitante = Usuario.objects.get(id_usuario =  datosInventarioVale['solicitante'])
            parte_estatus = Parte_Estatus.objects.get(id_parte_estatus =  datosInventarioVale['parte_estatus'])
            equipo = Equipo.objects.get(id_equipo =  datosInventarioVale['equipo'])

            inventarioValeNuevo = Inventario_Vale.objects.create(
                nombre_vale  = datosInventarioVale['nombre_vale'],
                inventario = inventario,
                instalacion = instalacion,
                solicitante = solicitante,
                cantidad_solicitada =datosInventarioVale['cantidad_solicitada'],
                cantidad_surtida = datosInventarioVale['cantidad_surtida'],
                parte_estatus = parte_estatus,
                fecha_surtido = datosInventarioVale['fecha_surtido'],
                fecha_solicitud  = datosInventarioVale['fecha_solicitud'],
                equipo = equipo
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'inventario_vale': inventarioValeNuevo.nombre_vale}
       
    def listarinventariovale(id_inventario_vale=None):
        if id_inventario_vale:
            try:
                queryset = Inventario_Vale.objects.get(id_inventario_vale=id_inventario_vale)
            except Inventario_Vale.DoesNotExist:
                return ({'result': 'No se encontró el vale de inventario deseado'})
            serializer = InventarioValeSerializer(queryset)
            return serializer.data
        else:
            queryset = Inventario_Vale.objects.all()
            serializer = InventarioValeSerializer(queryset, many=True)
            return serializer.data
