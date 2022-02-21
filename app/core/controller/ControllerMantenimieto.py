from ..serializers import MantenimientoSerializer  
from ..models import Equipo, Instalacion, Mantenimiento, Mes


class ControllerMantenimiento:
    def crearmantenimiento(request):
        datosMantenimiento = request.data
        try:
            equipo = Equipo.objects.get(id_equipo = datosMantenimiento['equipo'])
            instalacion = Instalacion.objects.get(id_instalacion = datosMantenimiento['instalacion'])
            mes = Mes.objects.get(id_mes = datosMantenimiento['mes'])
            
            mantenimientoNuevo = Mantenimiento.objects.create(
                equipo = equipo,
                instalacion = instalacion, 
                mes = mes,
                total = datosMantenimiento['total']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_mantenimiento': mantenimientoNuevo.id_mantenimiento}
       
    def listarmantenimiento(id_mantenimiento=None):
        if id_mantenimiento:
            try:
                queryset = Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
            except Mantenimiento.DoesNotExist:
                return ({'result': 'No se encontró el mantenimiento deseado'})
            serializer = MantenimientoSerializer(queryset)
            return serializer.data
        else:
            queryset = Mantenimiento.objects.all()
            serializer = MantenimientoSerializer(queryset, many=True)
            return serializer.data
