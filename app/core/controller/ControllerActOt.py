from ..serializers import ActOtSerializer
from ..models import OT, Act_Ot, Codigo_Falla, Usuario


class ControllerActOt:

    def crearactot(request):
        datosActOt = request.data
        try:
            ot = OT.objects.get(id_ot = datosActOt['ot'])
            codigo_paro_act = Codigo_Falla.objects.get(id_codigo_falla = datosActOt['codigo_paro_act'])
            creador_act_ot = Usuario.objects.get(id_usuario =  datosActOt['creador_act_ot'])

            act_OTNueva = Act_Ot.objects.create(
                ot = ot,
                comentarios_act_ot = datosActOt['comentarios_act_ot'],
                fecha_act_ot = datosActOt['fecha_act_ot'],
                hora_inicio_act = datosActOt['hora_inicio_act'],
                fecha_act_ot_2 = datosActOt['fecha_act_ot_2'],
                hora_inicio_act_2 = datosActOt['hora_inicio_act_2'],
                hora_fin_act =  datosActOt['hora_fin_act'],
                tipo_hora_act = datosActOt['tipo_hora_act'],
                codigo_paro_act = codigo_paro_act,
                creador_act_ot = creador_act_ot,
                tiempo_muerto = datosActOt['ot'],
           )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'act_ot': act_OTNueva.comentarios_act_ot}

    def listaractot(id_act_ot=None):
        if id_act_ot:
            try:
                queryset = Act_Ot.objects.get(id_act_ot=id_act_ot)
            except Act_Ot.DoesNotExist:
                return ({'result': 'No se encontró el Act Ot deseado'})
            serializer = ActOtSerializer(queryset)
            return serializer.data
        else:
            queryset = Act_Ot.objects.all()
            serializer = ActOtSerializer(queryset, many=True)
            return serializer.data