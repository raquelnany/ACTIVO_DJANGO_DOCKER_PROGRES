from ..serializers import RutaCondicionUnidadSerializer
from ..models import Ruta_Condicion_Unidad, Ruta_Condicion


class ControllerRutaCondicionUnidad:

    def crearrutacondicionunidad(request):
        datosRutaCondicionUnidad = request.data
        try:
            ruta_condicion = Ruta_Condicion.objects.get(id_ruta_condicion = datosRutaCondicionUnidad['ruta_condicion'])
            
            rutaCondicionUnidadNueva = Ruta_Condicion_Unidad.objects.create(
                ruta_condicion = ruta_condicion,
                ruta_condicion_unidad_en = datosRutaCondicionUnidad['ruta_condicion_unidad_en'],
                ruta_condicion_unidad_es = datosRutaCondicionUnidad['ruta_condicion_unidad_es']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'ruta_unidad_condicion_unidad': rutaCondicionUnidadNueva.ruta_condicion_unidad_en}

    def listarrutacondicionunidad(id_ruta_condicion_unidad=None):
        if id_ruta_condicion_unidad:
            try:
                queryset = Ruta_Condicion_Unidad.objects.get(id_almaid_ruta_condicion_unidadcen=id_ruta_condicion_unidad)
            except Ruta_Condicion_Unidad.DoesNotExist:
                return ({'result': 'No se encontró la ruta condicion unidad deseada'})
            serializer = RutaCondicionUnidadSerializer(queryset)
            return serializer.data
        else:
            queryset = Ruta_Condicion_Unidad.objects.all()
            serializer = RutaCondicionUnidadSerializer(queryset, many=True)
            return serializer.data

    def generarrutacondicion(self):
        
        ruido = Ruta_Condicion.objects.get(id_ruta_condicion = 1)
        temperatura = Ruta_Condicion.objects.get(id_ruta_condicion = 2)
        corriente = Ruta_Condicion.objects.get(id_ruta_condicion = 3)
        presion = Ruta_Condicion.objects.get(id_ruta_condicion = 4)
        desgaste = Ruta_Condicion.objects.get(id_ruta_condicion = 5)
        tiempo = Ruta_Condicion.objects.get(id_ruta_condicion = 6)
        distancia = Ruta_Condicion.objects.get(id_ruta_condicion =7)

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = temperatura,
           ruta_condicion_unidad_es = "°F",
           ruta_condicion_unidad_en = "°F",
        )
        CE.save()
        
        CE = Ruta_Condicion.objects.create(
           ruta_condicion = temperatura,
           ruta_condicion_unidad_es = "°C",
           ruta_condicion_unidad_en = "°C",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = corriente,
           ruta_condicion_unidad_es = "Amps",
           ruta_condicion_unidad_en = "Amps",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = presion,
           ruta_condicion_unidad_es = "Pa",
           ruta_condicion_unidad_en = "Pa",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = presion,
           ruta_condicion_unidad_es = "Bar",
           ruta_condicion_unidad_en = "Bar",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = presion,
           ruta_condicion_unidad_es = "Psi",
           ruta_condicion_unidad_en = "Psi",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = presion,
           ruta_condicion_unidad_es = "Kg/cm2",
           ruta_condicion_unidad_en = "Kg/cm2",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = desgaste,
           ruta_condicion_unidad_es = "Pulg/In",
           ruta_condicion_unidad_en = "Pulg/In",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = desgaste,
           ruta_condicion_unidad_es = "%",
           ruta_condicion_unidad_en = "%",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = desgaste,
           ruta_condicion_unidad_es = "CM",
           ruta_condicion_unidad_en = "CM",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = ruido,
           ruta_condicion_unidad_es = "DBs",
           ruta_condicion_unidad_en = "DBs",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = tiempo,
           ruta_condicion_unidad_es = "Horas",
           ruta_condicion_unidad_en = "Hours",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = tiempo,
           ruta_condicion_unidad_es = "Dias",
           ruta_condicion_unidad_en = "Days",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = tiempo,
           ruta_condicion_unidad_es = "Minutos",
           ruta_condicion_unidad_en = "Minutes",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = distancia,
           ruta_condicion_unidad_es = "KM",
           ruta_condicion_unidad_en = "KM",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = distancia,
           ruta_condicion_unidad_es = "Millas",
           ruta_condicion_unidad_en = "Miles",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = distancia,
           ruta_condicion_unidad_es = "Yardas",
           ruta_condicion_unidad_en = "Yards",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = distancia,
           ruta_condicion_unidad_es = "Metros",
           ruta_condicion_unidad_en = "Meters",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = distancia,
           ruta_condicion_unidad_es = "CM",
           ruta_condicion_unidad_en = "CM",
        )
        CE.save()

        CE = Ruta_Condicion.objects.create(
           ruta_condicion = distancia,
           ruta_condicion_unidad_es = "Pulgadas",
           ruta_condicion_unidad_en = "Inches",
        )
        CE.save()

