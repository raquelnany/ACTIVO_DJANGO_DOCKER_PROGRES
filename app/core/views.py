from inflection import re
from rest_framework import generics, serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .controller.ControllerCentroCosto import CentroCosto, ControllerCentroCosto
from .controller.ControllerHistTurno import ControllerHistTurno
from .controller.ControllerPuesto import ControllerPuesto
from .controller.ControllerIdioma import ControllerIdioma
from .controller.ControllerDept import ControllerDept
from .controller.ControllerUsuario import ControllerUsuario
from .controller.ControllerTurno import ControllerTurno
from .controller.ControllerTipoRol import ControllerTipoRol
from .controller.ControllerScope import ControllerScope
from .controller.ControllerEstatus import ControllerEstatus
from .controller.ControllerRol import ControllerRol
from .controller.ControllerLogin import ControllerLogin
from .controller.ControllerDeptTurno import ControllerDeptTurno
from .controller.ContollerProveedor import ControllerProveedor
from .controller.ControllerUnidad import ControllerUnidad
from .controller.ControllerContactoProveedor import ControllerContactoProveedor
from .assets.DistanciaEntrePuntos import DistanciaEntrePuntos
from .controller.ControllerInventarioCategoria import ControllerInventarioCategoria
from .controller.ControllerCliente import ControllerCliente
from .controller.ControllerJornada import ControllerJornada
from .controller.ControllerEquipoCategoriaEstatus import ControllerEquipoCategiriaEstatus
from .controller.ControllerJornadaHoras import ControllerJornadaHoras
from .controller.ControllerEquipoCategoria import ControllerEquipoCategoria
from .controller.ControllerClaseEquipo import ControllerClaseEquipo
from .controller.ControllerEquipoCategoriaIcono import ControllerEquipoCategoriaIcono
from .controller.ControllerModelo import ControllerModelo
from .controller.ControllerEquipoEstatus import ControllerEquipoEstatus
from .controller.ControllerEquipo import ControllerEquipo
from .controller.ControllerHerramientaMovimiento import ControllerHerramientaMovimiento
from .controller.ControllerHerramienta import ControllerHerramienta
from .controller.ControllerHerramientaHistorial import ControllerHerramientaHistorial
from .controller.ControllerInventarioTipo import ControllerInventarioTipo
from .controller.ControllerStock import ControllerStock
from .controller.ControllerStockDetalle import ControllerStockDetalle
from .controller.ControllerStockEntrada import ControllerStockEntrada
from .controller.ControllerStockAjuste import ControllerStockAjuste
from .controller.ControllerParteEstatus import ControllerParteEstatus
from .controller.ControllerInventarioAjuste import ControllerInventarioAjuste
from .controller.ControllerParteDetalle import ControllerParteDetalle
from .controller.ControllerDevolucion import ControllerDevolucion
from .controller.ControllerAlmacen import ControllerAlmacen
from .controller.ControllerOrdenTrabajoTipo import ControllerOrdenTrabajoTipo
from .controller.ControllerOrdenTrabajoPrioridad import ControllerOrdenTrabajoPrioridad
from .controller.ControllerInventarioVale import ControllerInventarioVale
from .controller.ControllerParteDetalleSurtido import ControllerParteDetalleSurtido
from .controller.ControllerInstalacion import ControllerInstalacion
from .controller.ControllerInstalacionIcono import ControllerInstalacionIcono
from .controller.ControllerModeloIcono import ControllerModeloIcono
from .controller.ControllerOrdenSubestatus import ControllerOrdenSubestatus
from .controller.ControllerOrdenTrabajoEstatus import ControllerOrdenTrabajoEstatus
from .controller.ControllerOT import ControllerOT
from .controller.ControllerActOtCodigo import ControllerActOtCodigo
from .controller.ControllerActOtTipo import ControllerActOtTipo
from .controller.ControllerEvento import ControllerEvento
from .controller.ControllerOrdenArchivos import ControllerOrdenArchivos
from .controller.ControllerOrdenTrabajoParte import ControllerOrdenTrabajoParte
from .controller.ControllerTareaOrdenTrabajo import ControllerTareaOrdenTrabajo
from .controller.ControllerTipoCambio import ControllerTipoCambio
from .controller.ControllerOrdenTrabajoCompleta import ControllerOrdenTrabajoCompleta
from .controller.ControllerRca import ControllerRca
from .controller.ControllerRcaAccionPreventiva import ControllerRcaAccionPreventiva
from .controller.ControllerRcaPreventiveStatus import ControllerRcaPreventiveStatus
from .controller.ControllerRcaStatus import ControllerRcaStatus
from .controller.ControllerRcaTipoAccion import ControllerRcaTipoAccion
from .controller.ControllerModoDeteccion import ControllerModoDeteccion
from .controller.ControllerActividadMantenimiento import ControllerActividadMantenimiento
from .controller.ControllerUsuarioRevisar import ControllerUsuarioRevisar
from .controller.ControllerOrdenTrabajoRevisada import ControllerOrdenTrabajoRevisada
from .controller.ControllerRutaEstatus import ControllerRutaEstatus
from .controller.ControllerRuta import ControllerRuta
from .controller.ControllerRutaEquipo import ControllerRutaEquipo
from .controller.ControllerRutaCondicion import ControllerRutaCondicion
from .controller.ControllerRutaCondicionUnidad import ControllerRutaCondicionUnidad
from .controller.ControllerRutaEquipoComponente import ControllerRutaEquipoComponente
from .controller.ControllerRutaSetPointOperador import ControllerRutaSetPointOperador
from .controller.ControllerRutaSetPoint import ControllerRutaSetPoint
from .controller.ControllerOrdenTrabajoRuta import ControllerOrdenTrabajoRuta
from .controller.ControllerChecklist import ControllerChecklist
from .controller.ControllerChecklistEquipo import ControllerChecklistEquipo
from .controller.ControllerOrdenTrabajoRutaSetPoint import ControllerOrdenTrabajoRutaSetPoint
from .controller.ControllerChecklistAspecto import ControllerChecklistAspecto
from .controller.ControllerChecklistInstruccion import ControllerChecklistInstruccion
from .controller.ControllerChecklistAspectoCopiado import ControllerChecklistAspectoCopiado
from .controller.ControllerChk import ControllerChk
from .controller.ControllerChkEquipo import ControllerChkEquipo
from .controller.ControllerChkAspecto import ControllerChkAspecto
from .controller.ControllerChkInstruccion import ControllerChkIntruccion
from .controller.ControllerOrdenTrabajoChecklist import ControllerOrdenTrabajoChecklist

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ActividadMantenimientoSerializer, AlmacenSerializer, AtcOtCodigoSerializer, AtcOtTipoSerializer, ChecklistAspectoCopiadoSerializer, ChecklistAspectoSerializer, ChecklistEquipoSerializer, ChecklistInstruccionSerializer, ChecklistSerializer, ChkAspectoSerializer, ChkEquipoSerializer, ChkInstruccionSerializer, ChkSerializer, ClaseEquipoSerializer, DevolucionSerializer, EquipoCategoriaEstatusSerializaer, EquipoCategoriaIconoSerializaer, EquipoEstatusSerializer, EquipoSerializer, EventoSerializer, HerramientaMovimientoSerializer, HerramientaSerializer, InstalacionIconoSerializer, InstalacionSerializer, InventarioAjusteSerializer, InventarioTipoSerializer, InventarioValeSerializer, JornadaHorasSerializer, JornadaSerializer, CentroCostoSerializer, ClienteSerializer, Contacto_ProveedorSerializer, Departamento_TurnoSerializer, EstatusSerializer, IdiomaSerializer, Inventario_CategoriaSerializer, ModeloIconoSerializer, ModeloSerializer, ModoDeteccionSerializer, OTSerializer, OrdenArchivosSerializer, OrdenSubestatusSerializer, OrdenTrabajoChecklistSerializer, OrdenTrabajoCompletaSerializer, OrdenTrabajoEstatusSerializer, OrdenTrabajoParteSerializer, OrdenTrabajoPrioridadSerializer, OrdenTrabajoRevisadaSerializer, OrdenTrabajoRutaSerializer, OrdenTrabajoRutaSetPointSerializer, OrdenTrabajoTipoSerializer, ParteDetalleSerializer, ParteDetalleSurtidoSerializer, ParteEstatusSerializer, PuestoSerializer, RCASerializer, RcaAccionPreventivaSerializer, RcaPreventiveStatusSerializer, RcaStatusSerializer, RcaTipoAccionSerializer, RolSerializer, RutaCondicionSerializer, RutaCondicionUnidadSerializer, RutaEquipoComponenteSerializer, RutaEquipoSerializer, RutaEstatusSerializer, RutaSerializer, RutaSetPointOperadorSerializer, RutaSetPointSerializer, ScopeSerializer, StockAjusteSerializer, StockDetalleSerializer, StockEntradaSerializer, StockSerializer, TareaOrdenTrabajoSerializer, Tipo_RolSerializer, TipoCambioSerializer, TurnoSerializer, UserSerializer, AuthTokenSerializer, DepartamentoSerializer, UsuarioRevisarSerializer, UsuarioSerializer, CentroCostoSerializer, ProveedorSerializer
from .serializers import Usuario_Lat_Lng_Serializer, TurnoSerializer, UnidadSerializer, setup_Serializer, EquipoCategoriaSerializer, HerramientaHistorialSerializer

