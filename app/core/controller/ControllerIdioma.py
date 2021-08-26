from ..serializers import IdiomaSerializer
from ..models import Idioma


class ControllerIdioma:
    def crearidioma(request):
        datosIdioma = request.data
        idiomaNuevo = Idioma()
        try:
            idiomaNuevo.idioma = datosIdioma['idioma']
            idiomaNuevo.idioma_en = datosIdioma['idioma_en']
        except Exception:
             return {"estatus":"Error"}
        
        idiomaNuevo.save()
        return {"estatus":"Ok", 'idioma': idiomaNuevo.idioma}

    def listariridioma(id_idioma=None):
        if id_idioma:
            try:
                queryset = Idioma.objects.get(id_idioma=id_idioma)
            except Idioma.DoesNotExist:
                return ({'result': 'No se encontró el idioma deseado'})
            serializer = IdiomaSerializer(queryset)
            return serializer.data
        else:
            queryset = Idioma.objects.all()
            serializer = IdiomaSerializer(queryset, many=True)
            return serializer.data

    def modificaridioma(request,id_idioma=None):
        if id_idioma:
            datosIdioma = request.data
            try:
                idiomModificar = Idioma.objects.get(id_idioma=id_idioma)
            except Idioma.DoesNotExist:
                return ({'result': 'No se encontró el idioma a modificar'})
            try: 
              
                idiomModificar.idioma = datosIdioma['idioma']
                idiomModificar.idioma_en = datosIdioma['idioma_en']
                idiomModificar.save()
              
            except Exception:
                return {"estatus":"Error"}

            return {"estatus":"Ok", 'idioma_modificado': idiomModificar.idioma}
        else: 
            return {"result":"Ingrese el Id del idioma que desea modificar"}

