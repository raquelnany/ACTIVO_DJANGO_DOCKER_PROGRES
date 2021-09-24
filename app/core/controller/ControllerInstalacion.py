from ..serializers import InstalacionSerializer
from ..models import EstatusUsuario, Instalacion, Instalacion_Icono


class ControllerInstalacion:

    def crearinstalacion(request):
        datosInstalacion = request.data
        try:
           icono = Instalacion_Icono.objects.get(id_instalacion_icono = datosInstalacion['icono'])
           estatus_instalacion = EstatusUsuario.objects.get(id_estatus =datosInstalacion['estatus_instalacion'])

           instalacionNueva = Instalacion.objects.create(
                descripcion_instalacion = datosInstalacion['descripcion_instalacion'],
                jerarquia_instalacion = datosInstalacion['jerarquia_instalacion'],
                padre_instalacion = datosInstalacion['padre_instalacion'],
                foto_instalacion = datosInstalacion['foto_instalacion'],
                lugar_instalacion = datosInstalacion['lugar_instalacion'],
                icono =icono,
                color = datosInstalacion['color'],
                estatus_instalacion = estatus_instalacion,
                horas =datosInstalacion['horas'],
                operadores = datosInstalacion['operadores'],
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nueva_instalacion': instalacionNueva.descripcion_instalacion}

    def listarinstalacion(id_instalacion=None):
        if id_instalacion:
            try:
                queryset = Instalacion.objects.get(id_instalacion=id_instalacion)
            except Instalacion.DoesNotExist:
                return ({'result': 'No se encontró la instalación deseada'})
            serializer = InstalacionSerializer(queryset)
            return serializer.data
        else:
            queryset = Instalacion.objects.all()
            serializer = InstalacionSerializer(queryset, many=True)
            return serializer.data

    def modificarinstalacion(request,id_instalacion=None):
        if id_instalacion:
            datosInstalacion = request.data
            try:
                instalacionModificar = Instalacion.objects.get(id_instalacion=id_instalacion)
            except Instalacion.DoesNotExist:
                return ({'result': 'No se encontró la instalación deseada'})
            try:
                
                estatus_instalacion = EstatusUsuario.objects.get(id_estatus=datosInstalacion['estatus'])
                icono = Instalacion_Icono.objects.get(id_instalacion_icono = datosInstalacion['icono'] )
                
                instalacionModificar.descripcion_instalacion = datosInstalacion['descripcion_instalacion']
                instalacionModificar.jerarquia_instalacion = datosInstalacion['jerarquia_instalacion']
                instalacionModificar.padre_instalacion = datosInstalacion['padre_instalacion']
                instalacionModificar.foto_instalacion = datosInstalacion['foto_instalacion']
                instalacionModificar.lugar_instalacion = datosInstalacion['lugar_instalacion']
                instalacionModificar.icono =icono
                instalacionModificar.color = datosInstalacion['color']
                instalacionModificar.estatus_instalacion = estatus_instalacion
                instalacionModificar.horas =datosInstalacion['horas']
                instalacionModificar.operadores = datosInstalacion['operadores']
                
                instalacionModificar.save()
                
            except Exception:
                return {"estatus":"Error"}
            return {"estatus":"Ok", 'Instalación_modificada': instalacionModificar.descripcion_instalacion}
        else: 
            return {"result":"Ingrese el Id de la instalación que desea modificar"}