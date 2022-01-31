from ..serializers import EmpaqueTipoSerializer
from ..models import Empaque_Tipo


class ControllerEmpaqueTipo:
    def crearempaquetipo(request):
        datosEmpaque = request.data
        try:
           empaqueNuevo = Empaque_Tipo.objects.create(         
                empaque_tipo_es = datosEmpaque['empaque_tipo_es'],
                empaque_tipo_en = datosEmpaque['empaque_tipo_en']
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_empaque': empaqueNuevo.empaque_tipo_es}
       
    def listarempaquetipo(id_empaque_tipo = None):
        if id_empaque_tipo:
            try:
                queryset = Empaque_Tipo.objects.get(id_empaque_tipo = id_empaque_tipo)
            except Empaque_Tipo.DoesNotExist:
                return ({'result': 'No se encontró el empaque tipo deseado'})
            serializer = EmpaqueTipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Empaque_Tipo.objects.all()
            serializer = EmpaqueTipoSerializer(queryset, many=True)
            return serializer.data
