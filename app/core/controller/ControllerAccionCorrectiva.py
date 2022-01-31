from ..serializers import AccionCorrectivaSerializer
from ..models import OT, Accion_Correctiva


class ControllerAccionCorrectiva:
    def crearaccioncorrectiva(request):
        datosAccionCorrectiva = request.data
        try:
            ot = OT.objects.get(id_ot  = datosAccionCorrectiva['ot'])
            
            accionCorrectivaNueva = Accion_Correctiva.objects.create(
                ot = ot, 
                comentarios = datosAccionCorrectiva['comentarios']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nueva_accion_correctiva': accionCorrectivaNueva.id_accion_correctiva}
       
    def listaraccioncorrectiva(id_accion_correctiva=None):
        if id_accion_correctiva:
            try:
                queryset = Accion_Correctiva.objects.get(id_accion_correctiva=id_accion_correctiva)
            except Accion_Correctiva.DoesNotExist:
                return ({'result': 'No se encontró la accion correctiva deseada'})
            serializer = AccionCorrectivaSerializer(queryset)
            return serializer.data
        else:
            queryset = Accion_Correctiva.objects.all()
            serializer = AccionCorrectivaSerializer(queryset, many=True)
            return serializer.data
