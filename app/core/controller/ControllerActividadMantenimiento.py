from ..serializers import ActividadMantenimientoSerializer
from ..models import Actividad_Mantenimiento


class ControllerActividadMantenimiento:

    def crearactividadmantenimiento(request):
        datosActividadMantenimieto = request.data
        actividadMantenimientoNuevo = Actividad_Mantenimiento()
        try:
           actividadMantenimientoNuevo.actividad_mantenimiento_en = datosActividadMantenimieto['actividad_mantenimiento_en']
           actividadMantenimientoNuevo.actividad_mantenimiento_es = datosActividadMantenimieto['actividad_mantenimiento_es']
           actividadMantenimientoNuevo.actividad_mantenimiento_code = datosActividadMantenimieto['actividad_mantenimiento_code']

           actividadMantenimientoNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'actividad_mantenimiento': actividadMantenimientoNuevo.actividad_mantenimiento_en}

    def listaractividadmantenimiento(id_actividad_mantenimiento=None):
        if id_actividad_mantenimiento:
            try:
                queryset = Actividad_Mantenimiento.objects.get(id_actividad_mantenimiento=id_actividad_mantenimiento)
            except Actividad_Mantenimiento.DoesNotExist:
                return ({'result': 'No se encontró el modo de deteccion deseado'})
            serializer = ActividadMantenimientoSerializer(queryset)
            return serializer.data
        else:
            queryset = Actividad_Mantenimiento.objects.all()
            serializer = ActividadMantenimientoSerializer(queryset, many=True)
            return serializer.data

    def generaractividadesmantenimiento(self):

        CE = Actividad_Mantenimiento.objects.create(
           actividad_mantenimiento_en = "Replacement",
           actividad_mantenimiento_es = "Reemplazar",
           actividad_mantenimiento_code = "RPC"
        )
        CE.save()

        CE = Actividad_Mantenimiento.objects.create(
           actividad_mantenimiento_en = "Repair",
           actividad_mantenimiento_es = "Reparar",
           actividad_mantenimiento_code = "RPR"
        )
        CE.save()

        CE = Actividad_Mantenimiento.objects.create(
           actividad_mantenimiento_en = "Modify",
           actividad_mantenimiento_es = "Modificar",
           actividad_mantenimiento_code = "MDF"
        )
        CE.save()

        CE = Actividad_Mantenimiento.objects.create(
           actividad_mantenimiento_en = "Adjusment",
           actividad_mantenimiento_es = "Ajustar",
           actividad_mantenimiento_code = "AJS"
        )
        CE.save()

        CE = Actividad_Mantenimiento.objects.create(
           actividad_mantenimiento_en = "Check Up",
           actividad_mantenimiento_es = "Verificar",
           actividad_mantenimiento_code = "CHK"
        )
        CE.save()

        CE = Actividad_Mantenimiento.objects.create(
           actividad_mantenimiento_en = "Service",
           actividad_mantenimiento_es = "Servicio",
           actividad_mantenimiento_code = "SER"
        )
        CE.save()

        CE = Actividad_Mantenimiento.objects.create(
           actividad_mantenimiento_en = "Inspection",
           actividad_mantenimiento_es = "Inspeccionar",
           actividad_mantenimiento_code = "INS"
        )
        CE.save()

        CE = Actividad_Mantenimiento.objects.create(
           actividad_mantenimiento_en = "Reaconditioning",
           actividad_mantenimiento_es = "Reacondicionamiento",
           actividad_mantenimiento_code = "RCN"
        )
        CE.save()

        CE = Actividad_Mantenimiento.objects.create(
           actividad_mantenimiento_en = "Other",
           actividad_mantenimiento_es = "Otro",
           actividad_mantenimiento_code = "OTR"
        )
        CE.save()

        
