from inflection import re
from rest_framework import generics, serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .controller.ControllerCentroCosto import ControllerCentroCosto
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
from .controller.ControllerDashboardAjuste import ControllerDashboardAjuste
from .controller.ControllerDashboardMtbf import ControllerDashboardMtbf
from .controller.ControllerAccionCorrectiva import ControllerAccionCorrectiva
from .controller.ControllerActEquipo import ControllerActEquipo
from .controller.ControllerCausaRaiz import ControllerCausaRaiz
from .controller.ControllerCuentaCc import ControllerCuentaCc
from .controller.ControllerEmpaqueTipo import ControllerEmpaqueTipo
from .controller.ControllerEmpaqueCategoria import ControllerEmpaqueCategoria
from .controller.ControllerEmpaque import ControllerEmpaque
from .controller.ControllerEmpaqueStockEntrada import ControllerEmpaqueStockEntrada
from .controller.ControllerEmpaqueStock import ControllerEmpaqueStock
from .controller.ControllerEmpaqueStockDetalle import ControllerEmpaqueStockDetalle
from .controller.ControllerEmpaqueStockAjuste import ControllerEmpaqueStockAjuste
from .controller.ControllerEmpaqueStockOrdenCompra import ControllerEmpaqueStockOrdenCompra
from .controller.ControllerEmpaqueStockSalida import ControllerEmpaqueStockSalida
from .controller.ControllerEmpaqueVale import ControllerEmpaqueVale
from .controller.ControllerOrdenArchivos import ControllerOrdenArchivos
from .controller.ControllerOrdenInventario import ControllerOrdenInventario
from .controller.ControllerMes import ControllerMes
from .controller.ControllerMantenimieto import ControllerMantenimiento
from .controller.ControllerMenu import ControllerMenu
from .controller.ControllerParte import ControllerParte
from .controller.ControllerProbEquipo import ControllerProbEquipo
from .controller.ControllerRequisicionEstatus import ControllerRequisicionEstatus
from .controller.ControllerRequisicion import ControllerRequisicion
from .controller.ControllerSatisfaccion import ControllerSatisfaccion
from .controller.ControllerSubmenu import ControllerSubmenu
from .controller.ControllerSuscripcion import ControllerSuscripcion
from .controller.ControllerToken import ControllerToken
from .controller.ControllerUsuario_ import ControllerUsuario_
from .controller.ControllerCriticidad import ControllerCriticidad
from .controller.ControllerEstadoMaterial import ControllerEstadoMaterial
from .controller.ControllerEstadoPaquete import ControllerEstadoPaquete
from .controller.ControllerEstadoSello import ControllerEstadoSello
from .controller.ControllerGiro import ControllerGiro
from .controller.ControllerNivelMro import ControllerNivelMro
from .controller.ControllerNivelGastos import ControllerNivelGastos
from .controller.ControllerOrdenDeCompraEstado import ControllerOrdenDeCompraEstado
from .controller.ControllerOrdenDeCompraAccion import ControllerOrdenDeCompraAccion
from .controller.ControllerOrdenDeCompraProveedor import ControllerOrdenDeCompraProveedor
from .controller.ControllerOrdenDeCompra import ControllerOrdenDeCompra
from .controller.ControllerOrdenDeCompraProducto import ControllerOrdenDeCompraProducto
from .controller.ControllerOrdenDeCompraCotizacionProducto import ControllerOrdenDeCompraCotizacionProducto
from .controller.ControllerOrdenDeCompraArchivo import ControllerOrdenDeCompraArchivo
from .controller.ControllerOrdenDeCompraArchivoProveedor import ControllerOrdenDeCompraArchivoProveedor
from .controller.ControllerOrdenDeCompraCotizacion import ControllerOrdenDeCompraCotizacion
from .controller.ControllerOrdenDeCompraArchivoCosto import ControllerOrdenDeCompraArchivoCosto
from .controller.ControllerOrdenDeCompraEmailVisto import ControllerOrdenDeCompraEmailVisto
from .controller.ControllerOrdenDeCompraHistorial import ControllerOrdenDeCompraHistorial
from .controller.ControllerOrdenDeCompraMensaje import ControllerOrdenDeCompraMensaje
from .controller.ControllerOrdenDeCompraPresupuesto import ControllerOrdenDeCompraPresupuesto
from .controller.ControllerEstadoProductoRecibido import ControllerEstadoProductoRecibido
from .controller.ControllerOcChat import ControllerOcChat
from .controller.ControllerOcEstado import ControllerOcEstado
from .controller.ControllerOcMensajeProveedor import ControllerOcMensajeProveedor
from .controller.ControllerOcMensajeUsuario import ControllerOcMensajeUsuario
from .controller.ControllerOcPresupuestoCostos import ControllerOcPresupuestoCostos
from .controller.ControllerOcProd import ControllerOcProd
from .controller.ControllerOcProv import ControllerOcProv
from .controller.ControllerOrdenDeCompraAprovada import ControllerOrdenDeCompraAprovada
from .controller.ControllerProveedorGiro import ControllerProveedorGiro
from .controller.ControllerRequisicionAprovada import ControllerRequisicionAprovada
from .controller.ControllerUsuarioContrasena import ControllerUsuarioContrasena
from .controller.ControllerUsuarioEvento import ControllerUsuarioEvento
from .controller.ControllerUsuarioMro import ControllerUsuarioMro
from .controller.ControllerUsuarioSesion import ControllerUsuarioSesion
from .controller.ControllerUsuarioActivoeam import ControllerUsuarioActivoeam

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AccionCorrectivaSerializer, ActEquipoSerializer, ActividadMantenimientoSerializer, AlmacenSerializer, AtcOtCodigoSerializer, AtcOtTipoSerializer, CausaRaizSerializer, ChecklistAspectoCopiadoSerializer, ChecklistAspectoSerializer, ChecklistEquipoSerializer, ChecklistInstruccionSerializer, ChecklistSerializer, ChkAspectoSerializer, ChkEquipoSerializer, ChkInstruccionSerializer, ChkSerializer, ClaseEquipoSerializer, CriticidadSerializer, CuentaCcSerializer, DashboardAjusteSerializer, DashboardmtbfSerializer, DevolucionSerializer, EmpaqueCategoriaSerializer, EmpaqueSerializer, EmpaqueStockAjusteSerializer, EmpaqueStockDetalleSerializer, EmpaqueStockEntradaSerializer, EmpaqueStockOrdenCompraSerializer, EmpaqueStockSalidaSerializer, EmpaqueStockSerializer, EmpaqueTipoSerializer, EmpaqueValeSerializer, EquipoCategoriaEstatusSerializaer, EquipoCategoriaIconoSerializaer, EquipoEstatusSerializer, EquipoSerializer, EstadoMaterialSerializer, EstadoPaqueteSerializer, EstadoSelloSerializer, EventoSerializer, GiroSerializer, HerramientaMovimientoSerializer, HerramientaSerializer, InstalacionIconoSerializer, InstalacionSerializer, InventarioAjusteSerializer, InventarioTipoSerializer, InventarioValeSerializer, JornadaHorasSerializer, JornadaSerializer, CentroCostoSerializer, ClienteSerializer, Contacto_ProveedorSerializer, Departamento_TurnoSerializer, EstatusSerializer, IdiomaSerializer, Inventario_CategoriaSerializer, MantenimientoSerializer, MenuSerializer, MesSerializer, ModeloIconoSerializer, ModeloSerializer, ModoDeteccionSerializer, NivelGastosSerializer, NivelMroSerializer, OTSerializer, OrdenArchivosSerializer, OrdenDeCompraAccionSerializer, OrdenDeCompraArchivoCostoSerializer, OrdenDeCompraArchivoProveedorSerializer, OrdenDeCompraArchivoSerializer, OrdenDeCompraCotizacionSerializer, OrdenDeCompraEmailVistoSerializer, OrdenDeCompraEstadoSerializer, OrdenDeCompraHistorialSerializer, OrdenDeCompraMensajeSerializer, OrdenDeCompraPresupuestoSerializer, OrdenDeCompraProductoSerializer, OrdenDeCompraProveedorSerializer, OrdenDeCompraSerializer, OrdenInventarioSerializer, OrdenSubestatusSerializer, OrdenTrabajoChecklistSerializer, OrdenTrabajoCompletaSerializer, OrdenTrabajoEstatusSerializer, OrdenTrabajoParteSerializer, OrdenTrabajoPrioridadSerializer, OrdenTrabajoRevisadaSerializer, OrdenTrabajoRutaSerializer, OrdenTrabajoRutaSetPointSerializer, OrdenTrabajoTipoSerializer, ParteDetalleSerializer, ParteDetalleSurtidoSerializer, ParteEstatusSerializer, ParteSerializer, ProbEquipoSerializer, PuestoSerializer, RCASerializer, RcaAccionPreventivaSerializer, RcaPreventiveStatusSerializer, RcaStatusSerializer, RcaTipoAccionSerializer, RequisicionEstatusSerializer, RequisicionSerializer, RolSerializer, RutaCondicionSerializer, RutaCondicionUnidadSerializer, RutaEquipoComponenteSerializer, RutaEquipoSerializer, RutaEstatusSerializer, RutaSerializer, RutaSetPointOperadorSerializer, RutaSetPointSerializer, SatisfaccionSerializer, ScopeSerializer, StockAjusteSerializer, StockDetalleSerializer, StockEntradaSerializer, StockSerializer, SubmenuSerializer, SuscripcionSerializer, TareaOrdenTrabajoSerializer, Tipo_RolSerializer, TipoCambioSerializer, TokenSerializer, TurnoSerializer, UserSerializer, AuthTokenSerializer, DepartamentoSerializer, Usuario_Serializer, UsuarioRevisarSerializer, UsuarioSerializer, CentroCostoSerializer, ProveedorSerializer
from .serializers import Usuario_Lat_Lng_Serializer, TurnoSerializer, UnidadSerializer, setup_Serializer, EquipoCategoriaSerializer, HerramientaHistorialSerializer

