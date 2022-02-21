from ..serializers import SuscripcionSerializer  
from ..models import Suscripcion


class ControllerSuscripcion:
    def crearsuscripcion(request):
        datosSuscripcion = request.data
        try:
            suscripcionNuevo = Suscripcion.objects.create(
                nivel = datosSuscripcion['nivel'],
                usuarios  = datosSuscripcion['usuarios']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_suscripcion': suscripcionNuevo.id_suscripcion}
       
    def listarsuscripcion(id_suscripcion=None):
        if id_suscripcion:
            try:
                queryset = Suscripcion.objects.get(id_suscripcion=id_suscripcion)
            except Suscripcion.DoesNotExist:
                return ({'result': 'No se encontró la suscripcion deseada'})
            serializer = SuscripcionSerializer(queryset)
            return serializer.data
        else:
            queryset = Suscripcion.objects.all()
            serializer = SuscripcionSerializer(queryset, many=True)
            return serializer.data