from .models import Modelo, Unidad

#View encargada de auto generar una serie de unidades con datos quemados por el método
#Observación: Es importante que solo sea usada una vez
class Setup(GenericAPIView):
    serializer_class = setup_Serializer
    def post(self, request, *args, **kwargs):

        generate_data = request.data

        #Desde el serializer el valor de generate sera de tipo booleano
        generar_unidades=generate_data['generar_unidades']
        generar_categorias=generate_data['generar_categorias']
        generar_equipo_categoria_estatus=generate_data['generar_equipo_categoria_estatus']
        generar_equipo_categoria=generate_data['generar_equipo_categoria']
        generar_clase_equipo=generate_data['generar_clase_equipo']
        generar_modelo_icono=generate_data['generar_modelo_icono']
        generar_equipo_categoria_icono=generate_data['generar_equipo_categoria_icono']
        generar_instalacion_icono = generate_data['generar_instalacion_icono']
        generar_equipo_estatus =  generate_data['generar_equipo_estatus']
        generar_herramienta_movimiento = generate_data['generar_herramienta_movimiento']
        generar_orden_subestatus = generate_data['generar_orden_subestatus']
        generar_orden_trabajo_estatus = generate_data['generar_orden_trabajo_estatus']
        mensaje =''

        if generar_unidades:
            ControllerUnidad.generarunidades(request)
            mensaje='Se han generado exitosamente las unidades: UM, km, m, in, ft, yd, m2, m3, cm3, l, oz, lb, t, g, kg, l, rll, tq, serv'
        if generar_categorias:
            ControllerInventarioCategoria.generarcategorias(request)
            mensaje=mensaje+ 'Se han generado correctamente las categorias: GENE, GRAS, SEGU, MAQU, HERR, ACEI, DIEL, PEGA, BURI, INSE, PAPE, FERRE, ALCO, JOBO, BATE, LIMP, SOLV'
        if generar_equipo_categoria_estatus:
            ControllerEquipoCategiriaEstatus.generarequipocategoriaestatus(request)
            mensaje=mensaje+ 'Se han generado correctamente los equipo categoria estatus : Inactivo, Activo, Re-activar'
        if generar_equipo_categoria:
            ControllerEquipoCategoria.generarequipocategoria(request)
            mensaje=mensaje+ 'Se han generado correctamente las categorias de equipo : RTT, MCH, ELC, SFC, SBP, DLL, WLC, WLI, MRN, UTL, PN, HD, PL,ST'
        if generar_clase_equipo:
            ControllerClaseEquipo.generarclaseequipo(request)
            mensaje=mensaje+ 'Se han generado correctamente las clases de equipo : MX, CR, HE, HB, VE, PI, WI, ST, FS, PS, TR, TD, FC, CB, CPB, FD ...'
        if generar_modelo_icono:
            ControllerModeloIcono.generarmodeloicono(request)
            mensaje=mensaje+ 'Se han generado correctamente los modelos iconos : ...'
        if generar_equipo_categoria_icono:
            ControllerEquipoCategoriaIcono.generarequipocategoriaIcono(request)
            mensaje = mensaje + 'Se han generado correctamente los equipos categorias iconos'
        if generar_instalacion_icono:
            ControllerInstalacionIcono.generarinstalacionicono(request)
            mensaje = mensaje + 'Se han generado correctamente las instalaciones iconos'
        if generar_equipo_estatus:
            ControllerEquipoEstatus.generarequipoestatus(request)
            mensaje = mensaje + 'Se han generado correctamente las estatus de los objetos'
        if generar_herramienta_movimiento:
            ControllerHerramientaMovimiento.generarherramientamovimiento(request)
            mensaje = mensaje + 'Se han generado los movimientos de herramietas'
        if generar_orden_subestatus:
            ControllerOrdenSubestatus.generarordensubestatus(request)
            mensaje = mensaje + 'Se han generado los subestatus de orden'
        if generar_orden_trabajo_estatus:
            ControllerOrdenTrabajoEstatus.generarordentrabajoestatus(request)
            mensaje = mensaje + 'Se han generado los estatus de orden de trabajo'

        if not generar_unidades and not generar_categorias and not generar_equipo_categoria_estatus and not generar_equipo_categoria and not generar_clase_equipo and not generar_modelo_icono and not generar_equipo_categoria_icono and not generar_instalacion_icono:
            if not generar_equipo_estatus and not generar_herramienta_movimiento and not generar_orden_subestatus and not generar_orden_trabajo_estatus:
                mensaje= 'no se cargo nada'
        return Response({'result':mensaje})

    
        
        
   
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UsuarioLatLngView(GenericAPIView):

    serializer_class = Usuario_Lat_Lng_Serializer

    def post(self, request, *args, **kwargs):

        lat_us = float(request.data['lat_usuario'])
        lon_us = float(request.data['lon_usuario'])
        lat_em = float(request.data['lat_empresa'])
        lon_em = float(request.data['lon_empresa'])
        print(request.data)
        mts = round (DistanciaEntrePuntos.distancia_km(
            lat1=lat_us, lon1=lon_us, lat2=lat_em, lon2=lon_em), 2)
        acceso = True if mts<50 else False
        return Response({'distancia_usuario_planta': f'{mts} metros', 'acceso':acceso})

