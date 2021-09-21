from ..serializers import ModeloSerializer
from ..models import Modelo, Clase_Equipo, Modelo_Icono

class ControllerModelo:
    def crearmodelo(request):
        datosModelo = request.data
        try:
            clase_equipo = Clase_Equipo.objects.get(id_clase_equipo=datosModelo['clase_equipo'])
            icono = Modelo_Icono.objects.get(id_modelo_icono=datosModelo['clase_equipo'])
                    
            ModeloNuevo = Modelo.objects.create(
                num_modelo =datosModelo['num_modelo'],
                modelo = datosModelo['modelo'],
                descripcion = datosModelo['descripcion'],
                fabricante= datosModelo['fabricante'],
                tipo_de_equipo= datosModelo['tipo_de_equipo'],
                clase_equipo = clase_equipo, 
                icono = icono,
            )
                
        except Exception:
            return {"estatus":"Error"}

        return {"estatus":"Ok", 'nuevo_modelo': ModeloNuevo.modelo}
       
    def listarmodelo(id_modelo=None):
        if id_modelo:
            try:
                queryset = Modelo.objects.get(id_modelo=id_modelo)
            except Modelo.DoesNotExist:
                return ({'result': 'No se encontró el modelo deseado'})
            serializer = ModeloSerializer(queryset)
            return serializer.data
        else:
            queryset = Modelo.objects.all()
            serializer = ModeloSerializer(queryset, many=True)
            return serializer.data

    def modificarmodelo(request,id_modelo=None):
        if id_modelo:
            datosModelo = request.data
            try:
                modeloModificar = Modelo.objects.get(id_modelo=id_modelo)
            except Modelo.DoesNotExist:
                return ({'result': 'No se encontró el modelo deseado'})
            try:
                clase_equipo = Clase_Equipo.objects.get(id_clase_equipo=datosModelo['clase_equipo'])
                icono = Modelo_Icono.objects.get(id_modelo_icono=datosModelo['clase_equipo'])
                 
                modeloModificar.num_modelo =datosModelo['num_modelo']
                modeloModificar.modelo = datosModelo['modelo']
                modeloModificar.descripcion = datosModelo['descripcion']
                modeloModificar.fabricante= datosModelo['fabricante']
                modeloModificar.tipo_de_equipo= datosModelo['tipo_de_equipo']
                modeloModificar.clase_equipo = clase_equipo
                modeloModificar.icono = icono
                
                modeloModificar.save()
              
            except Exception:
                return {"estatus":"Error"}

            return {"estatus":"Ok", 'modelo_modificar': modeloModificar.modelo}
        else: 
            return {"result":"Ingrese el Id del modelo que desea modificar"}