from ..serializers import ModoDeteccionSerializer
from ..models import Modo_Deteccion


class ControllerModoDeteccion:

    def crearmododeteccion(request):
        datosModoDeteccion = request.data
        modoDeteccionNuevo = Modo_Deteccion()
        try:
           modoDeteccionNuevo.modo_deteccion_en = datosModoDeteccion['modo_deteccion_en']
           modoDeteccionNuevo.modo_deteccion_es = datosModoDeteccion['modo_deteccion_es']
           modoDeteccionNuevo.modo_deteccion_code_en = datosModoDeteccion['modo_deteccion_code_en']
           modoDeteccionNuevo.modo_deteccion_code_es = datosModoDeteccion['modo_deteccion_code_es']

           modoDeteccionNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'modo_deteccion': modoDeteccionNuevo.modo_deteccion_code_es}

    def listarmododeteccion(id_modo_deteccion=None):
        if id_modo_deteccion:
            try:
                queryset = Modo_Deteccion.objects.get(id_modo_deteccion=id_modo_deteccion)
            except Modo_Deteccion.DoesNotExist:
                return ({'result': 'No se encontró el modo de deteccion deseado'})
            serializer = ModoDeteccionSerializer(queryset)
            return serializer.data
        else:
            queryset = Modo_Deteccion.objects.all()
            serializer = ModoDeteccionSerializer(queryset, many=True)
            return serializer.data

    def generarmodosdeteccion(self):

        CE = Modo_Deteccion.objects.create(
           modo_deteccion_en = "Preventive Maintenence",
           modo_deteccion_es = "Mantenimiento Preventivo",
           modo_deteccion_code_en = "PM",
           modo_deteccion_code_es = "MP"
        )
        CE.save()

        CE = Modo_Deteccion.objects.create(
           modo_deteccion_en = "Functional Testing",
           modo_deteccion_es = "Pruebas Funcionales",
           modo_deteccion_code_en = "FS",
           modo_deteccion_code_es = "PF"
        )
        CE.save()

        CE = Modo_Deteccion.objects.create(
           modo_deteccion_en = "Inspection",
           modo_deteccion_es = "Inspección",
           modo_deteccion_code_en = "IN",
           modo_deteccion_code_es = "IN"
        )
        CE.save()

        CE = Modo_Deteccion.objects.create(
           modo_deteccion_en = "Condition Period Monitoring",
           modo_deteccion_es = "Monitoreo Periódico a Condición",
           modo_deteccion_code_en = "CPM",
           modo_deteccion_code_es = "MPC"
        )
        CE.save()

        CE = Modo_Deteccion.objects.create(
           modo_deteccion_en = "Condition Continue Monitoring",
           modo_deteccion_es = "Monitoreo Continuo de Condición",
           modo_deteccion_code_en = "CCM",
           modo_deteccion_code_es = "MCC"
        )
        CE.save()

        CE = Modo_Deteccion.objects.create(
           modo_deteccion_en = "Corrective Maintenance",
           modo_deteccion_es = "Mantenimiento Correctivo",
           modo_deteccion_code_en = "CM",
           modo_deteccion_code_es = "MC"
        )
        CE.save()

        CE = Modo_Deteccion.objects.create(
           modo_deteccion_en = "Observation",
           modo_deteccion_es = "Observación",
           modo_deteccion_code_en = "OB",
           modo_deteccion_code_es = "OB"
        )
        CE.save()

        CE = Modo_Deteccion.objects.create(
           modo_deteccion_en = "Production Interference",
           modo_deteccion_es = "Interferencia con la producción",
           modo_deteccion_code_en = "OP",
           modo_deteccion_code_es = "OP"
        )
        CE.save()

        CE = Modo_Deteccion.objects.create(
           modo_deteccion_en = "Others",
           modo_deteccion_es = "Otros",
           modo_deteccion_code_en = "OTR",
           modo_deteccion_code_es = "OTR"
        )
        CE.save()