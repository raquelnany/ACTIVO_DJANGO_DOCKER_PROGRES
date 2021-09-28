from ..serializers import HerramientaMovimientoSerializer
from ..models import Herramienta_Movimiento


class ControllerHerramientaMovimiento:

    def crearherramientamovimiento(request):
        datosHerramientaMovimiento = request.data
        herramientaMovimientoNuevo = Herramienta_Movimiento()
        try:
            herramientaMovimientoNuevo.herramienta_movimiento_en = datosHerramientaMovimiento['herramienta_movimiento_en']
            herramientaMovimientoNuevo.herramienta_movimiento_en_es = datosHerramientaMovimiento['herramienta_movimiento_en_es']
        except Exception:
             return {"estatus":"Error"}

        herramientaMovimientoNuevo.save()
        return {"estatus":"Ok", 'herramienta_movimiento_nueva': herramientaMovimientoNuevo.herramienta_movimiento_en}

    def listarherramientamovimiento(id_herramienta_movimiento=None):
        if id_herramienta_movimiento:
            try:
                queryset = Herramienta_Movimiento.objects.get(id_herramienta_movimiento=id_herramienta_movimiento)
            except Herramienta_Movimiento.DoesNotExist:
                return ({'result': 'No se encontró el movimiento de herramienta deseado'})
            serializer = HerramientaMovimientoSerializer(queryset)
            return serializer.data
        else:
            queryset = Herramienta_Movimiento.objects.all()
            serializer = HerramientaMovimientoSerializer(queryset, many=True)
            return serializer.data

    def generarherramientamovimiento(request):

        Ava = Herramienta_Movimiento.objects.create(
            herramienta_movimiento_es = "Disponible",
            herramienta_movimiento_en = "Available",
        )
        Ava.save()

        Req = Herramienta_Movimiento.objects.create(
            herramienta_movimiento_es = "Solicitado",
            herramienta_movimiento_en = "Request",
        )
        Req.save()

        Can = Herramienta_Movimiento.objects.create(
            herramienta_movimiento_es = "Cancelado",
            herramienta_movimiento_en = "Canceled",
        )
        Can.save()

        Rej = Herramienta_Movimiento.objects.create(
            herramienta_movimiento_es = "Rechazado",
            herramienta_movimiento_en = "Rejected",
        )
        Rej.save()

        Inu = Herramienta_Movimiento.objects.create(
            herramienta_movimiento_es = "En Uso",
            herramienta_movimiento_en = "In use",
        )
        Inu.save()

        Ent = Herramienta_Movimiento.objects.create(
            herramienta_movimiento_es = "Entregado",
            herramienta_movimiento_en = "Delivered",
        )
        Ent.save()