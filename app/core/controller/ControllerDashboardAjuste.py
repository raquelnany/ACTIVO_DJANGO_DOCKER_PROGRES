from ..serializers import DashboardAjusteSerializer  
from ..models import Dashboard_Ajuste


class ControllerDashboardAjuste:
    def creardashboardajuste(request):
        datosDashboardAjuste = request.data
        try:
            dashboardAjusteNuevo = Dashboard_Ajuste.objects.create(
                dispo_1 = datosDashboardAjuste['dispo_1'],
                dispo_2 = datosDashboardAjuste['dispo_2'],
                dispo_3 = datosDashboardAjuste['dispo_3'],
                proa_1 = datosDashboardAjuste['proa_1'],
                proa_2 = datosDashboardAjuste['proa_2'],
                proa_3 = datosDashboardAjuste['proa_3'],
                cump_1 = datosDashboardAjuste['cump_1'],
                cump_2 = datosDashboardAjuste['cump_2'],
                cump_3 = datosDashboardAjuste['cump_3']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_dashboard_ajuste': dashboardAjusteNuevo.id_dashboard_ajuste}
       
    def listardashboardajuste(id_dashboard_ajuste = None):
        if id_dashboard_ajuste:
            try:
                queryset = Dashboard_Ajuste.objects.get(id_dashboard_ajuste = id_dashboard_ajuste)
            except Dashboard_Ajuste.DoesNotExist:
                return ({'result': 'No se encontró el dashboard ajuste deseado'})
            serializer = DashboardAjusteSerializer(queryset)
            return serializer.data
        else:
            queryset = Dashboard_Ajuste.objects.all()
            serializer = DashboardAjusteSerializer(queryset, many=True)
            return serializer.data
