from ..serializers import EquipoEstatusSerializer
from ..models import Equipo_Estatus


class ControllerEquipoEstatus:

    def crearequipoestatus(request):
        datosEstatus = request.data
        estatusNuevo = Equipo_Estatus()
        try:
            estatusNuevo.equipo_estatus_en = datosEstatus['equipo_estatus_en']
            estatusNuevo.equipo_estatus_es =datosEstatus['equipo_estatus_es']
        except Exception:
             return {"estatus":"Error"}

        estatusNuevo.save()
        return {"estatus":"Ok", 'estatus': estatusNuevo.equipo_estatus_en}

    def listarequipoestatus(id_equipo_estatus=None):
        if id_equipo_estatus:
            try:
                queryset = Equipo_Estatus.objects.get(id_equipo_estatus=id_equipo_estatus)
            except Equipo_Estatus.DoesNotExist:
                return ({'result': 'No se encontró el estatus deseado'})
            serializer = EquipoEstatusSerializer(queryset)
            return serializer.data
        else:
            queryset = Equipo_Estatus.objects.all()
            serializer = EquipoEstatusSerializer(queryset, many=True)
            return serializer.data

    def generarequipoestatus(request):
        Act = Equipo_Estatus.objects.create(
            equipo_estatus_en = "Active",
            equipo_estatus_es = "Activo",
        )
        Act.save()

        Inact = Equipo_Estatus.objects.create(
            equipo_estatus_en = "Inactive",
            equipo_estatus_es = "Inactivo",
        )
        Inact.save()

        Obs = Equipo_Estatus.objects.create(
            equipo_estatus_en = "Obsolete",
            equipo_estatus_es = "Obsoleto",
        )
        Obs.save()

        Trans = Equipo_Estatus.objects.create(
            equipo_estatus_en = "Transferred",
            equipo_estatus_es = "Transferido",
        )
        Trans.save()

        Scp = Equipo_Estatus.objects.create(
            equipo_estatus_en = "Scrap",
            equipo_estatus_es = "Chatarra",
        )
        Scp.save()

        Ref = Equipo_Estatus.objects.create(
            equipo_estatus_en = "Reference",
            equipo_estatus_es = "Referencia",
        )
        Ref.save()

        Tool = Equipo_Estatus.objects.create(
            equipo_estatus_en = "Tooling",
            equipo_estatus_es = "Herramental",
        )
        Tool.save()