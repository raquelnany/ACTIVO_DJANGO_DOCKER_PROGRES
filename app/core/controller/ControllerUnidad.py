from ..serializers import UnidadSerializer
from ..models import Unidad

class ControllerUnidad:
    serializer_class = UnidadSerializer
        
    def crearunidad(request):
        datosUnidad = request.data
        UnidadNuevo = Unidad()
        
        try:
            UnidadNuevo.unidad_es =  datosUnidad['unidad_es']
            UnidadNuevo.unidad_en =  datosUnidad['unidad_en']
            UnidadNuevo.siglas = datosUnidad['siglas']
        except Exception:
             return {"estatus":"Error"}
        
        UnidadNuevo.save()
        return {"estatus":"Ok", 'nuevo_unidad': UnidadNuevo.unidad_es}

    def listarunidad(id_unidad=None):
        if id_unidad:
            try:
                queryset = Unidad.objects.get(id_unidad=id_unidad)
            except Unidad.DoesNotExist:
                return ({'result': 'No se encontró la unidad deseada'})
            serializer = UnidadSerializer(queryset)
            return serializer.data
        else:
            queryset = Unidad.objects.all()
            serializer = UnidadSerializer(queryset, many=True)
            return serializer.data

    def modificarunidad(request,id_unidad=None):
        if id_unidad:
            datosUnidad = request.data
            try:
                UnidadModificar = Unidad.objects.get(id_unidad=id_unidad)
            except Unidad.DoesNotExist:
                return ({'result': 'No se encontró la unidad deseada'})
            try: 
              
                UnidadModificar.unidad_es = datosUnidad['unidad_es']
                UnidadModificar.unidad_en = datosUnidad['unidad_en']
                UnidadModificar.siglas = datosUnidad['siglas']
                UnidadModificar.save()
              
            except Exception:
                return {"estatus":"Error"}

            return {"estatus":"Ok", 'Unidad_modificado': UnidadModificar.unidad_es}
        else: 
            return {"result":"Ingrese el Id de la unidad que desea modificar"}

    def generarunidades(self):

        UM=Unidad.objects.create(
            unidad_es='UNIDAD',
            unidad_en='UNIT',
            siglas='UM'
        )
        UM.save()

        KM=Unidad.objects.create(
            unidad_es='KILOMETRO',
            unidad_en='KILOMETER',
            siglas='km'
        )
        KM.save()

        M=Unidad.objects.create(
            unidad_es='METRO',
            unidad_en='METER',
            siglas='m'
        )
        M.save()

        IN=Unidad.objects.create(
            unidad_es='PULGADAS',
            unidad_en='INCH',
            siglas='in'
        )
        IN.save()

        FT=Unidad.objects.create(
            unidad_es='PIES',
            unidad_en='FEET',
            siglas='ft'
        )
        FT.save()

        YD=Unidad.objects.create(
            unidad_es='YARDAS',
            unidad_en='YARDAS',
            siglas='yd'
        )
        YD.save()

        M2=Unidad.objects.create(
            unidad_es='METRO CUADRADO',
            unidad_en='SQUARE MERTE',
            siglas='m2'
        )
        M2.save()

        M3=Unidad.objects.create(
            unidad_es='METRO CUBICO',
            unidad_en='CUBIC METER',
            siglas='m3'
        )
        M3.save()

        CM3=Unidad.objects.create(
            unidad_es='CENTIMETRO CUBICO',
            unidad_en='CUBIC CENTIMETER',
            siglas='cm3'
        )
        CM3.save()

        L=Unidad.objects.create(
            unidad_es='LITRO',
            unidad_en='LITER',
            siglas='l'
        )
        L.save()

        OZ=Unidad.objects.create(
            unidad_es='INZA',
            unidad_en='OUNCE',
            siglas='oz'
        )
        OZ.save()

        LB=Unidad.objects.create(
            unidad_es='LIBRAS',
            unidad_en='POUNDS',
            siglas='lb'
        )
        LB.save()

        T=Unidad.objects.create(
            unidad_es='TONELADA',
            unidad_en='TON',
            siglas='t'
        )
        T.save()

        KG=Unidad.objects.create(
            unidad_es='KILOGRAMO',
            unidad_en='KILOGRAM',
            siglas='kg'
        )
        KG.save()

        G=Unidad.objects.create(
            unidad_es='GRAMO',
            unidad_en='GRAMO',
            siglas='g'
        )
        G.save()

        PZ=Unidad.objects.create(
            unidad_es='PIEZA',
            unidad_en='PIECE',
            siglas='pz'
        )
        PZ.save()

        RLL=Unidad.objects.create(
            unidad_es='ROLLO',
            unidad_en='ROLL',
            siglas='rll'
        )
        RLL.save()

        TQ=Unidad.objects.create(
            unidad_es='TANQUE',
            unidad_en='TANK',
            siglas='tq'
        )
        TQ.save()

        SERV=Unidad.objects.create(
            unidad_es='SERVICIO',
            unidad_en='SERVICE',
            siglas='serv'
        )
        SERV.save()