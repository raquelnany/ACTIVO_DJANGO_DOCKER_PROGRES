from ..serializers import DashboardmtbfSerializer  
from ..models import Dashboard_Ajuste, Dashboard_Mtbf


class ControllerDashboardMtbf:
    def creardashboardmtbf(request):
        datosDashboarmtbf = request.data
        ajuste = Dashboard_Ajuste.objects.get(id_dashboard_ajuste = datosDashboarmtbf['ajuste'])

        try:
            dashboardMtbfNuevo = Dashboard_Mtbf.objects.create(
                id_mes = datosDashboarmtbf['id_mes'],
                anio = datosDashboarmtbf['anio'],
                ajuste = ajuste
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_dashboard_mtbf': dashboardMtbfNuevo.id_dashboard_mtbf}
       
    def listardashboardmtbf(id_dashboard_mtbf = None):
        if id_dashboard_mtbf:
            try:
                queryset = Dashboard_Mtbf.objects.get(id_dashboard_mtbf = id_dashboard_mtbf)
            except Dashboard_Mtbf.DoesNotExist:
                return ({'result': 'No se encontró el dashboard mtbf deseado'})
            serializer = DashboardmtbfSerializer(queryset)
            return serializer.data
        else:
            queryset = Dashboard_Mtbf.objects.all()
            serializer = DashboardmtbfSerializer(queryset, many=True)
            return serializer.data
