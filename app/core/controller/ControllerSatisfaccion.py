from ..serializers import SatisfaccionSerializer
from ..models import OT, Satisfaccion, Usuario


class ControllerSatisfaccion:
    def crearsatisfaccion(request):
        datosSatisfaccion = request.data
        try:
            ot = OT.objects.get(id_ot=datosSatisfaccion['ot'])
            requisitor = Usuario.objects.get(id_usuario=datosSatisfaccion['requisitor'])
            user_completo = Usuario.objects.get(id_usuario=datosSatisfaccion['user_completo'])
            
            satisfaccionNuevo = Satisfaccion.objects.create(
                ot =  ot,
                requisitor = requisitor,
                folio = datosSatisfaccion['folio'],
                fecha_completado = datosSatisfaccion['fecha_completado'],
                fecha_satisfaccion = datosSatisfaccion['fecha_satisfaccion'],
                user_completo = user_completo,
                satisfaccion = datosSatisfaccion['satisfaccion'],
                comentarios = datosSatisfaccion['comentarios']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_satisfaccion': satisfaccionNuevo.id_satisfaccion}
       
    def listarsatisfaccion(id_satisfaccion=None):
        if id_satisfaccion:
            try:
                queryset = Satisfaccion.objects.get(id_satisfaccion=id_satisfaccion)
            except Satisfaccion.DoesNotExist:
                return ({'result': 'No se encontró la satisfaccion deseada'})
            serializer = SatisfaccionSerializer(queryset)
            return serializer.data
        else:
            queryset = Satisfaccion.objects.all()
            serializer = SatisfaccionSerializer(queryset, many=True)
            return serializer.data
