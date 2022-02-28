from ..serializers import  OcPresupuestoCostosSerializer
from ..models import  Oc_Presupuesto_Costos, Orden_De_Compra_Presupuesto


class ControllerOcPresupuestoCostos:
    def creaocpresupuestocostos(request):
        datosOc = request.data
        try:
            oc_presupuesto = Orden_De_Compra_Presupuesto.objects.get(id = datosOc['oc_presupuesto'])

            ocNuevo = Oc_Presupuesto_Costos.objects.create(
                oc_presupuesto = oc_presupuesto

            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'oc_presupuesto_costos': ocNuevo.id }
       
    def listarocpresupuestocostos(id=None):
        if id:
            try:
                queryset = Oc_Presupuesto_Costos.objects.get(id = id)
            except Oc_Presupuesto_Costos.DoesNotExist:
                return ({'result': 'No se encontró el presupuesto costos de  la oc equipo deseada'})
            serializer = OcPresupuestoCostosSerializer(queryset)
            return serializer.data
        else:
            queryset = Oc_Presupuesto_Costos.objects.all()
            serializer = OcPresupuestoCostosSerializer(queryset, many=True)
            return serializer.data
