from ..serializers import ChkInstruccionSerializer
from ..models import Chk_Aspecto, Chk_Instruccion


class ControllerChkIntruccion:
    def crearchkinstruccion(request):
        datosChecklist = request.data
        try:
            chk_aspecto = Chk_Aspecto.objects.get(id_chk_aspecto =  datosChecklist['chk_aspecto'])

            checklistNuevo = Chk_Instruccion.objects.create(
                chk_aspecto = chk_aspecto,
                chk_instruccion =  datosChecklist['chk_instruccion'],
                chk_opcion =  datosChecklist['chk_opcion'],
                chk_comentarios =  datosChecklist['chk_comentarios'],
                chk_modificacion =  datosChecklist['chk_modificacion'],
                chk_modifico = datosChecklist['chk_modifico']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'chk_instruccion': checklistNuevo.chk_instruccion}
       
    def listarcheckinstruccion(id_chk_instruccion=None):
        if id_chk_instruccion:
            try:
                queryset = Chk_Instruccion.objects.get(id_chk_instruccion=id_chk_instruccion)
            except Chk_Instruccion.DoesNotExist:
                return ({'result': 'No se encontró la instruccion chk deseada'})
            serializer = ChkInstruccionSerializer(queryset)
            return serializer.data
        else:
            queryset = Chk_Instruccion.objects.all()
            serializer = ChkInstruccionSerializer(queryset, many=True)
            return serializer.data
