from ..serializers import ParteSerializer  
from ..models import OT, Parte, Usuario


class ControllerParte:
    def crearparte(request):
        datosParte = request.data
        try:
            creador = Usuario.objects.get(id_usuario=datosParte['creador'])
            ot = OT.objects.get(id_ot=datosParte['ot'])
            
            parteNuevo = Parte.objects.create(
                ot =  ot,
                creador = creador,
                parte = datosParte['parte'],
                cantidad_sugerida = datosParte['cantidad_sugerida'],
                cantidad_real = datosParte['cantidad_real'],
                costo_individual = datosParte['costo_individual'],
                fecha_parte = datosParte['fecha_parte']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_parte': parteNuevo.parte}
       
    def listarparte(id_parte=None):
        if id_parte:
            try:
                queryset = Parte.objects.get(id_parte=id_parte)
            except Parte.DoesNotExist:
                return ({'result': 'No se encontró la parte deseada'})
            serializer = ParteSerializer(queryset)
            return serializer.data
        else:
            queryset = Parte.objects.all()
            serializer = ParteSerializer(queryset, many=True)
            return serializer.data
