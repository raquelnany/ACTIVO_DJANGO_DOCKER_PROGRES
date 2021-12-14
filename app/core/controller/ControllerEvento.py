from ..serializers import EventoSerializer
from ..models import Evento

class ControllerEvento:
    serializer_class = EventoSerializer
        
    def crearorevento(request):
        datosEvento = request.data
        eventoNuevo = Evento()
        try:
            eventoNuevo.tabla = datosEvento['tabla']
            eventoNuevo.id_registro = datosEvento['id_registro']
            eventoNuevo.accion_en = datosEvento['accion_en']
            eventoNuevo.fecha  = datosEvento['fecha']
            eventoNuevo.hora = datosEvento['hora']
            eventoNuevo.linux = datosEvento['linux']
            eventoNuevo.bloque_es = datosEvento['bloque_es']
            eventoNuevo.accion_es = datosEvento['accion_es']
            eventoNuevo.usuario = datosEvento['usuario']
            eventoNuevo.bloque_en = datosEvento['bloque_en']

        except Exception:
             return {"estatus":"Error"}
        
        eventoNuevo.save()

        return {"estatus":"Ok", 'evento': eventoNuevo.tabla}

    def listarevento(id_evento=None):
        if id_evento:
            try:
                queryset = Evento.objects.get(id_evento=id_evento)
            except Evento.DoesNotExist:
                return ({'result': 'No se encontró el evento deseado'})
            serializer = EventoSerializer(queryset)
            return serializer.data
        else:
            queryset = Evento.objects.all()
            serializer = EventoSerializer(queryset, many=True)
            return serializer.data
