from ..serializers import RutaCondicionSerializer
from ..models import Ruta_Condicion


class ControllerRutaCondicion:

    def crearrutacondicion(request):
        datosRuta = request.data
        rutaNuevo = Ruta_Condicion()
        try:
           rutaNuevo.ruta_condicion_en = datosRuta['ruta_condicion_en']
           rutaNuevo.ruta_condicion_es = datosRuta['ruta_condicion_es']
           rutaNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'ruta_condicion': rutaNuevo.ruta_condicion_es}

    def listarrutacondicion(id_ruta_condicion=None):
        if id_ruta_condicion:
            try:
                queryset = Ruta_Condicion.objects.get(id_ruta_condicion=id_ruta_condicion)
            except Ruta_Condicion.DoesNotExist:
                return ({'result': 'No se encontró la condicion de ruta deseada'})
            serializer = RutaCondicionSerializer(queryset)
            return serializer.data
        else:
            queryset = Ruta_Condicion.objects.all()
            serializer = RutaCondicionSerializer(queryset, many=True)
            return serializer.data

    def generarrutacondicion(self):
    
        CE = Ruta_Condicion.objects.create(
           ruta_condicion_en = "Noise",
           ruta_condicion_es = "Ruido",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion_en = "Temperature",
           ruta_condicion_es = "Temperatura",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion_en = "Current",
           ruta_condicion_es = "Corriente",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion_en = "Pressure",
           ruta_condicion_es = "Presion",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion_en = "Wear",
           ruta_condicion_es = "Desgaste",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion_en = "Time",
           ruta_condicion_es = "Tiempo",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion_en = "Distance",
           ruta_condicion_es = "Distancia",
        )
        CE.save()
