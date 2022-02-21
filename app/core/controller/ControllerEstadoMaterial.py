from ..serializers import EstadoMaterialSerializer
from ..models import Estado_Material


class ControllerEstadoMaterial:
    def crearestadomaterial(request):
        datos = request.data
        try:
            estadoMaterialNuevo = Estado_Material.objects.create(
                estado_material_es = datos['estado_material_es'],  
                estado_material_en  = datos['estado_material_en']        
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_estado_material': estadoMaterialNuevo.estado_material_es}
       
    def listarestadomaterial(id_estado_material=None):
        if id_estado_material:
            try:
                queryset = Estado_Material.objects.get(id_estado_material=id_estado_material)
            except Estado_Material.DoesNotExist:
                return ({'result': 'No se encontró el estado del material deseado'})
            serializer = EstadoMaterialSerializer(queryset)
            return serializer.data
        else:
            queryset = Estado_Material.objects.all()
            serializer = EstadoMaterialSerializer(queryset, many=True)
            return serializer.data