class Proveedorview(APIView):
    serializer_class = ProveedorSerializer

    def post(self, request):
        respuesta = ControllerProveedor.crearproveedor(request)
        return Response(respuesta)

    def get(self, request, id_proveedor=None):
        respuesta = ControllerProveedor.listarproveedor(id_proveedor)
        return Response(respuesta)

    def put(self, request, id_proveedor=None):
        respuesta = ControllerProveedor.modificarProveedor(request,id_proveedor)
        return Response(respuesta)

class Contacto_Proveedorview(APIView):
    serializer_class = Contacto_ProveedorSerializer

    def post(self, request):
        respuesta = ControllerContactoProveedor.crearcontacto_proveedor(request)
        return Response(respuesta)

    def get(self, request, id_contacto_proveedor=None):
        respuesta = ControllerContactoProveedor.listarcontacto_proveedor(id_contacto_proveedor)
        return Response(respuesta)

    def put(self, request, id_contacto_proveedor=None):
        respuesta = ControllerContactoProveedor.modificarcontacto_proveedor(request,id_contacto_proveedor)
        return Response(respuesta)

class CentroCostosview(APIView):
    serializer_class = CentroCostoSerializer

    def post(self, request):
        respuesta = ControllerCentroCosto.crearcentrocostos(request)
        return Response(respuesta)

    def get(self, request, id_centro_costo=None):
        respuesta = ControllerCentroCosto.listarcentrocosto(id_centro_costo)
        return Response(respuesta)
        
    def put(self, request, id_centro_costo=None):
        respuesta = ControllerCentroCosto.modificarCentroCosto(request,id_centro_costo)
        return Response(respuesta)
   

class Departamentoview(APIView):
    serializer_class = DepartamentoSerializer

    def post(self, request):
        respuesta = ControllerDept.creardepartamento(request)
        return Response(respuesta)

    def get(self, request, id_departamento=None):
        respuesta = ControllerDept.listardepartamento(id_departamento)
        return Response(respuesta)

class Jornadaview(APIView):
    serializer_class = JornadaSerializer

    def post(self, request):
        respuesta = ControllerJornada.crearjornada(request)
        return Response(respuesta)

    def get(self, request, id_jornada=None):
        respuesta = ControllerJornada.listarjornada(id_jornada)
        return Response(respuesta)
        
    def put(self, request, id_jornada=None):
        respuesta = ControllerJornada.modificarjornada(request,id_jornada)
        return Response(respuesta)

class Turnoview(APIView):
    serializer_class = TurnoSerializer

    def post(self, request):
        respuesta = ControllerTurno.crearturno(request)
        return Response(respuesta)

    def get(self, request, id_turno=None):
        respuesta = ControllerTurno.listarturno(id_turno)
        return Response(respuesta)


class Tipo_Rolview(APIView):
    serializer_class = Tipo_RolSerializer

    def post(self, request):
        respuesta = ControllerTipoRol.creartipo_rol(request)
        return Response(respuesta)

    def get(self, request, id_tipo_rol=None):
        respuesta = ControllerTipoRol.listartipo_rol(id_tipo_rol)
        return Response(respuesta)


class Scopeview(APIView):
    serializer_class = ScopeSerializer

    def post(self, request):
        respuesta = ControllerScope.crearscope(request)
        return Response(respuesta)

    def get(self, request, id_scope=None):
        respuesta = ControllerScope.listarscope(id_scope)
        return Response(respuesta)


class Estatusview(APIView):
    serializer_class = EstatusSerializer

    def post(self, request):
        respuesta = ControllerEstatus.crearestatus(request)
        return Response(respuesta)

    def get(self, request, id_estatus=None):
        respuesta = ControllerEstatus.listarestatus(id_estatus)
        return Response(respuesta)