from .models import Estado_Producto_Recibido, Modelo, Oc_Chat, Oc_Estado, Oc_Mensaje_Proveedor, Oc_Mensaje_Usuario, Oc_Presupuesto_Costos, Oc_Prod, Oc_Prov, Orden_De_Compra_Aprovada, Proveedor_Giro, Requisicion_Aprovada, Unidad, Usuario_Activoeam, Usuario_Contrasena, Usuario_Evento, Usuario_Mro, Usuario_Sesion

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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = DepartamentoSerializer

    def post(self, request):
        respuesta = ControllerDept.creardepartamento(request)
        return Response(respuesta)

    def get(self, request, id_departamento=None):
        respuesta = ControllerDept.listardepartamento(id_departamento)
        return Response(respuesta)

class Jornadaview(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = TurnoSerializer

    def post(self, request):
        respuesta = ControllerTurno.crearturno(request)
        return Response(respuesta)

    def get(self, request, id_turno=None):
        respuesta = ControllerTurno.listarturno(id_turno)
        return Response(respuesta)


class Tipo_Rolview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Tipo_RolSerializer

    def post(self, request):
        respuesta = ControllerTipoRol.creartipo_rol(request)
        return Response(respuesta)

    def get(self, request, id_tipo_rol=None):
        respuesta = ControllerTipoRol.listartipo_rol(id_tipo_rol)
        return Response(respuesta)


class Scopeview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ScopeSerializer

    def post(self, request):
        respuesta = ControllerScope.crearscope(request)
        return Response(respuesta)

    def get(self, request, id_scope=None):
        respuesta = ControllerScope.listarscope(id_scope)
        return Response(respuesta)


class Estatusview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EstatusSerializer

    def post(self, request):
        respuesta = ControllerEstatus.crearestatus(request)
        return Response(respuesta)

    def get(self, request, id_estatus=None):
        respuesta = ControllerEstatus.listarestatus(id_estatus)
        return Response(respuesta)


class Idiomaview(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = RolSerializer

    def post(self, request):
        respuesta = ControllerRol.crearrol(request)
        return Response(respuesta)

    def get(self, request, id_rol=None):
        respuesta = ControllerRol.listarrol(id_rol)
        return Response(respuesta)


class Departamento_Turnoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Departamento_TurnoSerializer

    def post(self, request):
        respuesta = ControllerDeptTurno.creardepartamento_turno(request)
        return Response(respuesta)

    def get(self, request, id_departamento_turno=None):
        respuesta = ControllerDeptTurno.listardepartamento_turno(
            id_departamento_turno)
        return Response(respuesta)


class Puestoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PuestoSerializer

    def post(self, request):
        respuesta = ControllerPuesto.crearpuesto(request)
        return Response(respuesta)

    def get(self, request, id_puesto=None):
        respuesta = ControllerPuesto.listarpuesto(id_puesto)
        return Response(respuesta)


class Usuarioview(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    def get(self, request, p_nombre=None):
        respuesta = ControllerUsuario.verPerfil(p_nombre)
        return Response(respuesta)


class Historial_TurnoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        respuesta = ControllerHistTurno.crearhistorial_turno(request)
        return Response(respuesta)

    def get(self, request, id_historial_turno=None):
        respuesta = ControllerHistTurno.listarhistorialturno(
            id_historial_turno)
        return Response(respuesta)

class JornadaHorasview(APIView):
    permission_classes = [IsAuthenticated]
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
        
class Loginview(APIView):
    def post(self, request):
        respuesta = ControllerLogin.login(request)
        return Response(respuesta)


class Unidadview(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = EquipoCategoriaEstatusSerializaer

    def post(self, request):
        respuesta = ControllerEquipoCategiriaEstatus.crearequipocategoriaestatus(request)
        return Response(respuesta)

    def get(self, request, id_estatus=None):
        respuesta = ControllerEquipoCategiriaEstatus.listarequipocategoriaestatus(id_estatus)
        return Response(respuesta)


class EquipoCategoriaview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipoCategoriaSerializer

    def post(self, request):
        respuesta = ControllerEquipoCategoria.crearequipocategoria(request)
        return Response(respuesta)

    def get(self, request, id_equipo_categoria=None):
        respuesta = ControllerEquipoCategoria.listarequipocategoria(id_equipo_categoria)
        return Response(respuesta)

class ClaseEquipoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClaseEquipoSerializer

    def post(self, request):
        respuesta = ControllerClaseEquipo.crearclaseequipo(request)
        return Response(respuesta)

    def get(self, request, id_equipo_categoria=None):
        respuesta = ControllerClaseEquipo.listarclaseequipo(id_equipo_categoria)
        return Response(respuesta)

class ModeloIconoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ModeloIconoSerializer

    def post(self, request):
        respuesta = ControllerModeloIcono.crearmodeloicono(request)
        return Response(respuesta)

    def get(self, request, id_modelo_icono=None):
        respuesta = ControllerModeloIcono.listarmodeloicono(id_modelo_icono)
        return Response(respuesta)
    
class EquipoCategoriaIconoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipoCategoriaIconoSerializaer

    def post(self, request):
        respuesta = ControllerEquipoCategoriaIcono.crearequipocategoriaicono(request)
        return Response(respuesta)

    def get(self, request, id_equipo_categoria_icono=None):
        respuesta = ControllerEquipoCategoriaIcono.listarequipocategoriaicono(id_equipo_categoria_icono)
        return Response(respuesta)

class Modeloview(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = InstalacionIconoSerializer

    def post(self, request):
        respuesta = ControllerInstalacionIcono.crearinstalacionicono(request)
        return Response(respuesta)

    def get(self, request, id_instalacion_icono=None):
        respuesta = ControllerInstalacionIcono.listarinstalacionicono(id_instalacion_icono)
        return Response(respuesta)

class InstalacionView(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = EquipoEstatusSerializer

    def post(self, request):
        respuesta = ControllerEquipoEstatus.crearequipoestatus(request)
        return Response(respuesta)

    def get(self, request, id_equipo_estatus=None):
        respuesta = ControllerEquipoEstatus.listarequipoestatus(id_equipo_estatus)
        return Response(respuesta)

class Equipoview(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = HerramientaMovimientoSerializer

    def post(self, request):
        respuesta = ControllerHerramientaMovimiento.crearherramientamovimiento(request)
        return Response(respuesta)

    def get(self, request, id_herramienta_movimiento=None):
        respuesta = ControllerHerramientaMovimiento.listarherramientamovimiento(id_herramienta_movimiento)
        return Response(respuesta)

class Herramientaview(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = HerramientaHistorialSerializer

    def post(self, request):
        respuesta = ControllerHerramientaHistorial.crearherramientahistorial(request)
        return Response(respuesta)

    def get(self, request, id_herramienta_historial=None):
        respuesta = ControllerHerramientaHistorial.listarherramientahistorial(id_herramienta_historial)
        return Response(respuesta)

class InventarioTipoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InventarioTipoSerializer

    def post(self, request):
        respuesta = ControllerInventarioTipo.crearinventarioTipo(request)
        return Response(respuesta)

    def get(self, request, id_inventario_tipo=None):
        respuesta = ControllerInventarioTipo.listarinventariotipo(id_inventario_tipo)
        return Response(respuesta)

class Stockview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StockSerializer

    def post(self, request):
        respuesta = ControllerStock.crearstock(request)
        return Response(respuesta)

    def get(self, request, id_stock=None):
        respuesta = ControllerStock.listarstock(id_stock)
        return Response(respuesta)

class StockDetalleview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StockDetalleSerializer

    def post(self, request):
        respuesta = ControllerStockDetalle.crearstockdetalle(request)
        return Response(respuesta)

    def get(self, request, id_stock_detalle=None):
        respuesta = ControllerStockDetalle.listarstockDetalle(id_stock_detalle)
        return Response(respuesta)

class StockEntradaview(APIView):
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    serializer_class = StockEntradaSerializer

    def post(self, request):
        respuesta = ControllerStockEntrada.crearstockentrada(request)
        return Response(respuesta)

    def get(self, request, id_stock_entrada=None):
        respuesta = ControllerStockEntrada.listarstockentrada(id_stock_entrada)
        return Response(respuesta)
              
class StockAjusteview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StockAjusteSerializer

    def post(self, request):
        respuesta = ControllerStockAjuste.crearstockajuste(request)
        return Response(respuesta)

    def get(self, request, id_stock_ajuste=None):
        respuesta = ControllerStockAjuste.listarstockajuste(id_stock_ajuste)
        return Response(respuesta)
              
class ParteEstatusview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ParteEstatusSerializer

    def post(self, request):
        respuesta = ControllerParteEstatus
        return Response(respuesta)

    def get(self, request, id_stock_ajuste=None):
        respuesta = ControllerStockAjuste.listarstockajuste(id_stock_ajuste)
        return Response(respuesta)

class InventarioAjusteview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InventarioAjusteSerializer

    def post(self, request):
        respuesta = ControllerInventarioAjuste.crearinventarioajuste(request)
        return Response(respuesta)

    def get(self, request, id_inventario_ajuste=None):
        respuesta = ControllerInventarioAjuste.listarinventarioajuste(id_inventario_ajuste)
        return Response(respuesta)

class ParteDetalleview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ParteDetalleSerializer

    def post(self, request):
        respuesta = ControllerParteDetalle.crearpartedetalle(request)
        return Response(respuesta)

    def get(self, request, id_parte_detalle=None):
        respuesta =ControllerParteDetalle.listarpartedetalle(id_parte_detalle)
        return Response(respuesta)
        
class Devolucionview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DevolucionSerializer

    def post(self, request):
        respuesta = ControllerDevolucion.creardevolucion(request)
        return Response(respuesta)

    def get(self, request, id_devolucion=None):
        respuesta = ControllerDevolucion.listardevolcion(id_devolucion)
        return Response(respuesta)

class Almacenview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AlmacenSerializer

    def post(self, request):
        respuesta = ControllerAlmacen.crearalmacen(request)
        return Response(respuesta)

    def get(self, request, id_almacen=None):
        respuesta = ControllerAlmacen.listaralmacen(id_almacen)
        return Response(respuesta)

class OrdenTrabajoTipoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenTrabajoTipoSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoTipo.crearordentrabajotipo(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_tipo=None):
        respuesta = ControllerOrdenTrabajoTipo.listarordentrabajotipo(id_orden_trabajo_tipo)
        return Response(respuesta)

class OrdenTrabajoPrioridadview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenTrabajoPrioridadSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoPrioridad.crearordentrabajoprioridad(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_prioridad=None):
        respuesta = ControllerOrdenTrabajoPrioridad.listarordentrabajoprioridad(id_orden_trabajo_prioridad)
        return Response(respuesta)

class InventarioValeview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InventarioValeSerializer

    def post(self, request):
        respuesta = ControllerInventarioVale.crearinventariovale(request)
        return Response(respuesta)

    def get(self, request, id_inventario_vale=None):
        respuesta = ControllerInventarioVale.listarinventariovale(id_inventario_vale)
        return Response(respuesta)

class ParteDetalleSurtidoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ParteDetalleSurtidoSerializer

    def post(self, request):
        respuesta = ControllerParteDetalleSurtido.crearpartedetallesurtido(request)
        return Response(respuesta)

    def get(self, request, id_parte_detalle_surtido=None):
        respuesta = ControllerParteDetalleSurtido.listarpartedetallesurtido(id_parte_detalle_surtido)
        return Response(respuesta)

class OrdenTrabajoEstatusview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenTrabajoEstatusSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoEstatus.crearordentrabajoestatus(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_estatus=None):
        respuesta = ControllerOrdenTrabajoEstatus.listarordentrabajoestatus(id_orden_trabajo_estatus)
        return Response(respuesta)

class OrdenSubestatusview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenSubestatusSerializer

    def post(self, request):
        respuesta = ControllerOrdenSubestatus.crearordensubestatus(request)
        return Response(respuesta)

    def get(self, request, id_orden_subestatus=None):
        respuesta = ControllerOrdenSubestatus.listarordensubestatus(id_orden_subestatus)
        return Response(respuesta)

class OTview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OTSerializer

    def post(self, request):
        respuesta = ControllerOT.crearotr(request)
        return Response(respuesta)

    def get(self, request, id_ot=None):
        respuesta = ControllerOT.listarot(id_ot)
        return Response(respuesta)

class ActOtCodigoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AtcOtCodigoSerializer

    def post(self, request):
        respuesta = ControllerActOtCodigo.crearactotcodigo(request)
        return Response(respuesta)

    def get(self, request, id_act_ot_codigo=None):
        respuesta = ControllerActOtCodigo.listaractotcodigo(id_act_ot_codigo)
        return Response(respuesta)

class ActOtTipoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AtcOtTipoSerializer

    def post(self, request):
        respuesta = ControllerActOtTipo.crearactottipo(request)
        return Response(respuesta)

    def get(self, request, id_act_ot_tipo=None):
        respuesta = ControllerActOtTipo.listaractottipo(id_act_ot_tipo)
        return Response(respuesta)

class Eventoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventoSerializer

    def post(self, request):
        respuesta = ControllerEvento.crearorevento(request)
        return Response(respuesta)

    def get(self, request, id_evento=None):
        respuesta = ControllerEvento.listarevento(id_evento)
        return Response(respuesta)

class OrdenArchivosview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenArchivosSerializer

    def post(self, request):
        respuesta = ControllerOrdenArchivos.crearordenarchivos(request)
        return Response(respuesta)

    def get(self, request, id_orden_archivos=None):
        respuesta = ControllerOrdenArchivos.listarordenarchivos(id_orden_archivos)
        return Response(respuesta)

class OrdenTrabajoParteview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenTrabajoParteSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoParte.crearordentrabajoparte(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_parte=None):
        respuesta = ControllerOrdenTrabajoParte.listarordentrabajoparte(id_orden_trabajo_parte)
        return Response(respuesta)

class TareaOdenTrabajoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TareaOrdenTrabajoSerializer

    def post(self, request):
        respuesta = ControllerTareaOrdenTrabajo.creartareaordentrabajo(request)
        return Response(respuesta)

    def get(self, request, id_tarea_orden_trabajo=None):
        respuesta = ControllerTareaOrdenTrabajo.listartareaordentrabajo(id_tarea_orden_trabajo)
        return Response(respuesta)

class TipoCambioview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TipoCambioSerializer

    def post(self, request):
        respuesta = ControllerTipoCambio.creartipocambio(request)
        return Response(respuesta)

    def get(self, request, id_tipo_cambio=None):
        respuesta = ControllerTipoCambio.listartipocambio(id_tipo_cambio)
        return Response(respuesta)

class OrdenTrabajoCompletaview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenTrabajoCompletaSerializer

    def post(self, request):
        respuesta = ControllerOrdenTrabajoCompleta.crearordentrabajocompleta(request)
        return Response(respuesta)

    def get(self, request, id_orden_trabajo_completa=None):
        respuesta = ControllerOrdenTrabajoCompleta.listarordentrabajocompleta(id_orden_trabajo_completa)
        return Response(respuesta)

class Rcaview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RCASerializer

    def post(self, request):
        respuesta = ControllerRca.crearrca(request)
        return Response(respuesta)

    def get(self, request, id_rca=None):
        respuesta = ControllerRca.listarrca(id_rca)
        return Response(respuesta)

class RcaAccionPreventivaview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RcaAccionPreventivaSerializer

    def post(self, request):
        respuesta = ControllerRcaAccionPreventiva.crearrcaaccionpreventiva(request)
        return Response(respuesta)

    def get(self, request, id_rca_accion_preventiva=None):
        respuesta = ControllerRcaAccionPreventiva.listarrcaaccionpreventiva(id_rca_accion_preventiva)
        return Response(respuesta)

class RcaPreventiveStatusview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RcaPreventiveStatusSerializer

    def post(self, request):
        respuesta = ControllerRcaPreventiveStatus.crearrcapreventivestatus(request)
        return Response(respuesta)

    def get(self, request, id_rca_preventive_status=None):
        respuesta = ControllerRcaPreventiveStatus.listarrcapreventivestatus(id_rca_preventive_status)
        return Response(respuesta)

class RcaStatusview(APIView):
    permission_classes = [IsAuthenticated]
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

class DashboardAjusteview(APIView):
    serializer_class = DashboardAjusteSerializer

    def post(self, request):
        respuesta = ControllerDashboardAjuste.creardashboardajuste(request)
        return Response(respuesta)

    def get(self, request, id_dashboard_ajuste=None):
        respuesta = ControllerDashboardAjuste.listardashboardajuste(id_dashboard_ajuste)
        return Response(respuesta)

class DashboardMtbfview(APIView):
    serializer_class = DashboardmtbfSerializer

    def post(self, request):
        respuesta = ControllerDashboardMtbf.creardashboardmtbf(request)
        return Response(respuesta)

    def get(self, request, id_dashboard_mtbf=None):
        respuesta = ControllerDashboardMtbf.listardashboardmtbf(id_dashboard_mtbf)
        return Response(respuesta)

class AccionCorrectivaview(APIView):
    serializer_class = AccionCorrectivaSerializer

    def post(self, request):
        respuesta = ControllerAccionCorrectiva.crearaccioncorrectiva(request)
        return Response(respuesta)

    def get(self, request, id_accion_correctiva=None):
        respuesta = ControllerAccionCorrectiva.listaraccioncorrectiva(id_accion_correctiva)
        return Response(respuesta)

class ActEquipoview(APIView):
    serializer_class = ActEquipoSerializer

    def post(self, request):
        respuesta = ControllerActEquipo.crearactequipo(request)
        return Response(respuesta)

    def get(self, request, id_act_equipo=None):
        respuesta = ControllerActEquipo.listaractequipo(id_act_equipo)
        return Response(respuesta)

class CausaRaizview(APIView):
    serializer_class = CausaRaizSerializer

    def post(self, request):
        respuesta = ControllerCausaRaiz.crearcausaraiz(request)
        return Response(respuesta)

    def get(self, request, id_causa_raiz=None):
        respuesta = ControllerCausaRaiz.listarcausaraiz(id_causa_raiz)
        return Response(respuesta)

class CuentaCcview(APIView):
    serializer_class = CuentaCcSerializer

    def post(self, request):
        respuesta = ControllerCuentaCc.crearcuentacc(request)
        return Response(respuesta)

    def get(self, request, id_cuenta_cc=None):
        respuesta = ControllerCuentaCc.listarcuentacc(id_cuenta_cc)
        return Response(respuesta)

class EmpaqueTipoview(APIView):
    serializer_class = EmpaqueTipoSerializer

    def post(self, request):
        respuesta = ControllerEmpaqueTipo.crearempaquetipo(request)
        return Response(respuesta)

    def get(self, request, id_empaque_tipo=None):
        respuesta = ControllerEmpaqueTipo.listarempaquetipo(id_empaque_tipo)
        return Response(respuesta)

class EmpaqueCategoriaview(APIView):
    serializer_class = EmpaqueCategoriaSerializer

    def post(self, request):
        respuesta = ControllerEmpaqueCategoria.crearempaquecategoria(request)
        return Response(respuesta)

    def get(self, request, id_empaque_categoria=None):
        respuesta = ControllerEmpaqueCategoria.listarempaquecategoria(id_empaque_categoria)
        return Response(respuesta)

class Empaqueview(APIView):
    serializer_class = EmpaqueSerializer

    def post(self, request):
        respuesta = ControllerEmpaque.crearempaque(request)
        return Response(respuesta)

    def get(self, request, id_empaque=None):
        respuesta = ControllerEmpaque.listarempaque(id_empaque)
        return Response(respuesta)

class EmpaqueStockEntradaview(APIView):
    serializer_class = EmpaqueStockEntradaSerializer

    def post(self, request):
        respuesta = ControllerEmpaqueStockEntrada.crearempaquestockentrada(request)
        return Response(respuesta)

    def get(self, request, id_empaque_stock_entrada=None):
        respuesta = ControllerEmpaqueStockEntrada.listarempaquestockentrada(id_empaque_stock_entrada)
        return Response(respuesta)

class EmpaqueStockview(APIView):
    serializer_class = EmpaqueStockSerializer

    def post(self, request):
        respuesta = ControllerEmpaqueStock.crearempaquestock(request)
        return Response(respuesta)

    def get(self, request, id_empaque_stock=None):
        respuesta = ControllerEmpaqueStock.listarempaquestock(id_empaque_stock)
        return Response(respuesta)

class EmpaqueStockDetalleview(APIView):
    serializer_class = EmpaqueStockDetalleSerializer

    def post(self, request):
        respuesta = ControllerEmpaqueStockDetalle.crearempaquestockdetalle(request)
        return Response(respuesta)

    def get(self, request, id_empaque_stock_detalle=None):
        respuesta = ControllerEmpaqueStockDetalle.listarempaquestock(id_empaque_stock_detalle)
        return Response(respuesta)

class EmpaqueStockAjusteview(APIView):
    serializer_class = EmpaqueStockAjusteSerializer

    def post(self, request):
        respuesta = ControllerEmpaqueStockAjuste.crearempaquestockajuste(request)
        return Response(respuesta)

    def get(self, request, id_empaque_stock_ajuste=None):
        respuesta = ControllerEmpaqueStockAjuste.listarempaquestock(id_empaque_stock_ajuste)
        return Response(respuesta)

class EmpaqueStockOrdenCompraview(APIView):
    serializer_class = EmpaqueStockOrdenCompraSerializer

    def post(self, request):
        respuesta = ControllerEmpaqueStockOrdenCompra.crearempaquestockordencompra(request)
        return Response(respuesta)

    def get(self, request, id_empaque_stock_orden_compra=None):
        respuesta = ControllerEmpaqueStockOrdenCompra.listarempaquestockordencompra(id_empaque_stock_orden_compra)
        return Response(respuesta)

class EmpaqueStockSalidaview(APIView):
    serializer_class = EmpaqueStockSalidaSerializer

    def post(self, request):
        respuesta = ControllerEmpaqueStockSalida.crearempaquestock(request)
        return Response(respuesta)

    def get(self, request, id_empaque_stock_salida=None):
        respuesta = ControllerEmpaqueStockSalida.listarempaquestock(id_empaque_stock_salida)
        return Response(respuesta)

class EmpaqueValeview(APIView):
    serializer_class = EmpaqueValeSerializer

    def post(self, request):
        respuesta = ControllerEmpaqueVale.crearempaquevale(request)
        return Response(respuesta)

    def get(self, request, id_empaque_vale=None):
        respuesta = ControllerEmpaqueVale.listarempaquevale(id_empaque_vale)
        return Response(respuesta)

class OrdenArchivosview(APIView):
    serializer_class = OrdenArchivosSerializer

    def post(self, request):
        respuesta = ControllerOrdenArchivos.crearordenarchivos(request)
        return Response(respuesta)

    def get(self, request, id_orden_archivos=None):
        respuesta = ControllerOrdenArchivos.listarordenarchivos(id_orden_archivos)
        return Response(respuesta)

class OrdenInventarioview(APIView):
    serializer_class = OrdenInventarioSerializer

    def post(self, request):
        respuesta = ControllerOrdenInventario.crearordeninventario(request)
        return Response(respuesta)

    def get(self, request, id_orden_inventario=None):
        respuesta = ControllerOrdenInventario.listarordeninventario(id_orden_inventario)
        return Response(respuesta)

class Mesview(APIView):
    serializer_class = MesSerializer

    def post(self, request):
        respuesta = ControllerMes.crearmes(request)
        return Response(respuesta)

class Mantenimientoview(APIView):
    serializer_class = MantenimientoSerializer

    def post(self, request):
        respuesta = ControllerMantenimiento.crearmantenimiento(request)
        return Response(respuesta)

    def get(self, request, id_mantenimiento=None):
        respuesta = ControllerMantenimiento.listarmantenimiento(id_mantenimiento)
        return Response(respuesta)

class Menuview(APIView):
    serializer_class = MenuSerializer

    def post(self, request):
        respuesta = ControllerMenu.crearmenu(request)
        return Response(respuesta)

    def get(self, request, id_menu=None):
        respuesta = ControllerMenu.listarmenu(id_menu)
        return Response(respuesta)

class Parteview(APIView):
    serializer_class = ParteSerializer

    def post(self, request):
        respuesta = ControllerParte.crearparte(request)
        return Response(respuesta)

    def get(self, request, id_parte=None):
        respuesta = ControllerParte.listarparte(id_parte)
        return Response(respuesta)

class ProbEquipoview(APIView):
    serializer_class = ProbEquipoSerializer

    def post(self, request):
        respuesta =ControllerProbEquipo.crearprobequipo(request)
        return Response(respuesta)

    def get(self, request, id_prob_equipo=None):
        respuesta = ControllerProbEquipo.listarprobequipo(id_prob_equipo)
        return Response(respuesta)

class RequisicionEstatusview(APIView):
    serializer_class = RequisicionEstatusSerializer

    def post(self, request):
        respuesta = ControllerRequisicionEstatus.crearrequisicionestatus(request)
        return Response(respuesta)

    def get(self, request, id_requisicion_estatus=None):
        respuesta = ControllerRequisicionEstatus.listarrequisicionestatus(id_requisicion_estatus)
        return Response(respuesta)

class Requisicionview(APIView):
    serializer_class = RequisicionSerializer

    def post(self, request):
        respuesta = ControllerRequisicion.crearrequisicion(request)
        return Response(respuesta)

    def get(self, request, id_requisicion=None):
        respuesta = ControllerRequisicion.listarrequisicion(id_requisicion)
        return Response(respuesta)
        
class Satisfaccionview(APIView):
    serializer_class = SatisfaccionSerializer

    def post(self, request):
        respuesta =ControllerSatisfaccion.crearsatisfaccion(request)
        return Response(respuesta)

    def get(self, request, id_satisfaccion=None):
        respuesta = ControllerSatisfaccion.listarsatisfaccion(id_satisfaccion)
        return Response(respuesta)

class Submenuview(APIView):
    serializer_class = SubmenuSerializer

    def post(self, request):
        respuesta = ControllerSubmenu.crearsubmenu(request)
        return Response(respuesta)

    def get(self, request, id_submenu=None):
        respuesta = ControllerSubmenu.listarsubmenu(id_submenu)
        return Response(respuesta)

class Suscripcionview(APIView):
    serializer_class = SuscripcionSerializer

    def post(self, request):
        respuesta = ControllerSuscripcion.crearsuscripcion(request)
        return Response(respuesta)

    def get(self, request, id_suscripcion=None):
        respuesta = ControllerSuscripcion.listarsuscripcion(id_suscripcion)
        return Response(respuesta)

class Tokenview(APIView):
    serializer_class = TokenSerializer

    def post(self, request):
        respuesta = ControllerToken.creartoken(request)
        return Response(respuesta)

class Usuario_view(APIView):
    serializer_class = Usuario_Serializer

    def post(self, request):
        respuesta = ControllerUsuario_.crearusuario_(request)
        return Response(respuesta)

    def get(self, request, id_usuario_a=None):
        respuesta = ControllerUsuario_.listarusuario_(id_usuario_a)
        return Response(respuesta)

class Criticidadview(APIView):
    serializer_class = CriticidadSerializer

    def post(self, request):
        respuesta = ControllerCriticidad.crearcriticidad(request)
        return Response(respuesta)

    def get(self, request, id_criticidad=None):
        respuesta = ControllerCriticidad.listarcriticidad(id_criticidad)
        return Response(respuesta)

class EstadoMaterialview(APIView):
    serializer_class = EstadoMaterialSerializer

    def post(self, request):
        respuesta = ControllerEstadoMaterial.crearestadomaterial(request)
        return Response(respuesta)

    def get(self, request, id_estado_material=None):
        respuesta = ControllerEstadoMaterial.listarestadomaterial(id_estado_material)
        return Response(respuesta)

class EstadoPaqueteview(APIView):
    serializer_class = EstadoPaqueteSerializer

    def post(self, request):
        respuesta = ControllerEstadoPaquete.crearestadopaquete(request)
        return Response(respuesta)

    def get(self, request, id_estado_paquete=None):
        respuesta = ControllerEstadoPaquete.listarestadopaquete(id_estado_paquete)
        return Response(respuesta)

class EstadoSelloview(APIView):
    serializer_class = EstadoSelloSerializer

    def post(self, request):
        respuesta = ControllerEstadoSello.crearestadosello(request)
        return Response(respuesta)

    def get(self, request, id_estado_sello=None):
        respuesta = ControllerEstadoSello.listarestadosello(id_estado_sello)
        return Response(respuesta)

class Giroview(APIView):
    serializer_class = GiroSerializer

    def post(self, request):
        respuesta = ControllerGiro.creargiro(request)
        return Response(respuesta)

    def get(self, request, id_giro=None):
        respuesta = ControllerGiro.listarestadopaquete(id_giro)
        return Response(respuesta)

class NivelMroview(APIView):
    serializer_class = NivelMroSerializer

    def post(self, request):
        respuesta = ControllerNivelMro.crearnivelmro(request)
        return Response(respuesta)

    def get(self, request, id_nivel_mro=None):
        respuesta = ControllerNivelMro.listarnivelmro(id_nivel_mro)
        return Response(respuesta)

class NivelGastosview(APIView):
    serializer_class = NivelGastosSerializer

    def post(self, request):
        respuesta = ControllerNivelGastos.crearnivelgastos(request)
        return Response(respuesta)

    def get(self, request, id_nivel_gastos=None):
        respuesta = ControllerNivelGastos.listarnivelgastos(id_nivel_gastos)
        return Response(respuesta)

class OrdenDeCompraEstadoview(APIView):
    serializer_class = OrdenDeCompraEstadoSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraEstado.crearordendecompraestado(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta =ControllerOrdenDeCompraEstado.listarordendecompraestado(id)
        return Response(respuesta)

class OrdenDeCompraAccionview(APIView):
    serializer_class = OrdenDeCompraAccionSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraAccion.crearordendecompraaccion(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOrdenDeCompraAccion.listarordendecompraaccion(id)
        return Response(respuesta)    

class OrdenDeCompraProveedorview(APIView):
    serializer_class = OrdenDeCompraProveedorSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraProveedor.crearordendecompraproveedor(request)
        return Response(respuesta)

    def get(self, request, id_proveedor=None):
        respuesta = ControllerOrdenDeCompraProveedor.listarordendecompraproveedor(id_proveedor)
        return Response(respuesta)

class OrdenDeCompraview(APIView):
    serializer_class = OrdenDeCompraSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompra.crearordendecompra(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta =ControllerOrdenDeCompra.listarordendecompra(id)
        return Response(respuesta)

class OrdenDeCompraProductoview(APIView):
    serializer_class = OrdenDeCompraProductoSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraProducto.crearordendecompraproducto(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOrdenDeCompraProducto.listarordendecompraproducto(id)
        return Response(respuesta)

class OrdenDeCompraContizacionProductoview(APIView):
    serializer_class = OrdenDeCompraProductoSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraProducto.crearordendecompraproducto(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOrdenDeCompraProducto.listarordendecompraproducto(id)
        return Response(respuesta)
        
class OrdenDeCompraArchivoview(APIView):
    serializer_class = OrdenDeCompraArchivoSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraArchivo.crearordendecompraarchivo(request)
        return Response(respuesta)

    def get(self, request, id_orden_compra_archivo=None):
        respuesta =ControllerOrdenDeCompraArchivo.listarordendecompraarchivo(id_orden_compra_archivo)
        return Response(respuesta)

class OrdenDeCompraArchivoProveedorview(APIView):
    serializer_class = OrdenDeCompraArchivoProveedorSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraArchivoProveedor.crearordendecompraarchivoproveedor(request)
        return Response(respuesta)

    def get(self, request, id_orden_compra_archivo_proveedor=None):
        respuesta = ControllerOrdenDeCompraArchivoProveedor.listarordendecompraarchivo(id_orden_compra_archivo_proveedor)
        return Response(respuesta)

class OrdenDeCompraCotizacionview(APIView):
    serializer_class = OrdenDeCompraCotizacionSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraCotizacion.crearordendecompracotizacion(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOrdenDeCompraCotizacion.listarordendecompracotizacion(id)
        return Response(respuesta)

class OrdenDeCompraArchivoCostoview(APIView):
    serializer_class = OrdenDeCompraArchivoCostoSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraArchivoCosto.crearordendecompraarchivocosto(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOrdenDeCompraArchivoCosto.listarordendecompraarchivocosto(id)
        return Response(respuesta)

class OrdenDeCompraEmailVistoview(APIView):
    serializer_class = OrdenDeCompraEmailVistoSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraEmailVisto.crearordendecompraemailvisto(request)
        return Response(respuesta)

    def get(self, request, orden_de_compra_email_visto=None):
        respuesta = ControllerOrdenDeCompraEmailVisto.listarordendecompraemailvisto(orden_de_compra_email_visto)
        return Response(respuesta)

class OrdenDeCompraHistorialview(APIView):
    serializer_class = OrdenDeCompraHistorialSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraHistorial.crearordendecomprahistorial(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOrdenDeCompraHistorial.listarordendecompraemailvisto(id)
        return Response(respuesta)

class OrdenDeCompraMensajeview(APIView):
    serializer_class = OrdenDeCompraMensajeSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraMensaje.crearordendecompramensaje(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOrdenDeCompraMensaje.listarordendecompramensaje(id)
        return Response(respuesta)

class OrdenDeCompraPresupuestoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrdenDeCompraPresupuestoSerializer

    def post(self, request):
        respuesta = ControllerOrdenDeCompraPresupuesto.crearordendecomprapresupuesto(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOrdenDeCompraPresupuesto.listarordendecomprapresupuesto(id)
        return Response(respuesta)

class EstadoProductoRecibidoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Estado_Producto_Recibido

    def post(self, request):
        respuesta = ControllerEstadoProductoRecibido.crearestadoproductorecibido(request)
        return Response(respuesta)

    def get(self, request, id_estado_producto_recibido=None):
        respuesta = ControllerEstadoProductoRecibido.listarestadoproductorecibido(id_estado_producto_recibido)
        return Response(respuesta)

class OcChatview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Oc_Chat

    def post(self, request):
        respuesta = ControllerOcChat.crearocchat(request)
        return Response(respuesta)

    def get(self, request, id_oc_chat=None):
        respuesta = ControllerOcChat.listarocchat(id_oc_chat)
        return Response(respuesta)

class OcEstadoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Oc_Estado

    def post(self, request):
        respuesta = ControllerOcEstado.creaocestado(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOcEstado.listarocestado(id)
        return Response(respuesta)

class OcMensajeProveedorview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Oc_Mensaje_Proveedor

    def post(self, request):
        respuesta = ControllerOcMensajeProveedor.creaocmensajeproveedor(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOcMensajeProveedor.listarocmensajeproveedor(id)
        return Response(respuesta)

class OcMensajeUsuarioview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Oc_Mensaje_Usuario

    def post(self, request):
        respuesta = ControllerOcMensajeUsuario.creaocmensajeusuario(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOcMensajeUsuario.listarocmensajeusuario(id)
        return Response(respuesta)

class OcPresupuestoCostosview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Oc_Presupuesto_Costos

    def post(self, request):
        respuesta = ControllerOcPresupuestoCostos.creaocpresupuestocostos(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOcPresupuestoCostos.listarocpresupuestocostos(id)
        return Response(respuesta)

class OcProdview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Oc_Prod

    def post(self, request):
        respuesta = ControllerOcProd.creaocprod(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOcProd.listarocprod(id)
        return Response(respuesta)

class OcProvview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Oc_Prov

    def post(self, request):
        respuesta = ControllerOcProv.creaocprov(request)
        return Response(respuesta)

    def get(self, request, id=None):
        respuesta = ControllerOcProv.listarocprov(id)
        return Response(respuesta)

class OrdenDecompraAprovadaview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Orden_De_Compra_Aprovada

    def post(self, request):
        respuesta = ControllerOrdenDeCompraAprovada.creaocaprovada(request)
        return Response(respuesta)

    def get(self, request, id_orden_compra_aprovada=None):
        respuesta = ControllerOrdenDeCompraAprovada.listarocaprovada(id_orden_compra_aprovada)
        return Response(respuesta)

class ProveedorGiroview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Proveedor_Giro

    def post(self, request):
        respuesta = ControllerProveedorGiro.crearproveedorgiro(request)
        return Response(respuesta)

    def get(self, request, id_proveeor_giro=None):
        respuesta = ControllerProveedorGiro.listarproveedorgiro(id_proveeor_giro)
        return Response(respuesta)

class RequisicionAprovadaview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Requisicion_Aprovada

    def post(self, request):
        respuesta = ControllerRequisicionAprovada.crearrequisicionaprovada(request)
        return Response(respuesta)

    def get(self, request, id_requisicion_aprovada=None):
        respuesta = ControllerRequisicionAprovada.listarrequisicionaprovada(id_requisicion_aprovada)
        return Response(respuesta)

class UsuarioContrasenaview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Usuario_Contrasena

    def post(self, request):
        respuesta = ControllerUsuarioContrasena.crearusuariocontrasena(request)
        return Response(respuesta)

    def get(self, request, id_usuario_contrasena=None):
        respuesta = ControllerUsuarioContrasena.listarusuariocontrasena(id_usuario_contrasena)
        return Response(respuesta)

class UsuarioEventoview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Usuario_Evento

    def post(self, request):
        respuesta = ControllerUsuarioEvento.crearusuarioevento(request)
        return Response(respuesta)

    def get(self, request, id_usuario_evento=None):
        respuesta = ControllerUsuarioEvento.listarusuarioevento(id_usuario_evento)
        return Response(respuesta)

class UsuarioMroview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Usuario_Mro

    def post(self, request):
        respuesta = ControllerUsuarioMro.crearusuariomro(request)
        return Response(respuesta)

    def get(self, request, id_usuario_mro=None):
        respuesta = ControllerUsuarioMro.listarusuariomro(id_usuario_mro)
        return Response(respuesta)

class UsuarioSesionview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Usuario_Sesion

    def post(self, request):
        respuesta = ControllerUsuarioSesion.crearusuariosesion(request)
        return Response(respuesta)

    def get(self, request, id_usuario_sesion=None):
        respuesta = ControllerUsuarioSesion.listarusuariosesion(id_usuario_sesion)
        return Response(respuesta)

class UsuarioActivoeamview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Usuario_Activoeam

    def post(self, request):
        respuesta = ControllerUsuarioActivoeam.crearusuarioactivoeam(request)
        return Response(respuesta)

    def get(self, request, id_usuario_activoeam=None):
        respuesta = ControllerUsuarioActivoeam.listarusuarioactivoeam(id_usuario_activoeam)
        return Response(respuesta)

