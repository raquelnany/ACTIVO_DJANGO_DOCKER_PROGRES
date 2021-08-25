from ..serializers import CentroCostoSerializer
from ..models import CentroCosto

class ControllerCentroCosto:
    serializer_class = CentroCostoSerializer
        
    def crearcentrocostos(request):
        datosCentrocostos = request.data
        CentrocostoNuevo = CentroCosto()
        
        try:
            CentrocostoNuevo.codigo_centro_costo = datosCentrocostos['codigo_centro_costo']
            CentrocostoNuevo.nombre_centro_costo =  datosCentrocostos['nombre_centro_costo']
            CentrocostoNuevo.codigo_cc =  datosCentrocostos['codigo_cc']
        except Exception:
             return {"estatus":"Error"}
        
        CentrocostoNuevo.save()
        return {"estatus":"Ok", 'nuevo_centrocosto': CentrocostoNuevo.codigo_centro_costo}

    def listarcentrocosto(id_centro_costo=None):
        if id_centro_costo:
            try:
                queryset = CentroCosto.objects.get(id_centro_costo=id_centro_costo)
            except CentroCosto.DoesNotExist:
                return ({'result': 'No se encontró el centro de costos deseado'})
            serializer = CentroCostoSerializer(queryset)
            return serializer.data
        else:
            queryset =CentroCosto.objects.all()
            serializer = CentroCostoSerializer(queryset, many=True)
            return serializer.data

    def modificarCentroCosto(request,id_centro_costo=None):
        if id_centro_costo:
            datosCentroCosto = request.data
            try:
                CentroCostoModificar = CentroCosto.objects.get(id_centro_costo=id_centro_costo)
            except CentroCosto.DoesNotExist:
                return ({'result': 'No se encontró el centro de costos deseado'})
            try: 
              
                CentroCostoModificar.codigo_centro_costo = datosCentroCosto['codigo_centro_costo']
                CentroCostoModificar.nombre_centro_costo = datosCentroCosto['nombre_centro_costo']
                CentroCostoModificar.codigo_cc =  datosCentroCosto['codigo_cc']
                CentroCostoModificar.save()
              
            except Exception:
                return {"estatus":"Error"}

            return {"estatus":"Ok", 'Centro_de_costos_modificado': CentroCostoModificar.nombre_centro_costo}
        else: 
            return {"result":"Ingrese el Id del centro de costos que desea modificar"}