class Idiomaview(APIView):
    serializer_class = IdiomaSerializer

    def post(self, request):
        respuesta = ControllerIdioma.crearidioma(request)
        return Response(respuesta)

    def get(self, request, id_idioma=None):
        respuesta = ControllerIdioma.listariridioma(id_idioma)
        return Response(respuesta)

    def put(self, request, id_idioma=None):
        respuesta = ControllerIdioma.modificaridioma(request,id_idioma)
        return Response(respuesta)   

class Rolview(APIView):
    serializer_class = RolSerializer

    def post(self, request):
        respuesta = ControllerRol.crearrol(request)
        return Response(respuesta)

    def get(self, request, id_rol=None):
        respuesta = ControllerRol.listarrol(id_rol)
        return Response(respuesta)


class Departamento_Turnoview(APIView):
    serializer_class = Departamento_TurnoSerializer

    def post(self, request):
        respuesta = ControllerDeptTurno.creardepartamento_turno(request)
        return Response(respuesta)

    def get(self, request, id_departamento_turno=None):
        respuesta = ControllerDeptTurno.listardepartamento_turno(
            id_departamento_turno)
        return Response(respuesta)


class Puestoview(APIView):
    serializer_class = PuestoSerializer

    def post(self, request):
        respuesta = ControllerPuesto.crearpuesto(request)
        return Response(respuesta)

    def get(self, request, id_puesto=None):
        respuesta = ControllerPuesto.listarpuesto(id_puesto)
        return Response(respuesta)


class Usuarioview(APIView):
    serializer_class = UsuarioSerializer

    def post(self, request):
        respuesta = ControllerUsuario.crearUsuario(request)
        return Response(respuesta)

    def get(self, request, id_usuario=None):
        respuesta = ControllerUsuario.listarUsuario(id_usuario)
        return Response(respuesta)

    def put(self, request, id_usuario=None):
        respuesta = ControllerUsuario.modificarUsuario(request,id_usuario)
        return Response(respuesta)
        

class PerfilUsuarioview(APIView):
    def get(self, request, p_nombre=None):
        respuesta = ControllerUsuario.verPerfil(p_nombre)
        return Response(respuesta)


class Historial_TurnoView(APIView):
    def post(self, request):
        respuesta = ControllerHistTurno.crearhistorial_turno(request)
        return Response(respuesta)

    def get(self, request, id_historial_turno=None):
        respuesta = ControllerHistTurno.listarhistorialturno(
            id_historial_turno)
        return Response(respuesta)

class JornadaHorasview(APIView):
    serializer_class = JornadaHorasSerializer

    def post(self, request):
        respuesta = ControllerJornadaHoras.crearjornadahoras(request)
        return Response(respuesta)

    def get(self, request, id_jornada_horas=None):
        respuesta = ControllerJornadaHoras.listarjornadahoras(id_jornada_horas)
        return Response(respuesta)
    
    def put(self, request, id_jornada_horas=None):
        respuesta = ControllerJornadaHoras.modificarjornadahoras(request,id_jornada_horas)
        return Response(respuesta)
        
class LoginView(APIView):
    def post(self, request):
        respuesta = ControllerLogin.login(request)
        return Response(respuesta)


class Unidadview(APIView):
    serializer_class = UnidadSerializer

    def post(self, request):
        respuesta = ControllerUnidad.crearunidad(request)
        return Response(respuesta)

    def get(self, request, id_unidad=None):
        respuesta = ControllerUnidad.listarunidad(id_unidad)
        return Response(respuesta)
        
    def put(self, request, id_unidad=None):
        respuesta = ControllerUnidad.modificarunidad(request,id_unidad)
        return Response(respuesta)


class Inventario_Categoriaview(APIView):
    serializer_class = Inventario_CategoriaSerializer

    def post(self, request):
        respuesta = ControllerInventarioCategoria.crearinventariocategoria(request)
        return Response(respuesta)

    def get(self, request, id_inventario_categoria=None):
        respuesta = ControllerInventarioCategoria.listarinventariocategoria(id_inventario_categoria)
        return Response(respuesta)
        
    def put(self, request, id_inventario_categoria=None):
        respuesta = ControllerInventarioCategoria.modificarinventariocategoria(request,id_inventario_categoria)
        return Response(respuesta)


class Clienteview(APIView):
    serializer_class = ClienteSerializer

    def post(self, request):
        respuesta = ControllerCliente.crearcliente(request)
        return Response(respuesta)

    def get(self, request, id_cliente=None):
        respuesta = ControllerCliente.listarcliente(id_cliente)
        return Response(respuesta)

    def put(self, request, id_cliente=None):
        respuesta = ControllerCliente.modificarcliente(request,id_cliente)
        return Response(respuesta)


class EquipoCategoriaEstatusview(APIView):
    serializer_class = EquipoCategoriaEstatusSerializaer

    def post(self, request):
        respuesta = ControllerEquipoCategiriaEstatus.crearequipocategoriaestatus(request)
        return Response(respuesta)

    def get(self, request, id_estatus=None):
        respuesta = ControllerEquipoCategiriaEstatus.listarequipocategoriaestatus(id_estatus)
        return Response(respuesta)


class EquipoCategoriaview(APIView):
    serializer_class = EquipoCategoriaSerializer

    def post(self, request):
        respuesta = ControllerEquipoCategoria.crearequipocategoria(request)
        return Response(respuesta)

    def get(self, request, id_equipo_categoria=None):
        respuesta = ControllerEquipoCategoria.listarequipocategoria(id_equipo_categoria)
        return Response(respuesta)

class ClaseEquipoview(APIView):
    serializer_class = ClaseEquipoSerializer

    def post(self, request):
        respuesta = ControllerClaseEquipo.crearclaseequipo(request)
        return Response(respuesta)

    def get(self, request, id_equipo_categoria=None):
        respuesta = ControllerClaseEquipo.listarclaseequipo(id_equipo_categoria)
        return Response(respuesta)

class ModeloIconoview(APIView):
    serializer_class = ModeloIconoSerializer

    def post(self, request):
        respuesta = ControllerModeloIcono.crearmodeloicono(request)
        return Response(respuesta)

    def get(self, request, id_modelo_icono=None):
        respuesta = ControllerModeloIcono.listarmodeloicono(id_modelo_icono)
        return Response(respuesta)
    

