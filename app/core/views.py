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

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import EquipoCategoriaEstatusSerializaer, JornadaHorasSerializer, JornadaSerializer, CentroCostoSerializer, ClienteSerializer, Contacto_ProveedorSerializer, Departamento_TurnoSerializer, EstatusSerializer, IdiomaSerializer, Inventario_CategoriaSerializer, PuestoSerializer, RolSerializer, ScopeSerializer, Tipo_RolSerializer, TurnoSerializer, UserSerializer, AuthTokenSerializer, DepartamentoSerializer, UsuarioSerializer, CentroCostoSerializer, ProveedorSerializer
from .serializers import Usuario_Lat_Lng_Serializer, TurnoSerializer, UnidadSerializer, setup_Serializer, EquipoCategoriaSerializer

from .models import Unidad

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
        if not generar_unidades and not generar_categorias and not generar_equipo_categoria_estatus and not generar_equipo_categoria :
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