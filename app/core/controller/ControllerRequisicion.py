from ..serializers import RequisicionSerializer
from ..models import Requisicion, Requisicion_Estatus, Usuario


class ControllerRequisicion:
    def crearrequisicion(request):
        datosRequisicion = request.data
        try:
            requisitor = Usuario.objects.get(id_usuario = datosRequisicion['requisitor'])
            requisicion_estatus = Requisicion_Estatus.objects.get(id_requisicion_estatus = datosRequisicion['requisicion_estatus'])
            
            requisicionNuevo = Requisicion.objects.create(
                requisitor =  requisitor,
                requisicion_estatus = requisicion_estatus,
                departamento_solicitante = datosRequisicion['departamento_solicitante'],
                maquina_usarse = datosRequisicion['maquina_usarse'],
                centro_costos = datosRequisicion['centro_costos'],
                requisicion = datosRequisicion['requisicion'],
                requisicion_descripcion = datosRequisicion['requisicion_descripcion'],
                proveedor_principal = datosRequisicion['proveedor_principal'],
                proveedor_alterno = datosRequisicion['proveedor_alterno'],
                numero_parte_proveedor = datosRequisicion['numero_parte_proveedor'],
                costo = datosRequisicion['costo'],
                tiempo_entrega = datosRequisicion['tiempo_entrega'],
                maximo = datosRequisicion['maximo'],
                punto_reorden = datosRequisicion['punto_reorden'],
                fecha_creacion = datosRequisicion['fecha_creacion'],
                responde = datosRequisicion['responde'],
                fecha_respuesta = datosRequisicion['fecha_respuesta']
            )
                
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_requisicion': requisicionNuevo.id_requisicion}
       
    def listarrequisicion(id_requisicion=None):
        if id_requisicion:
            try:
                queryset = Requisicion.objects.get(id_requisicion=id_requisicion)
            except Requisicion.DoesNotExist:
                return ({'result': 'No se encontró la requisicion deseada'})
            serializer = RequisicionSerializer(queryset)
            return serializer.data
        else:
            queryset = Requisicion.objects.all()
            serializer = RequisicionSerializer(queryset, many=True)
            return serializer.data