class EquipoCategoriaIconoview(APIView):
    serializer_class = EquipoCategoriaIconoSerializaer

    def post(self, request):
        respuesta = ControllerEquipoCategoriaIcono.crearequipocategoriaicono(request)
        return Response(respuesta)

    def get(self, request, id_equipo_categoria_icono=None):
        respuesta = ControllerEquipoCategoriaIcono.listarequipocategoriaicono(id_equipo_categoria_icono)
        return Response(respuesta)

class Modeloview(APIView):
    serializer_class = ModeloSerializer

    def post(self, request):
        respuesta = ControllerModelo.crearmodelo(request)
        return Response(respuesta)

    def get(self, request, id_modelo=None):
        respuesta = ControllerModelo.listarmodelo(id_modelo)
        return Response(respuesta)

    def put(self, request, id_modelo=None):
        respuesta = ControllerModelo.modificarmodelo(request,id_modelo)
        return Response(respuesta)

class InstalacionIconoview(APIView):
    serializer_class = InstalacionIconoSerializer

    def post(self, request):
        respuesta = ControllerInstalacionIcono.crearinstalacionicono(request)
        return Response(respuesta)

    def get(self, request, id_instalacion_icono=None):
        respuesta = ControllerInstalacionIcono.listarinstalacionicono(id_instalacion_icono)
        return Response(respuesta)

class InstalacionView(APIView):
    serializer_class = InstalacionSerializer

    def post(self, request):
        respuesta = ControllerInstalacion.crearinstalacion(request)
        return Response(respuesta)

    def get(self, request, id_instalacion=None):
        respuesta = ControllerInstalacion.listarinstalacion(id_instalacion)
        return Response(respuesta)
        
    def put(self, request, id_instalacion=None):
        respuesta = ControllerInstalacion.modificarinstalacion(request,id_instalacion)
        return Response(respuesta)

class EquipoEstatusView(APIView):
    serializer_class = EquipoEstatusSerializer

    def post(self, request):
        respuesta = ControllerEquipoEstatus.crearequipoestatus(request)
        return Response(respuesta)

    def get(self, request, id_equipo_estatus=None):
        respuesta = ControllerEquipoEstatus.listarequipoestatus(id_equipo_estatus)
        return Response(respuesta)

class Equipoview(APIView):
    serializer_class = EquipoSerializer

    def post(self, request):
        respuesta = ControllerEquipo.crearequipo(request)
        return Response(respuesta)

    def get(self, request, id_equipo=None):
        respuesta = ControllerEquipo.listarequipo(id_equipo)
        return Response(respuesta)
        
    def put(self, request, id_equipo=None):
        respuesta  =ControllerEquipo.modificarequipo(request,id_equipo)
        return Response(respuesta)

class HerramientaMovimientoview(APIView):
    serializer_class = HerramientaMovimientoSerializer

    def post(self, request):
        respuesta = ControllerHerramientaMovimiento.crearherramientamovimiento(request)
        return Response(respuesta)

    def get(self, request, id_herramienta_movimiento=None):
        respuesta = ControllerHerramientaMovimiento.listarherramientamovimiento(id_herramienta_movimiento)
        return Response(respuesta)

class Herramientaview(APIView):
    serializer_class = HerramientaSerializer

    def post(self, request):
        respuesta = ControllerHerramienta.crearherramienta(request)
        return Response(respuesta)

    def get(self, request, id_herramienta=None):
        respuesta = ControllerHerramienta.listarherramienta(id_herramienta)
        return Response(respuesta)
        
    def put(self, request, id_herramienta=None):
        respuesta  = ControllerHerramienta.modificarherramienta(request,id_herramienta)
        return Response(respuesta)

class HerramientaHistorialview(APIView):
    serializer_class = HerramientaHistorialSerializer

    def post(self, request):
        respuesta = ControllerHerramientaHistorial.crearherramientahistorial(request)
        return Response(respuesta)

    def get(self, request, id_herramienta_historial=None):
        respuesta = ControllerHerramientaHistorial.listarherramientahistorial(id_herramienta_historial)
        return Response(respuesta)

class InventarioTipoview(APIView):
    serializer_class = InventarioTipoSerializer

    def post(self, request):
        respuesta = ControllerInventarioTipo.crearinventarioTipo(request)
        return Response(respuesta)

    def get(self, request, id_inventario_tipo=None):
        respuesta = ControllerInventarioTipo.listarinventariotipo(id_inventario_tipo)
        return Response(respuesta)

class Stockview(APIView):
    serializer_class = StockSerializer

    def post(self, request):
        respuesta = ControllerStock.crearstock(request)
        return Response(respuesta)

    def get(self, request, id_stock=None):
        respuesta = ControllerStock.listarstock(id_stock)
        return Response(respuesta)

class StockDetalleview(APIView):
    serializer_class = StockDetalleSerializer

    def post(self, request):
        respuesta = ControllerStockDetalle.crearstockdetalle(request)
        return Response(respuesta)

    def get(self, request, id_stock_detalle=None):
        respuesta = ControllerStockDetalle.listarstockDetalle(id_stock_detalle)
        return Response(respuesta)
              

class StockEntradaview(APIView):
    serializer_class = StockEntradaSerializer

    def post(self, request):
        respuesta = ControllerStockEntrada.crearstockentrada(request)
        return Response(respuesta)

    def get(self, request, id_stock_entrada=None):
        respuesta = ControllerStockEntrada.listarstockentrada(id_stock_entrada)
        return Response(respuesta)
              
class StockAjusteview(APIView):
    serializer_class = StockAjusteSerializer

    def post(self, request):
        respuesta = ControllerStockAjuste.crearstockajuste(request)
        return Response(respuesta)

    def get(self, request, id_stock_ajuste=None):
        respuesta = ControllerStockAjuste.listarstockajuste(id_stock_ajuste)
        return Response(respuesta)
              
