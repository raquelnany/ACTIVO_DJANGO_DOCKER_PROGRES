from ..serializers import ModeloIconoSerializer
from ..models import Modelo_Icono


class ControllerModeloIcono:

    def crearmodeloicono(request):
        datosModeloIcono = request.data
        modeloIconoNuevo = Modelo_Icono()
        try:
           modeloIconoNuevo.modelo_icono_en = datosModeloIcono['modelo_icono_en']
           modeloIconoNuevo.modelo_icono_es = datosModeloIcono['modelo_icono_es']
           modeloIconoNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'modelo_icono': modeloIconoNuevo.modelo_icono_es}

    def listarmodeloicono(id_modelo_icono=None):
        if id_modelo_icono:
            try:
                queryset = Modelo_Icono.objects.get(id_modelo_icono=id_modelo_icono)
            except Modelo_Icono.DoesNotExist:
                return ({'result': 'No se encontró el modelo icono deseado'})
            serializer = ModeloIconoSerializer(queryset)
            return serializer.data
        else:
            queryset = Modelo_Icono.objects.all()
            serializer = ModeloIconoSerializer(queryset, many=True)
            return serializer.data

    def generarmodeloicono(self):

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Sopladores y Ventiladores",
           modelo_icono_en = "Blowers & Fans",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Caldera",
           modelo_icono_en = "Boiler",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Motores de Combustión",
           modelo_icono_en = "Combustion Engines",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Grúa",
           modelo_icono_en = "Crane",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Motor Eléctrico",
           modelo_icono_en = "Electric Motor",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Intercambiador",
           modelo_icono_en = "Exchanger",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Tamiz Filtro",
           modelo_icono_en = "Filter Strainer",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Extintor",
           modelo_icono_en = "Fire Extinguisher",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Convertidor de Frecuencia",
           modelo_icono_en = "Frecuency Converter",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_en = "Equipo General",
           modelo_icono_es = "General Equipment",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Montacargas",
           modelo_icono_en = "Hoist",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Hidrante",
           modelo_icono_en = "Hydrant",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Bombas",
           modelo_icono_en = "Pumps",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Brazo Róbotico",
           modelo_icono_en = "Robot Arm",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Turbinas de vapor",
           modelo_icono_en = "Steam Turbines",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Camión",
           modelo_icono_en = "Truck",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Turbo Expansor",
           modelo_icono_en = "Turbo Espanders",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Válvula",
           modelo_icono_en = "Valve",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Cable de Alimentación",
           modelo_icono_en = "Power Cable",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Fuente de Alimentación",
           modelo_icono_en = "Power Supply",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Subestación",
           modelo_icono_en = "Subesatation",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Tubería",
           modelo_icono_en = "Piping",
        )
        CE.save()

        CE = Modelo_Icono.objects.create(
           modelo_icono_es = "Tanque Torre",
           modelo_icono_en = "Column Tank",
        )
        CE.save()


        
        