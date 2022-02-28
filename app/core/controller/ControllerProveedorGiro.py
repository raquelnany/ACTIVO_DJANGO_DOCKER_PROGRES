from ..serializers import ProveedorGiroSerializer  
from ..models import Giro, Orden_De_Compra_Proveedor, Proveedor_Giro


class ControllerProveedorGiro:
    def crearproveedorgiro(request):
        datosProveedorGiro = request.data
        try:
            giro = Giro.objects.get(id_giro = datosProveedorGiro['giro'])
            proveedor = Orden_De_Compra_Proveedor.objects.get(id_proveedor = datosProveedorGiro['proveedor'])

            proveedorGiroNuevo = Proveedor_Giro.objects.create(
                giro = giro,
                proveedor = proveedor
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'proveedor_giro_nuevo': proveedorGiroNuevo.id_proveeor_giro }
       
    def listarproveedorgiro(id_proveeor_giro=None):
        if id_proveeor_giro:
            try:
                queryset = Proveedor_Giro.objects.get(id_proveeor_giro = id_proveeor_giro)
            except Proveedor_Giro.DoesNotExist:
                return ({'result': 'No se encontró el giro de proveedor deseado'})
            serializer = ProveedorGiroSerializer(queryset)
            return serializer.data
        else:
            queryset = Proveedor_Giro.objects.all()
            serializer = ProveedorGiroSerializer(queryset, many=True)
            return serializer.data