class ParteEstatusview(APIView):
    serializer_class = ParteEstatusSerializer

    def post(self, request):
        respuesta = ControllerParteEstatus
        return Response(respuesta)

    def get(self, request, id_stock_ajuste=None):
        respuesta = ControllerStockAjuste.listarstockajuste(id_stock_ajuste)
        return Response(respuesta)

class InventarioAjusteview(APIView):
    serializer_class = InventarioAjusteSerializer

    def post(self, request):
        respuesta = ControllerInventarioAjuste.crearinventarioajuste(request)
        return Response(respuesta)

    def get(self, request, id_inventario_ajuste=None):
        respuesta = ControllerInventarioAjuste.listarinventarioajuste(id_inventario_ajuste)
        return Response(respuesta)

class ParteDetalleview(APIView):
    serializer_class = ParteDetalleSerializer

    def post(self, request):
        respuesta = ControllerParteDetalle.crearpartedetalle(request)
        return Response(respuesta)

    def get(self, request, id_parte_detalle=None):
        respuesta =ControllerParteDetalle.listarpartedetalle(id_parte_detalle)
        return Response(respuesta)
        
class Devolucionview(APIView):
    serializer_class = DevolucionSerializer

    def post(self, request):
        respuesta = ControllerDevolucion.creardevolucion(request)
        return Response(respuesta)

    def get(self, request, id_devolucion=None):
        respuesta = ControllerDevolucion.listardevolcion(id_devolucion)
        return Response(respuesta)

class Almacenview(APIView):
    serializer_class = AlmacenSerializer

    def post(self, request):
        respuesta = ControllerAlmacen.crearalmacen(request)
        return Response(respuesta)

    def get(self, request, id_almacen=None):
        respuesta = ControllerAlmacen.listaralmacen(id_almacen)
        return Response(respuesta)

class OrdenTrabajoTipoview(APIView):
    serializer_class = OrdenTrabajoTipoSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoTipo.crearordentrabajotipo(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_tipo=None):
        respuesta = ControllerOrdenTrabajoTipo.listarordentrabajotipo(id_orden_trabajo_tipo)
        return Response(respuesta)

class OrdenTrabajoPrioridadview(APIView):
    serializer_class = OrdenTrabajoPrioridadSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoPrioridad.crearordentrabajoprioridad(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_prioridad=None):
        respuesta = ControllerOrdenTrabajoPrioridad.listarordentrabajoprioridad(id_orden_trabajo_prioridad)
        return Response(respuesta)

class InventarioValeview(APIView):
    serializer_class = InventarioValeSerializer

    def post(self, request):
        respuesta = ControllerInventarioVale.crearinventariovale(request)
        return Response(respuesta)

    def get(self, request, id_inventario_vale=None):
        respuesta = ControllerInventarioVale.listarinventariovale(id_inventario_vale)
        return Response(respuesta)

class ParteDetalleSurtidoview(APIView):
    serializer_class = ParteDetalleSurtidoSerializer

    def post(self, request):
        respuesta = ControllerParteDetalleSurtido.crearpartedetallesurtido(request)
        return Response(respuesta)

    def get(self, request, id_parte_detalle_surtido=None):
        respuesta = ControllerParteDetalleSurtido.listarpartedetallesurtido(id_parte_detalle_surtido)
        return Response(respuesta)

class OrdenTrabajoEstatusview(APIView):
    serializer_class = OrdenTrabajoEstatusSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoEstatus.crearordentrabajoestatus(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_estatus=None):
        respuesta = ControllerOrdenTrabajoEstatus.listarordentrabajoestatus(id_orden_trabajo_estatus)
        return Response(respuesta)

class OrdenSubestatusview(APIView):
    serializer_class = OrdenSubestatusSerializer

    def post(self, request):
        respuesta = ControllerOrdenSubestatus.crearordensubestatus(request)
        return Response(respuesta)

    def get(self, request, id_orden_subestatus=None):
        respuesta = ControllerOrdenSubestatus.listarordensubestatus(id_orden_subestatus)
        return Response(respuesta)

class OTview(APIView):
    serializer_class = OTSerializer

    def post(self, request):
        respuesta = ControllerOT.crearotr(request)
        return Response(respuesta)

    def get(self, request, id_ot=None):
        respuesta = ControllerOT.listarot(id_ot)
        return Response(respuesta)

class ActOtCodigoview(APIView):
    serializer_class = AtcOtCodigoSerializer

    def post(self, request):
        respuesta = ControllerActOtCodigo.crearactotcodigo(request)
        return Response(respuesta)

    def get(self, request, id_act_ot_codigo=None):
        respuesta = ControllerActOtCodigo.listaractotcodigo(id_act_ot_codigo)
        return Response(respuesta)

class ActOtTipoview(APIView):
    serializer_class = AtcOtTipoSerializer

    def post(self, request):
        respuesta = ControllerActOtTipo.crearactottipo(request)
        return Response(respuesta)

    def get(self, request, id_act_ot_tipo=None):
        respuesta = ControllerActOtTipo.listaractottipo(id_act_ot_tipo)
        return Response(respuesta)

class Eventoview(APIView):
    serializer_class = EventoSerializer

    def post(self, request):
        respuesta = ControllerEvento.crearorevento(request)
        return Response(respuesta)

    def get(self, request, id_evento=None):
        respuesta = ControllerEvento.listarevento(id_evento)
        return Response(respuesta)

class OrdenArchivosview(APIView):
    serializer_class = OrdenArchivosSerializer

    def post(self, request):
        respuesta = ControllerOrdenArchivos.crearordenarchivos(request)
        return Response(respuesta)

    def get(self, request, id_orden_archivos=None):
        respuesta = ControllerOrdenArchivos.listarordenarchivos(id_orden_archivos)
        return Response(respuesta)

class OrdenTrabajoParteview(APIView):
    serializer_class = OrdenTrabajoParteSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoParte.crearordentrabajoparte(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_parte=None):
        respuesta = ControllerOrdenTrabajoParte.listarordentrabajoparte(id_orden_trabajo_parte)
        return Response(respuesta)

