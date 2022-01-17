from ..serializers import RutaSetPointOperadorSerializer
from ..models import Ruta_Set_Point_Operador


class ControllerRutaSetPointOperador:

    def crearrutasetpointoperador(request):
        datosRuta = request.data
        rutaNuevo = Ruta_Set_Point_Operador()
        try:
           rutaNuevo.ruta_set_point_operador_es = datosRuta['ruta_set_point_operador_es']
           rutaNuevo.ruta_set_point_operador_en = datosRuta['ruta_set_point_operador_en']
           rutaNuevo.save()
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'ruta_set_point_operador': rutaNuevo.ruta_set_point_operador_es}

    def listarrutasetoperador(id_ruta_set_point_operador=None):
        if id_ruta_set_point_operador:
            try:
                queryset = Ruta_Set_Point_Operador.objects.get(id_ruta_set_point_operador=id_ruta_set_point_operador)
            except Ruta_Set_Point_Operador.DoesNotExist:
                return ({'result': 'No se encontró el operador de ruta deseado'})
            serializer = RutaSetPointOperadorSerializer(queryset)
            return serializer.data
        else:
            queryset = Ruta_Set_Point_Operador.objects.all()
            serializer = RutaSetPointOperadorSerializer(queryset, many=True)
            return serializer.data


    def generarrutasetpointoperador(self):
        
        CE = Ruta_Set_Point_Operador.objects.create(
           ruta_set_point_operador_es = "<",
           ruta_set_point_operador_en = "<",
        )
        CE.save()

        CE = Ruta_Set_Point_Operador.objects.create(
           ruta_set_point_operador_es = "<=",
           ruta_set_point_operador_en = "<=",
        )
        CE.save()

        CE = Ruta_Set_Point_Operador.objects.create(
           ruta_set_point_operador_es = "==",
           ruta_set_point_operador_en = "==",
        )
        CE.save()

        CE = Ruta_Set_Point_Operador.objects.create(
           ruta_set_point_operador_es = "<>",
           ruta_set_point_operador_en = "<>",
        )
        CE.save()

        CE = Ruta_Set_Point_Operador.objects.create(
           ruta_set_point_operador_es = ">",
           ruta_set_point_operador_en = ">",
        )
        CE.save()

        CE = Ruta_Set_Point_Operador.objects.create(
           ruta_set_point_operador_es = ">=",
           ruta_set_point_operador_en = ">=",
        )
        CE.save()

        CE = Ruta_Set_Point_Operador.objects.create(
           ruta_set_point_operador_es = "Entre",
           ruta_set_point_operador_en = "Between",
        )
        CE.save()
