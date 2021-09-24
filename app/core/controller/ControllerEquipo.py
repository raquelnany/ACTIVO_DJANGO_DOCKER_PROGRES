from ..serializers import EquipoSerializer
from ..models import CentroCosto, Equipo, Equipo_Estatus, Instalacion, Modelo, Modelo_Icono


class ControllerEquipo:

    def crearequipo(request):
        datosEquipo = request.data
        try:
           modelo = Modelo.objects.get(id_modelo = datosEquipo['modelo'])
           estatus = Equipo_Estatus.objects.get(id_equipo_estatus = datosEquipo['estatus'])
           instalacion = Instalacion.objects.get(id_instalacion = datosEquipo['instalacion'])
           centro_costos = CentroCosto.objects.get(id_centro_costos = datosEquipo['centro_costos'])
           icono = Modelo_Icono.objects.get(id_modelo_icono =  datosEquipo['icono'])

           EquipoNuevo = Equipo.objects.create(
            numero_de_equipo = datosEquipo['numero_de_equipo'],
            modelo = modelo,
            estatus = estatus,
            instalacion = instalacion,
            centro_costos = centro_costos,
            criticidad = datosEquipo['criticidad'],
            pasillo = datosEquipo['pasillo'],
            equipo_caido = datosEquipo['equipo_caido'],
            tiempo_muerto = datosEquipo['tiempo_muerto'],
            fila = datosEquipo['fila'],
            jerarquia = datosEquipo['jerarquia'],
            codigo_qr = datosEquipo['codigo_qr'],
            codigo_barras = datosEquipo['codigo_barras'],
            foto_equipo = datosEquipo['foto_equipo'],
            icono =  icono,
            num_pedimiento = datosEquipo['num_pedimiento'],
            garantia = datosEquipo['garantia'],
            fecha_compra = datosEquipo['fecha_compra'],
            num_serie = datosEquipo['num_serie'],
            horas_diarias = datosEquipo['horas_diarias'],
            dlunes = datosEquipo['dlunes'],
            dmartes = datosEquipo['dmartes'],
            dmiercoles = datosEquipo['dmiercoles'],
            djueves = datosEquipo['djueves'],
            dviernes = datosEquipo['dviernes'],
            dsabado = datosEquipo['dsabado'],
            ddomingo = datosEquipo['ddomingo'],
            comentarios = datosEquipo['comentarios'],
            referencias = datosEquipo['referencias'],
            )
        except Exception:
             return {"estatus":"Error"}

        return {"estatus":"Ok", 'equipo': EquipoNuevo.numero_de_equipo}

    def listarequipo(id_equipo=None):
        if id_equipo:
            try:
                queryset = Equipo.objects.get(id_equipo=id_equipo)
            except Equipo.DoesNotExist:
                return ({'result': 'No se encontró el equipo deseado'})
            serializer = EquipoSerializer(queryset)
            return serializer.data
        else:
            queryset = Equipo.objects.all()
            serializer = EquipoSerializer(queryset, many=True)
            return serializer.data

    def modificarequipo(request,id_equipo=None):
        if id_equipo:
            datosEquipo = request.data
            try:
                equipoModificar = Equipo.objects.get(id_equipo=id_equipo)
            except Equipo.DoesNotExist:
                return ({'result': 'No se encontró el equipo deseado'})
            try:
                
               modelo = Modelo.objects.get(id_modelo = datosEquipo['modelo'])
               estatus = Equipo_Estatus.objects.get(id_equipo_estatus = datosEquipo['estatus'])
               instalacion = Instalacion.objects.get(id_instalacion = datosEquipo['instalacion'])
               centro_costos = CentroCosto.objects.get(id_centro_costos = datosEquipo['centro_costos'])
               icono = Modelo_Icono.objects.get(id_modelo_icono =  datosEquipo['icono'])

               equipoModificar.numero_de_equipo = datosEquipo['numero_de_equipo']
               equipoModificar.modelo = modelo
               equipoModificar.estatus = estatus
               equipoModificar.instalacion = instalacion
               equipoModificar.centro_costos = centro_costos
               equipoModificar.criticidad = datosEquipo['criticidad']
               equipoModificar.pasillo = datosEquipo['pasillo']
               equipoModificar.equipo_caido = datosEquipo['equipo_caido']
               equipoModificar.tiempo_muerto = datosEquipo['tiempo_muerto']
               equipoModificar.fila = datosEquipo['fila']
               equipoModificar.jerarquia = datosEquipo['jerarquia']
               equipoModificar.codigo_qr = datosEquipo['codigo_qr']
               equipoModificar.codigo_barras = datosEquipo['codigo_barras']
               equipoModificar.foto_equipo = datosEquipo['foto_equipo']
               equipoModificar.icono =  icono
               equipoModificar.num_pedimiento = datosEquipo['num_pedimiento']
               equipoModificar.garantia = datosEquipo['garantia']
               equipoModificar.fecha_compra = datosEquipo['fecha_compra']
               equipoModificar.num_serie = datosEquipo['num_serie']
               equipoModificar.horas_diarias = datosEquipo['horas_diarias']
               equipoModificar.dlunes = datosEquipo['dlunes']
               equipoModificar.dmartes = datosEquipo['dmartes']
               equipoModificar.dmiercoles = datosEquipo['dmiercoles']
               equipoModificar.djueves = datosEquipo['djueves']
               equipoModificar.dviernes = datosEquipo['dviernes']
               equipoModificar.dsabado = datosEquipo['dsabado']
               equipoModificar.ddomingo = datosEquipo['ddomingo']
               equipoModificar.comentarios = datosEquipo['comentarios']
               equipoModificar.referencias = datosEquipo['referencias']
               equipoModificar.save()

            except Exception:
                return {"estatus":"Error"}
            return {"estatus":"Ok", 'equipo_modificado': equipoModificar.numero_de_equipo}
        else: 
            return {"result":"Ingrese el Id del equipo que desea modificar"}