class TareaOdenTrabajoview(APIView):
    serializer_class = TareaOrdenTrabajoSerializer

    def post(self, request):
        respuesta = ControllerTareaOrdenTrabajo.creartareaordentrabajo(request)
        return Response(respuesta)

    def get(self, request, id_tarea_orden_trabajo=None):
        respuesta = ControllerTareaOrdenTrabajo.listartareaordentrabajo(id_tarea_orden_trabajo)
        return Response(respuesta)

class TipoCambioview(APIView):
    serializer_class = TipoCambioSerializer

    def post(self, request):
        respuesta = ControllerTipoCambio.creartipocambio(request)
        return Response(respuesta)

    def get(self, request, id_tipo_cambio=None):
        respuesta = ControllerTipoCambio.listartipocambio(id_tipo_cambio)
        return Response(respuesta)


class OrdenTrabajoCompletaview(APIView):
    serializer_class = OrdenTrabajoCompletaSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoCompleta.crearordentrabajocompleta(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_completa=None):
        respuesta = ControllerOrdenTrabajoCompleta.listarordentrabajocompleta(id_orden_trabajo_completa)
        return Response(respuesta)

class Rcaview(APIView):
    serializer_class = RCASerializer

    def post(self, request):
        respuesta = ControllerRca.crearrca(request)
        return Response(respuesta)

    def get(self, request, id_rca=None):
        respuesta = ControllerRca.listarrca(id_rca)
        return Response(respuesta)


class RcaAccionPreventivaview(APIView):
    serializer_class = RcaAccionPreventivaSerializer

    def post(self, request):
        respuesta = ControllerRcaAccionPreventiva.crearrcaaccionpreventiva(request)
        return Response(respuesta)

    def get(self, request, id_rca_accion_preventiva=None):
        respuesta = ControllerRcaAccionPreventiva.listarrcaaccionpreventiva(id_rca_accion_preventiva)
        return Response(respuesta)

class RcaPreventiveStatusview(APIView):
    serializer_class = RcaPreventiveStatusSerializer

    def post(self, request):
        respuesta = ControllerRcaPreventiveStatus.crearrcapreventivestatus(request)
        return Response(respuesta)

    def get(self, request, id_rca_preventive_status=None):
        respuesta = ControllerRcaPreventiveStatus.listarrcapreventivestatus(id_rca_preventive_status)
        return Response(respuesta)

class RcaStatusview(APIView):
    serializer_class = RcaStatusSerializer

    def post(self, request):
        respuesta = ControllerRcaStatus.crearrcastatus(request)
        return Response(respuesta)

    def get(self, request, id_rca_status=None):
        respuesta = ControllerRcaStatus.listarrcastatus(id_rca_status)
        return Response(respuesta)

class RcaTipoAccionview(APIView):
    serializer_class = RcaTipoAccionSerializer

    def post(self, request):
        respuesta = ControllerRcaTipoAccion.crearrcatipoacion(request)
        return Response(respuesta)

    def get(self, request, id_rca_tipo_accion=None):
        respuesta = ControllerRcaTipoAccion.listarrcatipoaccion(id_rca_tipo_accion)
        return Response(respuesta)


class ModoDeteccionview(APIView):
    serializer_class = ModoDeteccionSerializer

    def post(self, request):
        respuesta = ControllerModoDeteccion.crearmododeteccion(request)
        return Response(respuesta)

    def get(self, request, id_modo_deteccion=None):
        respuesta = ControllerModoDeteccion.listarmododeteccion(id_modo_deteccion)
        return Response(respuesta)


class ActividadMantenimientoview(APIView):
    serializer_class = ActividadMantenimientoSerializer

    def post(self, request):
        respuesta = ControllerActividadMantenimiento.crearactividadmantenimiento(request)
        return Response(respuesta)

    def get(self, request, id_actividad_mantenimiento=None):
        respuesta = ControllerActividadMantenimiento.listaractividadmantenimiento(id_actividad_mantenimiento)
        return Response(respuesta)

class UsuarioRevisarview(APIView):
    serializer_class = UsuarioRevisarSerializer

    def post(self, request):
        respuesta = ControllerUsuarioRevisar.crearusuariorevisar(request)
        return Response(respuesta)

    def get(self, request, id_usuario_revisar=None):
        respuesta = ControllerUsuarioRevisar.listarusuariorevisar(id_usuario_revisar)
        return Response(respuesta)

class OrdenTrabajoRevisadaview(APIView):
    serializer_class = OrdenTrabajoRevisadaSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoRevisada.crearordentrabajorevisada(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_revisada=None):
        respuesta = ControllerOrdenTrabajoRevisada.listarordentrabajorevisada(id_orden_trabajo_revisada)
        return Response(respuesta)

class RutaEstatusview(APIView):
    serializer_class = RutaEstatusSerializer

    def post(self, request):
        respuesta = ControllerRutaEstatus.crearrutaestatus(request)
        return Response(respuesta)

    def get(self, request, id_ruta_estatus=None):
        respuesta = ControllerRutaEstatus.listarrutaestatus(id_ruta_estatus)
        return Response(respuesta)

class Rutaview(APIView):
    serializer_class = RutaSerializer

    def post(self, request):
        respuesta = ControllerRuta(request)
        return Response(respuesta)

    def get(self, request, id_ruta=None):
        respuesta = ControllerRuta.listarruta(id_ruta)
        return Response(respuesta)

class RutaEquipoview(APIView):
    serializer_class = RutaEquipoSerializer

    def post(self, request):
        respuesta = ControllerRutaEquipo.crearrutaequipo(request)
        return Response(respuesta)

    def get(self, request, id_ruta_equipo=None):
        respuesta = ControllerRutaEquipo.listarusuariorevisar(id_ruta_equipo)
        return Response(respuesta)

class RutaCondicionview(APIView):
    serializer_class = RutaCondicionSerializer

    def post(self, request):
        respuesta = ControllerRutaCondicion.crearrutacondicion(request)
        return Response(respuesta)

    def get(self, request, id_ruta_condicion=None):
        respuesta = ControllerRutaCondicion.listarrutacondicion(id_ruta_condicion)
        return Response(respuesta)

