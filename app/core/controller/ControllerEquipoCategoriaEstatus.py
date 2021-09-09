from ..serializers import EquipoCategoriaEstatusSerializaer
from ..models import Equipo_Categoria_Estatus


class ControllerEquipoCategiriaEstatus:
    def crearequipocategoriaestatus(request):
        datosEstatus = request.data
        estatusNuevo = Equipo_Categoria_Estatus()
        try:
            estatusNuevo.equipo_categoria_estatus_en = datosEstatus['equipo_categoria_estatus_en']
            estatusNuevo.equipo_categoria_estatus_es = datosEstatus['equipo_categoria_estatus_es']
        except Exception:
             return {"estatus":"Error"}

        estatusNuevo.save()
        return {"estatus":"Ok", 'equipo_categoria_estatus': estatusNuevo.equipo_categoria_estatus_es}

    def listarequipocategoriaestatus(id_equipo_categoria_estatus=None):
        if id_equipo_categoria_estatus:
            try:
                queryset = Equipo_Categoria_Estatus.objects.get(id_equipo_categoria_estatus=id_equipo_categoria_estatus)
            except Equipo_Categoria_Estatus.DoesNotExist:
                return ({'result': 'No se encontró el estatus deseado'})
            serializer = EquipoCategoriaEstatusSerializaer(queryset)
            return serializer.data
        else:
            queryset = Equipo_Categoria_Estatus.objects.all()
            serializer = EquipoCategoriaEstatusSerializaer(queryset, many=True)
            return serializer.data

    def generarequipocategoriaestatus(self):
        inactivo=Equipo_Categoria_Estatus.objects.create(
           equipo_categoria_estatus_en='Inactive',
           equipo_categoria_estatus_es='Inactivo'
        )
        inactivo.save()

        activo=Equipo_Categoria_Estatus.objects.create(
           equipo_categoria_estatus_en='Active',
           equipo_categoria_estatus_es='Activo'
        )
        activo.save()

        reactivo=Equipo_Categoria_Estatus.objects.create(
           equipo_categoria_estatus_en='Re-active',
           equipo_categoria_estatus_es='Re-activar'
        )
        reactivo.save()
