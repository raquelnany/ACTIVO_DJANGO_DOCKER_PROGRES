from ..serializers import RutaEstatusSerializer
from ..models import Ruta_Estatus


class ControllerRutaEstatus:

    def crearrutaestatus(request):
        datosRuta = request.data
        rutaNuevo = Ruta_Estatus()
        try:
           rutaNuevo.ruta_estatus_es = datosRuta['ruta_estatus_es']
           rutaNuevo.ruta_estatus_en = datosRuta['ruta_estatus_en']
           rutaNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'ruta_status': rutaNuevo.ruta_estatus_es}

    def listarrutaestatus(id_ruta_estatus=None):
        if id_ruta_estatus:
            try:
                queryset = Ruta_Estatus.objects.get(id_ruta_estatus=id_ruta_estatus)
            except Ruta_Estatus.DoesNotExist:
                return ({'result': 'No se encontró el rca status deseado'})
            serializer = RutaEstatusSerializer(queryset)
            return serializer.data
        else:
            queryset = Ruta_Estatus.objects.all()
            serializer = RutaEstatusSerializer(queryset, many=True)
            return serializer.data

    def generarrutaestatus(self):
    
        CE = Ruta_Estatus.objects.create(
           ruta_estatus_en = "Inactive",
           ruta_estatus_es = "Inactiva",
        )
        CE.save()

        CE = Ruta_Estatus.objects.create(
           ruta_estatus_en = "Active",
           ruta_estatus_es = "Activa",
        )
        CE.save()