class RutaCondicionUnidadview(APIView):
    serializer_class = RutaCondicionUnidadSerializer

    def post(self, request):
        respuesta = ControllerRutaCondicionUnidad.crearrutacondicionunidad(request)
        return Response(respuesta)

    def get(self, request, id_ruta_condicion_unidad=None):
        respuesta = ControllerRutaCondicionUnidad.listarrutacondicionunidad(id_ruta_condicion_unidad)
        return Response(respuesta)

class RutaEquipoComponenteview(APIView):
    serializer_class = RutaEquipoComponenteSerializer

    def post(self, request):
        respuesta = ControllerRutaEquipoComponente.crearrutaequipocomponente(request)
        return Response(respuesta)

    def get(self, request, id_ruta_equipo_componente=None):
        respuesta = ControllerRutaEquipoComponente.listarrutaequipocomponente(id_ruta_equipo_componente)
        return Response(respuesta)

class RutaSetPointOperadorview(APIView):
    serializer_class = RutaSetPointOperadorSerializer

    def post(self, request):
        respuesta = ControllerRutaSetPointOperador.crearrutasetpointoperador(request)
        return Response(respuesta)

    def get(self, request, id_ruta_set_point_operador=None):
        respuesta = ControllerRutaSetPointOperador.listarrutasetoperador(id_ruta_set_point_operador)
        return Response(respuesta)

class RutaSetPointview(APIView):
    serializer_class = RutaSetPointSerializer

    def post(self, request):
        respuesta = ControllerRutaSetPoint.crearrutasetpoint(request)
        return Response(respuesta)

    def get(self, request, id_ruta_set_point=None):
        respuesta = ControllerRutaSetPoint.listarrutasetpoint(id_ruta_set_point)
        return Response(respuesta)

class OrdenTrabajoRutaview(APIView):
    serializer_class = OrdenTrabajoRutaSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoRuta.crearordentrabajoruta(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_ruta=None):
        respuesta = ControllerOrdenTrabajoRuta.listarordentrabajoruta(id_orden_trabajo_ruta)
        return Response(respuesta)

class Checklistview(APIView):
    serializer_class = ChecklistSerializer

    def post(self, request):
        respuesta = ControllerChecklist.crearchecklist(request)
        return Response(respuesta)

    def get(self, request, id_checklist=None):
        respuesta = ControllerChecklist.listarchecklist(id_checklist)
        return Response(respuesta)

class ChecklistEquipoview(APIView):
    serializer_class = ChecklistEquipoSerializer

    def post(self, request):
        respuesta = ControllerChecklistEquipo.crearchecklistequipo(request)
        return Response(respuesta)

    def get(self, request, id_checklist_equipo=None):
        respuesta = ControllerChecklistEquipo.listarchecklistequipo(id_checklist_equipo)
        return Response(respuesta)

class OrdenTrabajoRutaSetPointview(APIView):
    serializer_class = OrdenTrabajoRutaSetPointSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoRutaSetPoint.crearordentrabajorutasetpoint(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_ruta_set_point=None):
        respuesta = ControllerOrdenTrabajoRutaSetPoint.listarordentrabajorutasetpoint(id_orden_trabajo_ruta_set_point)
        return Response(respuesta)

class ChecklistAspectoview(APIView):
    serializer_class = ChecklistAspectoSerializer

    def post(self, request):
        respuesta = ControllerChecklistAspecto.crearchecklistaspecto(request)
        return Response(respuesta)

    def get(self, request, id_checklist_aspecto=None):
        respuesta = ControllerChecklistAspecto.listarchecklistaspecto(id_checklist_aspecto)
        return Response(respuesta)

class ChecklistInstruccionview(APIView):
    serializer_class = ChecklistInstruccionSerializer

    def post(self, request):
        respuesta = ControllerChecklistInstruccion.crearchecklistInstruccion(request)
        return Response(respuesta)

    def get(self, request, id_checklist_instruccion=None):
        respuesta = ControllerChecklistInstruccion.listarchecklistinstruccion(id_checklist_instruccion)
        return Response(respuesta)

class ChecklistAspectoCopiadoview(APIView):
    serializer_class = ChecklistAspectoCopiadoSerializer

    def post(self, request):
        respuesta = ControllerChecklistAspectoCopiado.crearchecklistaspectocopiado(request)
        return Response(respuesta)

    def get(self, request, id_checklist_aspecto_copiado=None):
        respuesta = ControllerChecklistAspectoCopiado.listarchecklistaspectocopiado(id_checklist_aspecto_copiado)
        return Response(respuesta)

class Chkview(APIView):
    serializer_class = ChkSerializer

    def post(self, request):
        respuesta = ControllerChk.crearchk(request)
        return Response(respuesta)

    def get(self, request, id_chk=None):
        respuesta = ControllerChk.listarchecklistchk(id_chk)
        return Response(respuesta)

class ChkEquipoview(APIView):
    serializer_class = ChkEquipoSerializer

    def post(self, request):
        respuesta = ControllerChkEquipo.crearchkequipo(request)
        return Response(respuesta)

    def get(self, request, id_chk_equipo=None):
        respuesta = ControllerChkEquipo.listarchecklistequipo(id_chk_equipo)
        return Response(respuesta)

class ChkAspectoview(APIView):
    serializer_class = ChkAspectoSerializer

    def post(self, request):
        respuesta = ControllerChkAspecto.crearchkaspecto(request)
        return Response(respuesta)

    def get(self, request, id_chk_aspecto=None):
        respuesta = ControllerChkAspecto.listarchecklistaspecto(id_chk_aspecto)
        return Response(respuesta)

class ChkInstruccionview(APIView):
    serializer_class = ChkInstruccionSerializer

    def post(self, request):
        respuesta = ControllerChkIntruccion.crearchkinstruccion(request)
        return Response(respuesta)

    def get(self, request, id_chk_instruccion=None):
        respuesta = ControllerChkIntruccion.listarcheckinstruccion(id_chk_instruccion)
        return Response(respuesta)

class OrdenTrabajoChecklistview(APIView):
    serializer_class = OrdenTrabajoChecklistSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoChecklist.crearordentrabajochecklist(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_checklist=None):
        respuesta = ControllerOrdenTrabajoChecklist.listarcheckinstruccion(id_orden_trabajo_checklist)
        return Response(respuesta)