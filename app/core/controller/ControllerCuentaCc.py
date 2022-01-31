from ..serializers import CuentaCcSerializer
from ..models import CentroCosto, Cuenta_Cc

class ControllerCuentaCc:
    def crearcuentacc(request):
        datosCuentaCc = request.data
        try:
            centro_costos = CentroCosto.objects.get(id_centro_costo = datosCuentaCc['centro_costos'])
            
            cuentaCcNuevo = Cuenta_Cc.objects.create(
                centro_costos = centro_costos,
                cuenta_cc = datosCuentaCc['cuenta_cc'],
                descripcion_cuenta_cc = datosCuentaCc['descripcion_cuenta_cc']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nueva_cuenta_cc': cuentaCcNuevo.cuenta_cc}
       
    def listarcuentacc(id_cuenta_cc=None):
        if id_cuenta_cc:
            try:
                queryset = Cuenta_Cc.objects.get(id_cuenta_cc = id_cuenta_cc)
            except Cuenta_Cc.DoesNotExist:
                return ({'result': 'No se encontró la cuenta cc deseada'})
            serializer = CuentaCcSerializer(queryset)
            return serializer.data
        else:
            queryset = Cuenta_Cc.objects.all()
            serializer = CuentaCcSerializer(queryset, many=True)
            return serializer.data
