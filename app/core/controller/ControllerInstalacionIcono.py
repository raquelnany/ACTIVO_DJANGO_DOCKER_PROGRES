from ..serializers import InstalacionIconoSerializer
from ..models import Instalacion_Icono


class ControllerInstalacionIcono:

    def crearinstalacionicono(request):
        datosInstalacionIcono = request.data
        instalacionIconoNuevo = Instalacion_Icono()
        try:
           instalacionIconoNuevo.instalacion_icono_en = datosInstalacionIcono['instalacion_icono_en']
           instalacionIconoNuevo.instalacion_icono_es = datosInstalacionIcono['instalacion_icono_es']
           instalacionIconoNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'instalacion_icono': instalacionIconoNuevo.instalacion_icono_es}

    def listarinstalacionicono(id_instalacion_icono=None):
        if id_instalacion_icono:
            try:
                queryset = Instalacion_Icono.objects.get(id_instalacion_icono=id_instalacion_icono)
            except Instalacion_Icono.DoesNotExist:
                return ({'result': 'No se encontró la instalación icono deseada'})
            serializer = InstalacionIconoSerializer(queryset)
            return serializer.data
        else:
            queryset = Instalacion_Icono.objects.all()
            serializer = InstalacionIconoSerializer(queryset, many=True)
            return serializer.data

    def generarinstalacionicono(self):
        IL = Instalacion_Icono.objects.create(
            instalacion_icono_en = "Industrial Location",
            instalacion_icono_es = "Industrial Location",
        )
        IL.save()

        PL = Instalacion_Icono.objects.create(
            instalacion_icono_en = "Production Line",
            instalacion_icono_es = "Production Line",
        )
        PL.save()